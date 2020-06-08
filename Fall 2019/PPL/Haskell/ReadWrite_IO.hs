import Data.List
import System.IO
import System.Environment


--returns number of arguments inputted in command line
main = do
    args <- getArgs
    putStr (“# args = “ ++ (show (length args)))


--reads a file
--main = do
    --fin <- openFile "Notes.txt" ReadMode
    --contents <- hGetContents fin
    --putStr contents
    --hClose fin

--writes a file
--main = do
    --let contents = ["Hello!", "My name is Krenko 2.0.", "Nice to meet you!"]
    --fout <- openFile "Notes.txt" WriteMode
    --hPutStr fout (unlines contents)
    --hClose fout
