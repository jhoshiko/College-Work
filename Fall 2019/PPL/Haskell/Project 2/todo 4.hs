import System.Environment
import System.IO
import Data.List

type Sequence = [Int]
type Board = [Sequence]

toInt :: [Char] -> Int
toInt s = read s :: Int

toIntList :: [Char] -> Sequence
toIntList s = [ toInt [c] | c <- s ]

trimBoard :: Board -> Int -> Board
trimBoard board n
    |n==0 = [take 3 newBoard | newBoard <- board]
    |n==1 = [take 3(drop 3 newBoard) | newBoard <- board]
    |n==2 = [drop 6 newBoard | newBoard <- board]

getBox :: Board -> Int -> Int -> Sequence
getBox board x y = result
    where {result = concat (trimBoard (transpose (trimBoard board x)) y);}

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
    let result = getBox thing 1 1
    print result