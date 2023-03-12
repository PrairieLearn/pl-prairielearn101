module Lib where

hidden_main_db300289_e071_4038_a55f_c847d0bd9dfa :: [Bool] -> [Bool] -> Bool
hidden_main_db300289_e071_4038_a55f_c847d0bd9dfa = op

op :: [Bool] -> [Bool] -> Bool
op [] [] = False
op [] x = op x x
op x [] = op x x
op (True:_) _ = True
op _ (True:_) = True
op _ _ = False
