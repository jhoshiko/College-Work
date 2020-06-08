data Suit = Spades | Hearts | Diamonds | Clubs
data Value = Two | Three | Four | Five | Six | Seven | Eight | Nine| Ten | Jack | Queen | King
data Card = Card Value Suit

main = do
    let card = Card Four Hearts
    print card
    {-|
        "print card" gives an error because it cannot convert card into string
        solution: use show 
    -}