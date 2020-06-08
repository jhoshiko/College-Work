import System.Environment
import System.IO
import Data.List

type Sequence = [Int]
type Board = [Sequence]

chunkRows :: Board -> Int -> Board
chunkRows board x
    | x == 0 = board[0] ++ board[1] ++ board[2]
    | x == 1 = board[3] ++ board[4] ++ board[5]
    | x == 2 = board[6] ++ board[7] ++ board[8]

getBox :: Board -> Int -> Int -> Sequence
getBox board x y = box where
rows = chunkRows board x
newBoard = transpose rows
columns = chunkRows newBoard y
box = columns[0] ++ columns[1] ++ columns[2] 

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
    let board = [row0, row1, row2, row3, row4, row5, row6, row7, row8]
    let box = getBox board 1 1
    print box
	
	
	