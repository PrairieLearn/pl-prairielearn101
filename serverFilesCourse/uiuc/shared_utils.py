import html
import re
from inspect import signature
from itertools import chain, combinations, count, product
from string import ascii_lowercase, ascii_uppercase
from typing import (
    Any,
    Callable,
    Dict,
    Generator,
    Iterable,
    List,
    Literal,
    Optional,
    Set,
    Tuple,
    TypedDict,
    TypeVar,
    Union,
)

from typing_extensions import NotRequired, assert_never


class PartialScore(TypedDict):
    "A class with type signatures for the partial scores dict"
    score: Optional[float]
    weight: NotRequired[int]
    feedback: NotRequired[str]


class QuestionData(TypedDict):
    "A class with type signatures for the data dictionary"

    params: Dict[str, Any]
    correct_answers: Dict[str, Any]
    submitted_answers: Dict[str, Any]
    format_errors: Dict[str, Any]
    partial_scores: Dict[str, PartialScore]
    score: float
    feedback: Dict[str, Any]
    variant_seed: int
    options: Dict[str, Any]
    raw_submitted_answers: Dict[str, Any]
    editable: bool
    panel: Literal["question", "submission", "answer"]
    extensions: Dict[str, Any]

# TODO replace this with question data once every data dict signature is migrated over
QuestionDataTemp = Union[QuestionData, Dict[str, Any]]


def binary_search(
    lo: int, hi: int, condition_fn: Callable[[int], bool]
) -> Optional[int]:
    """
    A parameterized binary search that searches an arbitrary range [lo, hi) for the
    lowest value condition_fn returns True for within the range, returning None if it is never true
    """

    assert lo <= hi

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if condition_fn(mid):  # Midpoint could be too big
            hi = mid
        else:
            lo = mid + 1

    if not condition_fn(lo):
        return None

    return lo


def is_power_of_base(num: int, base: int) -> bool:
    """
    Returns True if there is some integer x such that base^x = num,
    False otherwise
    """
    smallest_pow_greater_than = binary_search(0, num, lambda x: base**x >= num)

    if smallest_pow_greater_than is not None:
        return num == base**smallest_pow_greater_than

    raise ValueError(f"Binary search for {base}^x = {num} failed")
    # shouldn't ever get here


def is_perfect_power(num: int, power: int) -> bool:
    """
    Returns True if there is some integer x such that x^power = num
    False otherwise
    """
    smallest_base_greater_than = binary_search(0, num, lambda x: x**power >= num)

    if smallest_base_greater_than is not None:
        return num == smallest_base_greater_than**power

    raise ValueError(f"Binary search for x^{power} = {num} failed")
    # shouldn't ever get here


def form_string_from_shorthand(shorthand: str) -> str:
    """
    Expands a shorthand binary string into its expanded form (e.g. '0^{3}' --> '000').
    If the input is a binary string with no shorthand, the return value is the same as the input.
    If the input is 'e' (for epsilon), the return value is an empty string.
    @param shorthand string
        binary string that may contain shorthand
    @return string
        expanded form of shorthand string
    @throws ValueError
        if input shorthand string is malformed or empty (e.g. mismatched braces)
    """
    if shorthand == "e":
        return ""

    expanded_str_list = []
    pattern = re.compile(r"(0|1)\^{(\d+)}|0|1")
    match_intervals = []
    matches = pattern.finditer(shorthand)
    for match in matches:
        if match.group(1) is None:
            expanded_str_list.append(match.group(0))
        else:
            expanded_str_list.append(match.group(1) * int(match.group(2)))
        match_intervals.append([match.start(), match.end()])

    if len(match_intervals) == 0:
        raise ValueError(f"{shorthand} is not valid shorthand for a binary string")

    is_full_match = match_intervals[0][0] == 0 and match_intervals[-1][1] == len(
        shorthand
    )
    for index in range(len(match_intervals) - 1):
        if match_intervals[index][1] != match_intervals[index + 1][0]:
            is_full_match = False
            break

    if not is_full_match:
        raise ValueError(f"{shorthand} is not valid shorthand for a binary string")
    return "".join(expanded_str_list)


def integer_is_outside_PL_limit(number: int) -> bool:
    "Returns True if integer is outside of PL allowable range"
    LIMIT = 2**53 - 1
    return not (-LIMIT <= number <= LIMIT)


# https://stackoverflow.com/questions/29351492/how-to-make-a-continuous-alphabetic-list-python-from-a-z-then-from-aa-ab-ac-e/29351603#29351603
# labels = list(itertools.islice(iter_all_strings_lower(), number_of_strings))

def iter_all_strings(Uppercase: bool = True) -> Generator[str, None, None]:
    ascii_set = ascii_uppercase if Uppercase else ascii_lowercase
    for size in count(1):
        for s in product(ascii_set, repeat=size):
            yield "".join(s)


def remove_partial_credit_display(data: QuestionDataTemp, question_name: str) -> None:
    "Removes partial credit display for a specific question"
    scores_dict = data["partial_scores"]

    if question_name not in scores_dict:
        raise ValueError(
            f"Question {question_name} is not present in the partial scores dictionary"
        )

    scores_dict[question_name] = {"score": None}


def sanitize_input(student_ans: str) -> str:
    "Run unidecode and remove any extra spaces"
    # TODO move this import to the top once text_unidecode is added
    # to the python grader image
    from text_unidecode import unidecode

    return unidecode(student_ans).replace(" ", "")


def tokenize_string(string: str) -> List[str]:
    "Removes all spaces from string and splits on comma outside parethesis into a list"
    # Regex from here: https://stackoverflow.com/questions/26633452/how-to-split-by-commas-that-are-not-within-parentheses
    string = sanitize_input(string)
    return list(re.split(r",\s*(?![^()]*\))", string.replace(" ", "").strip(",")))


def tokenize_string_without_set(student_answer: str) -> List[str]:
    "Wrapper Function of tokenize_string that Checks if Student has Errorneous Set Braces"
    if student_answer.startswith("{") or student_answer.endswith("}"):
        raise ValueError(
            "This input field is not a set, so it does not require curly braces"
        )
    return tokenize_string(student_answer)


def tokenize_string_set(string: str) -> List[str]:
    "Turn string representing a set as input into a list of tokens."
    string = string.strip()
    # Handle empty set symbol
    if string == "∅":
        string = "{}"
    elif not string.startswith("{") or not string.endswith("}"):
        raise ValueError(
            "Make sure to format your answer with curly braces to denote a set"
        )
    string = string[1:-1]
    return tokenize_string(string)


def grade_question_tokenized(
    data: QuestionDataTemp,
    question_name: str,
    expected_answer_optional: Optional[str] = None,
    weight: int = 1,
) -> None:
    "Grade question named question_name where student input needs to be tokenized with a set"

    expected_answer = (
        expected_answer_optional
        if expected_answer_optional
        else data["correct_answers"][question_name]
    )
    is_expected_set = (
        expected_answer.startswith("{") and expected_answer.endswith("}")
    ) or expected_answer == "∅"
    tokenize_function = (
        tokenize_string_set if is_expected_set else tokenize_string_without_set
    )
    grade_question_parameterized(
        data,
        question_name,
        lambda student_ans: (
            set(tokenize_function(student_ans))
            == set(tokenize_function(expected_answer)),
            None,
        ),
        weight,
    )


def grade_question_parameterized(
    data: QuestionDataTemp,
    question_name: str,
    grade_function: Callable[[Any], Tuple[Union[bool, float], Optional[str]]],
    weight: int = 1,
    feedback_field_name: Optional[str] = None,
) -> None:
    """
    Grade question question_name, marked correct if grade_function(student_answer) returns True in
    its first argument. grade_function should take in a single parameter (which will be the submitted
    answer) and return a 2-tuple.
        - The first element of the 2-tuple should either be:
            - a boolean indicating whether the question should be marked correct
            - a partial score between 0 and 1, inclusive
        - The second element of the 2-tuple should either be:
            - a string containing feedback
            - None, if there is no feedback (usually this should only occur if the answer is correct)

    Note: if the feedback_field_name is the same as the question name,
    then the feedback_field_name does not need to be specified.
    """

    # Create the data dictionary at first
    data["partial_scores"][question_name] = {"score": 0.0, "weight": weight}

    try:
        submitted_answer = get_submitted_answer(data, question_name)
    except KeyError:
        # Catch error if no answer submitted
        data["format_errors"][question_name] = "No answer was submitted"
        return

    # Try to grade, exiting if there's an exception
    try:
        result, feedback_content = grade_function(submitted_answer)

        # Check _must_ be done in this order. Int check is to deal with subclass issues
        if isinstance(result, bool):
            partial_score = 1.0 if result else 0.0
        elif isinstance(result, (float, int)):
            assert 0.0 <= result <= 1.0
            partial_score = result
        else:
            assert_never(result)

    except ValueError as err:
        # Exit if there's a format error
        data["format_errors"][question_name] = html.escape(str(err))
        return

    # Set question score if grading succeeded
    data["partial_scores"][question_name]["score"] = partial_score

    # Put all feedback here
    if feedback_content:
        # Check for unescaped bad stuff in feedback string
        if isinstance(submitted_answer, str):
            contains_bad_chars = all(x in submitted_answer for x in {"<", ">"})
            if contains_bad_chars and submitted_answer in feedback_content:
                raise ValueError(
                    f"Unescaped student input should not be present in the feedback for {question_name}."
                )

        data["partial_scores"][question_name]["feedback"] = feedback_content

        if not feedback_field_name:
            feedback_field_name = question_name

        set_feedback(data, feedback_field_name, feedback_content)


def set_holistic_feedback(
    data: QuestionDataTemp,
    feedback_field_name: str,
    feedback_function: Callable[..., Optional[str]],
    hide_partial_scores=False,
) -> None:
    """
    Given the list of question names (which have already been graded), set feedback in
    feedback_field_name based on the behavior of feedback_function. Question
    names are taken from the arguments of feedback_function.
    Also have the option to hide partial scores, which causes the red 0% badges and the
    green 100% badges to not be displayed next to every input/dropdown.
    Should be called AFTER grading

    This is generally used for a statement containing multiple inputs and/or dropdowns
    where it makes more sense to give feedback on the statement as a whole rather than
    giving feedback on each individual input/dropdown.
    """

    submitted_answers = data["submitted_answers"]
    partial_scores = data["partial_scores"]

    # Get question names from arguments
    question_names = signature(feedback_function).parameters.keys()

    for question_name in question_names:
        if question_name not in submitted_answers:
            raise ValueError(
                f"Student answer for {question_name} not present in submitted answers."
            )

        if question_name not in partial_scores:
            raise ValueError(
                f"Partial score for {question_name} not present in partial scores."
            )

    # TODO if needed, add custom exceptions to handle multiple format errors
    argdict = {name: submitted_answers[name] for name in question_names}
    feedback_content = feedback_function(**argdict)

    # Set question feeback
    if feedback_content:
        set_feedback(data, feedback_field_name, feedback_content)

    # Remove partial scores
    if hide_partial_scores:
        for question_name in question_names:
            partial_scores.pop(question_name)


def get_partial_score(data: QuestionDataTemp, question_name: str) -> float:
    "Get partial score for question_name in data dictionary"
    score = data["partial_scores"][question_name]["score"]

    if score is None:
        return 0.0

    return score


def get_submitted_answer(data: QuestionDataTemp, question_name: str) -> Any:
    "Get submitted_answer for question_name in data dictionary."
    return data["submitted_answers"][question_name]


def get_question_weight(data: QuestionDataTemp, question_name: str) -> int:
    "Get question weight for question_name in data dictionary"
    return data["partial_scores"][question_name]["weight"]

def set_correct_answer(data: QuestionDataTemp, question_name: str, value: Any) -> None:
    "Set correct answer for question_name in data dictionary"
    data["correct_answers"][question_name] = value


def set_feedback(
    data: QuestionDataTemp, feedback_field_name: str, feedback_content: str
) -> None:
    "Set feedback for feedback_field_name in data dictionary"
    data["feedback"][feedback_field_name] = feedback_content


PowerSetT = TypeVar("PowerSetT")


def sized_powerset(
    iterable: Iterable[PowerSetT], min_size: int = 0, max_size: Optional[int] = None
) -> Iterable[Tuple[PowerSetT, ...]]:
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3) in increasing size"
    s = list(iterable)

    if max_size is None:
        max_size = len(s)
    elif max_size > len(s):
        raise ValueError(
            f"max_size parameter {max_size} is greater than the length of the input iterable"
        )

    return chain.from_iterable(
        combinations(s, r) for r in range(min_size, max_size + 1)
    )


def strings_of_length_at_most_n(
    lower_bound: int, n: int, *, alphabet: Set[str] = {"0", "1"}
) -> Generator[str, None, None]:
    return (
        "".join(char_list)
        for char_list in chain.from_iterable(
            product(alphabet, repeat=k) for k in range(lower_bound, n + 1)
        )
    )


def replace_empty(x: str) -> str:
    return x if x else "ε"


def float_equals(float_1: float, float_2: float, eps: float = 0.0001) -> bool:
    "Return true if floating point equality up to eps"
    return abs(float_1 - float_2) <= eps


T = TypeVar("T")


def list_as_set(elem_list: List[T]) -> Set[T]:
    """
    Transforms a list to a set, raising an exception if the input has duplicates.
    """
    elem_set = set(elem_list)

    if len(elem_set) != len(elem_list):
        raise ValueError(f"Input list {str(elem_list)} has duplicates.")

    return elem_set


def has_no_leading_palindrome(string: str, min_size: int) -> bool:
    n = len(string)
    for length in range(min_size, n + 1):
        temp = string[0:length]
        if temp == temp[::-1]:
            return False
    return True


def list_to_english(items: Optional[List[str]]) -> str:
    if not items:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        a, b = items
        return f"{a} and {b}"

    *all_but_last, last = items
    return f'{", ".join(all_but_last)}, and {last}'
