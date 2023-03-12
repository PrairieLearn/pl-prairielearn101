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

tests =
  [ testGroup
      "=G= Plain [True,...] and [False,...]"
      [ testProperty
          "=P= [True,...] only (1 points)"
          $ (\(NonEmpty lbs, NonEmpty rbs) -> (head lbs) && (head rbs) ==> propWorksOn lbs rbs),
        testProperty
          "=P= [False,...] only (1 points)"
          $ (\(NonEmpty lbs, NonEmpty rbs) -> not (head lbs) && not (head rbs) ==> propWorksOn lbs rbs),
        testProperty
          "=P= mix of [True,...] and [False,...] (3 points)"
          $ (\(NonEmpty lbs, NonEmpty rbs) -> (head lbs) /= (head rbs) ==> propWorksOn lbs rbs)
      ],
    testGroup
      "=G= Other values"
      [ testProperty
          "=P= only empty lists (2 points)"
          $ propWorksOn [] [],
        testProperty
          "=P= mix of at least one empty list and other values (3 points)"
          $ (\(NonEmpty bs) -> propWorksOn bs [] .&&. propWorksOn [] bs)
      ]
  ]

optiPessiMaybeVal = "{{optiPessiMaybeVal}}" == "True"

op = if "{{op}}" == "and" then (&&) else (||)

opEquiv :: [Bool] -> [Bool] -> Bool
opEquiv (lb:_) (rb:_) = op lb rb
opEquiv [] [] = optiPessiMaybeVal
opEquiv [] x = opEquiv x x
opEquiv x [] = opEquiv x x

sop = Lib.hidden_main_db300289_e071_4038_a55f_c847d0bd9dfa

propWorksOn :: [Bool] -> [Bool] -> Property
propWorksOn lbs rbs = opEquiv lbs rbs === sop lbs rbs

-- {{/params}}
