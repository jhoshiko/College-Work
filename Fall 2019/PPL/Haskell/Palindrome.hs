isPalindrome a
    | a == reverse a = True
    | otherwise = False

main = print(isPalindrome "SATOR AREPO TENET OPERA ROTAS")