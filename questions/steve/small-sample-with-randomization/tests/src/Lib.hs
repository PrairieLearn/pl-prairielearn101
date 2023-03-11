module Lib where

pairMap _ [] = []
pairMap _ [x] = []
pairMap op (x:y:xs) = (x `op` y) : pairMap op (y:xs)

main910189eb_f1c1_46e0_85e6_72dfcc70a42e :: [Int] -> Int
main910189eb_f1c1_46e0_85e6_72dfcc70a42e [] = 0
main910189eb_f1c1_46e0_85e6_72dfcc70a42e [x] = x
main910189eb_f1c1_46e0_85e6_72dfcc70a42e xs = maximum (pairMap (-) xs)
