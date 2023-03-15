module Lib where

data QuuxEggs = GizmoSmurf String Double
              | GonkStad
              | Fizz Double
              | XyzzyFnord [Bool] Double

extractDouble :: QuuxEggs -> Double
extractDouble GonkStad = 0.0
extractDouble (GizmoSurf _ d) = d
extractDouble (Fizz d) = d
extractDouble (XyzzyFnord _ d) = d