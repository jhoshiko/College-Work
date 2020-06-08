import System.IO

type Entry = (Person, Number)
type Person = String
type Number = Integer
type Phonebook = [Entry]

--add function
add pb ent
    |elem ent pb = pb
    |otherwise = ent : pb

--find function
find :: Phonebook -> Person -> [Number]
find pb prs = [ b | (prs, b) <- pb ]

--delete function
delete :: Phonebook -> Person -> Phonebook
delete pb prs = [ ent | ent <- pb, fst ent /= prs ]


main = do
    rawContents <- readFile "phonebook.txt"
    let rawContentsByLine  = lines rawContents
    let contents = [ splitOn "," content | content <- rawContentsByLine ]
    let pb = [ (content!!0 :: Person, read (content!!1) :: Int) | content <- contents ] 
    print pb
