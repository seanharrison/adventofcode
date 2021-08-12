import System.IO

main =
    do
        values <- getInputValues
        let thePair = find2020pair values
        print thePair
        print (product thePair)

        let theTriple = find2020triple values
        print theTriple
        print (product theTriple)

getInputValues = 
    do
        inh <- openFile "input.txt" ReadMode
        inStr <- hGetContents inh
        let values = map strToInt (lines inStr)
        return values    

strToInt s = 
    read s :: Integer

find2020pair values =
    if 2020 - a `elem` (tail values)
        then [a, 2020 - a]
        else find2020pair (tail values)
    where a = head values

find2020triple values = 
    if not (null bc)
        then [a] ++ bc
        else find2020triple (tail values)
    where a = head values
          bc = find2020bc (tail values) a

find2020bc values a =
    if null values
        then []
        else if 2020 - a - b `elem` (tail values)
            then [b, 2020 - a - b]
            else find2020bc (tail values) a
    where b = head values