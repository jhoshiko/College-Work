import System.Environment
import System.IO
import Data.List

type Sequence = [Int]
type Board = [Sequence]

toInt :: [Char] -> Int
toInt s = read s :: Int

toIntList :: [Char] -> Sequence
toIntList s = [ toInt [c] | c <- s ]

getBoard :: [[Char]] -> Board
getBoard stringArray = result
    where {result = map toIntList stringArray; }

main = do
    --let row0 = "530070000"
    --let row1 = "600195000"
    --let row2 = "098000060"
    --let row3 = "800060003"
    --let row4 = "400803001"
    --let row5 = "700020006"
    --let row6 = "060000280"
    --let row7 = "000419005"
    --let row8 = "000080079"
    --let thing = [row0, row1, row2, row3, row4, row5, row6, row7, row8]
    --let thing = getBoard thing
    print "hello"