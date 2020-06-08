import System.Environment
import System.IO
import Data.List

type Sequence = [Int]
type Board = [Sequence]

toInt :: [Char] -> Int
toInt s = read s :: Int

toIntList :: [Char] -> Sequence
toIntList s = [ toInt [c] | c <- s ]

getNRows :: Board -> Int 
getNRows board = result
    where {result = length board; }


main = do
    print "hello"