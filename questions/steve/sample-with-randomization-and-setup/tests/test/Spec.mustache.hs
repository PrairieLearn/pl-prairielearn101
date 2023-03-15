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

instance Arbitrary Lib.{{TypeName}} where
  arbitrary = oneof [
    {{#Cases}}(const Lib.{{Constructor}}) <$> return True{{#Types}} <*> arbitrary{{/Types}},
    {{/Cases}}{{#LastCase}}(const Lib.{{Constructor}}) <$> return True{{#Types}} <*> arbitrary{{/Types}}{{/LastCase}}]

{{#Cases}}soln (Lib.{{Constructor}}{{#Patterns}} {{.}}{{/Patterns}}) = {{{Result}}}
{{/Cases}}{{#LastCase}}soln (Lib.{{Constructor}}{{#Patterns}} {{.}}{{/Patterns}}) = {{{Result}}}{{/LastCase}}

tests =
  [ testGroup
      "=G= Just correctness testing"
      [
        testProperty
          "=P= works on arbitrary input (1 points)"
          (\value -> Lib.extract{{SelectedTypeID}} value === soln value)
      ]
  ]


-- {{/params}}
