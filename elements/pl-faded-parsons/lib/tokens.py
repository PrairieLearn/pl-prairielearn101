from dataclasses import dataclass, field
from enum import IntEnum
from json import JSONDecoder
from re import Pattern, finditer, match as test
from typing import Any

from lib.consts import MAIN_PATTERN, REGION_IMPORT_PATTERN
from lib.io_helpers import read_region_source_lines, format_ln


@dataclass(frozen=True, slots=True)
class RegionDelim:
    lineno: int
    name: str


class TokenType(IntEnum):
    COMMENT = -1
    UNMATCHED = 0
    STRING = 1
    DOCSTRING = 2


@dataclass(frozen=True, slots=True)
class Token:
    """ A record representing a single token of text """
    lineno: int
    type: TokenType
    text: str
    region: str


@dataclass(frozen=True, slots=True)
class Tokens:
    """ A record of source_path, data, and metadata from a lex """
    source_path: str
    data: list[Token]
    metadata: dict[str, Any]


@dataclass(slots=True)
class Lexer:
    """ A helper class for lexing """
    source_path: str = None
    data: list[Token] = field(default_factory=list)
    current_region: RegionDelim = None

    def format_ln(self, line_number: int):
        return format_ln(self.source_path, line_number)

    def put(self, t: Token):
        self.data.append(t)

    def put_curr(self, lineno: int, type: TokenType, text: str):
        curr_region = self.current_region.name if self.current_region else ''
        self.put(Token(lineno, type, text, curr_region))

    def put_region_delim(self, region_delim: str, lineno: int):
        if not len(region_delim):
            raise SyntaxError("Regions must be named (ie ## test ##) " +
                self.format_ln(lineno))

        if self.current_region:
            if region_delim != self.current_region.name:
                raise SyntaxError("Region \"{}\" began at {} before \"{}\" ended.".format(
                    region_delim,
                    self.format_ln(lineno),
                    self.current_region.lineno,
                ))

            self.current_region = None
            return

        import_region = test(REGION_IMPORT_PATTERN, region_delim)

        if not import_region:
            self.current_region = RegionDelim(lineno + 1, region_delim)
            if any(t.region == region_delim and t.text for t in self.data):
                self.put_curr(lineno, TokenType.UNMATCHED, '\n')
            return

        region_source, alias = import_region.groups()
        try:
            imported_lines = read_region_source_lines(self.source_path, region_source)
            imported_regions = lex(imported_lines, source_path=self.source_path)
            for t in imported_regions.data:
                if t.region:
                    raise SyntaxError('Imported regions cannot contain regions. ' +
                        self.format_ln(lineno))
                self.put(Token(lineno, t.type, t.text, alias))
        except FileNotFoundError:
            raise FileNotFoundError(
                "Region \"{}\" failed on import. Could not find {} at {}".format(
                    alias, region_source, self.format_ln(lineno)))
        except OSError as e:
            raise OSError(
                "Region \"{}\" failed on import. Could not read {}:\n\t\t{}\n\tat {}".format(
                    alias, region_source, e.strerror, self.format_ln(lineno)))

    def finish(self) -> Tokens:
        if self.current_region:
            raise SyntaxError("File ended before \"{}\" {} ended".format(
                self.current_region.name,
                self.format_ln(self.current_region.lineno)
            ))

        def unparse(tkns: list[Token]):
            return ''.join(q_tkn.text for q_tkn in tkns)

        data = []
        metadata = []
        for t in self.data:
            if t.region == 'metadata':
                metadata.append(t)
            else:
                data.append(t)

        if metadata:
            metadata = unparse(metadata)
            # strict allows control chars (\n \t \r) in strings
            metadata = metadata and JSONDecoder(strict=False).decode(metadata)

        # replace None, 0, '', or [] with {}
        metadata = metadata or {}

        if not isinstance(metadata, dict):
            raise SyntaxError('Metadata region must be empty or a JSON object.')

        return Tokens(self.source_path, data, metadata)


def regex_chunk_lines(pattern: Pattern, txt: str, *, line_number = 1):
    """ Chunks `txt` up using `finditer(pattern)`, alternating
        between `pattern` matches and unmatched pieces of `txt`.

        Yields the line number of the start of the chunk, the success flag,
        and chunk data. If the success flag is `True`, then the chunk data
        is an `re.Match` object. Otherwise (when the success flag is false)
        the chunk data is a `str` object containing all the text that did
        not match the pattern.
    """
    last_end = 0
    for match in finditer(pattern, txt):
        start, end = match.span()

        unmatched = txt[last_end:start]
        yield (line_number, False, unmatched)

        line_number += sum(1 for x in unmatched if x == '\n')
        last_end = end

        yield (line_number, True, match)

        line_number += sum(1 for x in txt[start:end] if x == '\n')

    # don't forget everything after the last match!
    unmatched = txt[last_end:]
    yield (line_number, False, unmatched)


def lex(source_code: str, *, source_path: str = None) -> Tokens:
    """ Get the tokens from source_code """
    # (exclusive) end of the last match
    lexer = Lexer(source_path)

    for line_number, found, chunk in regex_chunk_lines(MAIN_PATTERN, source_code):
        # found is False when chunk is the text between matches
        if not found:
            lexer.put_curr(line_number, TokenType.UNMATCHED, chunk)
            continue

        # exactly one is non-None
        region_delim, comment, docstring, string = chunk.groups()

        if region_delim:
            lexer.put_region_delim(region_delim, line_number)
        elif comment:
            lexer.put_curr(line_number, TokenType.COMMENT, comment)
        elif docstring:
            lexer.put_curr(line_number, TokenType.DOCSTRING, docstring)
        elif string:
            lexer.put_curr(line_number, TokenType.STRING, string)
        else:
            raise Exception("Unreachable! Inexhaustive match groups.\n", f"{line_number=}, {found=} \n{chunk.groups()}")

    return lexer.finish()
