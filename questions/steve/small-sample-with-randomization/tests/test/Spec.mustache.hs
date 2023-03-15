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

main :: IO ()
main = defaultMain tests

testF = Lib.main910189eb_f1c1_46e0_85e6_72dfcc70a42e

pairMap _ [] = []
pairMap _ [x] = []
pairMap op (x:y:xs) = (x `op` y) : pairMap op (y:xs)

absDiff x y = abs (x - y)

getOp "difference" = (-)
getOp "product" = (*)
getOp "sum" = (+)
getOp "absolute difference (absolute value of the difference)" = absDiff
getOp _ = (-)

getAggregator "largest" = maximum
getAggregator "smallest" = minimum
getAggregator _ = maximum

getValue "0" _ = 0
getValue "the single element's value" n = n
getValue _ n = n

soln :: [Int] -> Int
soln [] = 0
soln [x] = getValue "{{valOrZero}}" x
soln xs = (getAggregator "{{superlative}}") (pairMap (getOp "{{op}}") xs)


tests =
  [ testGroup
      "=G= base cases"
      [
        testProperty
          "=P= produces 0 for [] (1 points)"
          (testF [] === 0),
        testProperty
          "=P= produces {{valOrZero}} for a one-element list (1 points)"
          (\n -> testF [n] === getValue "{{valOrZero}}" n)
      ],
    testGroup
      "=G= longer lists"
      [
        testProperty
          "=P= produces a correct result for a longer list (2 points)"
          (\(n1, n2, ns) -> testF (n1:n2:ns) === soln (n1:n2:ns))
      ]
  ]


-- {{/params}}
