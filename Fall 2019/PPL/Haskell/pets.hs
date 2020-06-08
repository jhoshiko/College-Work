--creates type and sets parameters with genus and name
data Pet = Dog String | Cat String | Fish String | Saproling String

instance Show Pet where
    show (Dog name) =  name ++ "--" ++ "bork"
    show (Cat name) = name ++ "--" ++ "nya"
    show (Fish name) = name ++ "--" ++ "flopwop"
    show (Saproling name) = name ++ "--" ++ "Father, no.."

main = do
    let dog = Dog "name"
    let cat = Cat "name"
    let fish = Fish "name"
    let saproling = Saproling "stool"
    print saproling