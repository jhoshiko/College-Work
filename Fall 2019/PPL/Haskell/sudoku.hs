-- CS3210 - Principles of Programming Languages - Fall 2019
-- Programming Assignment 02 - A Sudoku Solver
-- Author(s): WRITE YOUR NAME(S) HERE
-- Date:

import System.Environment
import System.IO
import Data.List

type Sequence = [Int]
type Board    = [Sequence]
enumerate = zip [0..9]

-- ***** HELPER FUNCTIONS *****

toInt :: [Char] -> Int
toInt s = read s :: Int

toIntList :: [Char] -> Sequence
toIntList s = [ toInt [c] | c <- s ]

sameLength :: [Int] -> Int
sameLength lengthList
    | all (==head lengthList)lengthList = head lengthList
    | otherwise = 0

trimBoard :: Board -> Int -> Board
trimBoard board n
    |n==0 = [take 3 newBoard | newBoard <- board]
    |n==1 = [take 3(drop 3 newBoard) | newBoard <- board]
    |n==2 = [drop 6 newBoard | newBoard <- board]

makeBoxList :: Board -> Board
makeBoxList board = result
    where {result = [(getBox board 0 0), (getBox board 0 1), 
        (getBox board 0 2), (getBox board 1 0), (getBox board 1 1), 
        (getBox board 1 2), (getBox board 2 0), (getBox board 2 1), (getBox board 2 2)];}

getRow :: Board -> Int -> Sequence
getRow board row = board!!row

-- ***** GETTER FUNCTIONS *****

-- TODO #1
getBoard :: [[Char]] -> Board
getBoard stringArray = result
    where {result = map toIntList stringArray; }

-- TODO #2
getNRows :: Board -> Int 
getNRows board = result
    where {result = length board; }

-- TODO #3
getNCols :: Board -> Int
getNCols board = result
    where {result = sameLength [length rowSizes | rowSizes <- board]}

-- TODO #4
getBox :: Board -> Int -> Int -> Sequence
getBox board x y = result
    where {result = concat (trimBoard (transpose (trimBoard board x)) y);}

-- TODO #5
getEmptySpot :: Board -> (Int, Int)
getEmptySpot board = result
    where {result = head [ (x, y) | (x, row) <- enumerate board
                     , (y, value) <- enumerate row
                     , value == 0]}

-- ***** PREDICATE FUNCTIONS *****

-- TODO #6
isGridValid :: Board -> Bool
isGridValid board = numRow && numColumn where
    numRow = getNRows board == 9
    numColumn = getNCols board == 9

-- TODO #7
isSequenceValid :: Sequence -> Bool
isSequenceValid sequence = result
    where{ result = filter (/=0) sequence == nub (filter (/=0) sequence); }

-- TODO #8
areRowsValid :: Board -> Bool
areRowsValid board
    | [True] == nub (map isSequenceValid board) = True
    | otherwise = False

-- TODO #9
areColsValid :: Board -> Bool
areColsValid board
    | [True] == nub (map isSequenceValid (transpose board)) = True
    | otherwise = False

-- TODO #10
areBoxesValid :: Board -> Bool
areBoxesValid board 
    | [True] == nub (map isSequenceValid (makeBoxList board)) = True
    | otherwise = False

-- TODO #11
isValid :: Board -> Bool
isValid board = result
    where{result = ((isGridValid board) && (areRowsValid board) && (areColsValid board) && (areBoxesValid board))}

-- TODO #12
isCompleted :: Board -> Bool
isCompleted board
    | [True] == nub (map (elem 0) board) = False
    | otherwise = True

-- TODO #13
isSolved :: Board -> Bool
isSolved board
    | and [isCompleted board, isValid board] = True
    | otherwise = False

-- ***** SETTER FUNCTIONS *****

-- TODO #14
setRowAt :: Sequence -> Int -> Int -> Sequence
setRowAt set index newValue
    | 0 /= set!!index = set
    | otherwise = result
        where
        leftSide = take (index) set
        rightSide = drop(index+1) set
        left = leftSide ++ [newValue]
        result = left ++ rightSide

-- TODO #15
setBoardAt :: Board -> Int -> Int -> Int -> Board
setBoardAt board row column value = newBoard where
    top = take(row) board
    bottom = drop(row+1) board
    set = getRow board row
    newRow = setRowAt set column value
    newBoard = top ++ [newRow] ++ bottom


-- TODO #16
-- name: buildChoices
-- description: given a board and a two indexes i and j (representing coordinates), generate ALL possible boards, replacing the cell at (i, j) with ALL possible digits from 1 to 9; OK to assume that the cell at (i, j) is empty
-- input: a board and two indexes (i, j)
-- output: a list of boards from the original board
-- example: buildChoices
-- [ [5,3,0,0,7,0,0,0,0],
--   [6,0,0,1,9,5,0,0,0],
--   [0,9,8,0,0,0,0,6,0],
--   [8,0,0,0,6,0,0,0,3],
--   [4,0,0,8,0,3,0,0,1],
--   [7,0,0,0,2,0,0,0,6],
--   [0,6,0,0,0,0,2,8,0],
--   [0,0,0,4,1,9,0,0,5],
--   [0,0,0,0,8,0,0,7,9] ] 0 2 yields
-- [
-- [ [5,3,1,0,7,0,0,0,0],
--   [6,0,0,1,9,5,0,0,0],
--   [0,9,8,0,0,0,0,6,0],
--   [8,0,0,0,6,0,0,0,3],
--   [4,0,0,8,0,3,0,0,1],
--   [7,0,0,0,2,0,0,0,6],
--   [0,6,0,0,0,0,2,8,0],
--   [0,0,0,4,1,9,0,0,5],
--   [0,0,0,0,8,0,0,7,9] ],
-- [ [5,3,2,0,7,0,0,0,0],
--   [6,0,0,1,9,5,0,0,0],
--   [0,9,8,0,0,0,0,6,0],
--   [8,0,0,0,6,0,0,0,3],
--   [4,0,0,8,0,3,0,0,1],
--   [7,0,0,0,2,0,0,0,6],
--   [0,6,0,0,0,0,2,8,0],
--   [0,0,0,4,1,9,0,0,5],
--   [0,0,0,0,8,0,0,7,9] ],
-- ...
-- [ [5,3,9,0,7,0,0,0,0],
--   [6,0,0,1,9,5,0,0,0],
--   [0,9,8,0,0,0,0,6,0],
--   [8,0,0,0,6,0,0,0,3],
--   [4,0,0,8,0,3,0,0,1],
--   [7,0,0,0,2,0,0,0,6],
--   [0,6,0,0,0,0,2,8,0],
--   [0,0,0,4,1,9,0,0,5],
--   [0,0,0,0,8,0,0,7,9] ]
-- ]
-- hint: use list comprehension and the function setBoardAt
-- buildChoices :: Board -> Int -> Int -> [Board]

-- solve :: Board -> [Board]
-- solve board
--   | isSolved board = [board]
--   | isCompleted board = [[[]]]
--   | not (isValid board) = [[[]]]
--   | otherwise = concat [ solve choice | choice <- buildChoices board i j ]
--     where
--       emptySpot = getEmptySpot board
--       i = fst emptySpot
--       j = snd emptySpot

-- program starts here
main = do

  -- TODO #17: validate the command-line and get the file name containing the board
    fileName <- getArgs
  -- TODO #18: read the contents of the board file into a string
    boardContents <- readFile filename
    let boardContentsByRow = lines boardContents
  -- TODO #19: create a board from the string board (hint: use getBoard)
    let board = getBoard boardContents
  -- TODO #20: use solve to find the solutions, disconsidering the ones that are [[]]
    let solvedBoard = solve board
  -- TODO #21: print the solutions found

  print "Done!"
