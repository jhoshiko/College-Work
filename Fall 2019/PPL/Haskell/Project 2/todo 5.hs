import System.Environment
import System.IO
import Data.List

type Sequence = [Int]
type Board = [Sequence]

enumerate = zip [0..9]

toInt :: [Char] -> Int
toInt s = read s :: Int

toIntList :: [Char] -> Sequence
toIntList s = [ toInt [c] | c <- s ]

getEmptySpot :: Board -> (Int, Int)
getEmptySpot board = result
    where {result = head [ (x, y) | (x, row) <- enumerate board
                     , (y, value) <- enumerate row
                     , value == 0]}

main = do
    let row0 = [5,3,0,0,7,0,0,0,0]
    let row1 = [6,0,0,1,9,5,0,0,0]
    let row2 = [0,9,8,0,0,0,0,6,0]
    let row3 = [8,0,0,0,6,0,0,0,3]
    let row4 = [4,0,0,8,0,3,0,0,1]
    let row5 = [7,0,0,0,2,0,0,0,6]
    let row6 = [0,6,0,0,0,0,2,8,0]
    let row7 = [0,0,0,4,1,9,0,0,5]
    let row8 = [0,0,0,0,8,0,0,7,9]
    let thing = [row0, row1, row2, row3, row4, row5, row6, row7, row8]
    let result = getEmptySpot thing
    print result