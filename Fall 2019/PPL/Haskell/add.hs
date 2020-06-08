type Entry = (Person, Number)
type Person = String
type Number = Integer
type Phonebook = [Entry]

add :: Phonebook -> Entry -> Phonebook
add pb ent
    | elem ent pb = pb
    | otherwise = ent : pb

main = do
    let pb = [ ("Joe Hughes", 4371239212), ("Mary Owen", 2039183421), ("Patty Riley", 2012349283), ("Mark Flores", 3039343844) ]
    let pb2 = add pb ("New Guy", 111222121234)
    print (pb2)