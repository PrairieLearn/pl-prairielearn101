{-# LANGUAGE DeriveFoldable      #-}
{-# LANGUAGE DeriveGeneric       #-}
{-# LANGUAGE ScopedTypeVariables #-}
{-# LANGUAGE StandaloneDeriving  #-}

-- {{#params}}

import Test.Framework (defaultMain, testGroup)
import Test.Framework.Providers.QuickCheck2 (testProperty)

import Test.QuickCheck
import Test.QuickCheck.Monadic

import Data.Foldable
import qualified Data.List as List
import GHC.Generics (Generic)

import qualified Lib
import GHC.Base (String, Bool, liftM2)

import Text.Regex.TDFA


main :: IO ()
main = defaultMain tests

tests =
  [ testGroup
      "=G= All tests"
      [ testProperty
          "=P= Used the Required Words (2 points)"
          $ propWordsCorrect
        -- {{#cases}}
      , testProperty
          "=P= Well-formed constructors, Version {{number}} (1 points)"
          $ ioProperty (isCaseOf (tail [""{{#words}}, "{{.}}"{{/words}}]) <$> studentWords)
        -- {{/cases}}
      ]
  ]

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


-- | True if the first list represents an intact case within the second.
-- An intact case starts with either @=@ or @|@ and ends with either @|@
-- or the end of the list.
isCaseOf :: [String] -> [String] -> Bool
caseWords `isCaseOf` answerWords = 
  (["|"] ++ caseWords ++ ["|"]) `List.isInfixOf` answerWords ||
  (["="] ++ caseWords ++ ["|"]) `List.isInfixOf` answerWords ||
  (["|"] ++ caseWords) `List.isSuffixOf` answerWords ||
  (["="] ++ caseWords) `List.isSuffixOf` answerWords

studentWords :: IO [String]
studentWords = words
  where fileContents :: IO String
        fileContents = readFile "src/Lib.hs"

        headerContents :: IO String
        headerContents = readFile "src/Lib-header.hs"

        trueFileContents :: IO String
        trueFileContents = drop <$> (length <$> headerContents) <*> fileContents

        words :: IO [String]
        words = getWords <$> trueFileContents

propWordsCorrect :: Property
propWordsCorrect = ioProperty $ match >>= pure . (=== WordsMatch [] [])
  where match :: IO WordsMatch
        match = makeWordsMatch solnWords <$> studentWords



-- {{/params}}
