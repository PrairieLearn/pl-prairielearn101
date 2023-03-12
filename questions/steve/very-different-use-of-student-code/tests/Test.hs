import Text.Regex.TDFA
import qualified Data.List as List

specialRE, opRE, normalRE :: String
specialRE = "[][(),;`{}]"
opRE = "[!#$%&*+./<=>?@\\|~:^-]"
normalRE = "[A-Za-z0-9_\"']"

wordRE :: String
wordRE = "(" ++ specialRE ++ 
         "|" ++ opRE ++ "+" ++
         "|" ++ normalRE ++ "+" ++
         ")"

-- | If no mustache replacement happens, gets a default.
soln :: String
soln = if "{{solution}}" == "{" ++ "{solution}" ++ "}"
       then "data Bet = Won Int | Lost Int | Pending Int | Tied"
       else "{{solution}}"

getWords :: String -> [String]
getWords = getAllTextMatches . (=~ wordRE)

solnWords :: [String]
solnWords = getWords soln

data WordsMatch = WordsMatch {
  addedWords :: [String],
  missingWords :: [String]
} deriving (Show, Eq)

makeWordsMatch :: [String] -> [String] -> WordsMatch
makeWordsMatch solnWords givenWords = buildMatch (WordsMatch [] []) alphaSoln alphaGiven
  where alphaSoln = List.sort solnWords
        alphaGiven = List.sort givenWords

        buildMatch acc [] extras = acc { addedWords = extras ++ (addedWords acc) }
        buildMatch acc missings [] = acc { missingWords = missings ++ (missingWords acc) }
        buildMatch acc (soln:solns) (extra:extras)
          | soln == extra = buildMatch acc solns extras
          | soln < extra = buildMatch (acc {missingWords = soln : (missingWords acc)}) solns (extra:extras)
          | otherwise = buildMatch (acc {addedWords = extra : (addedWords acc)}) (soln:solns) extras
