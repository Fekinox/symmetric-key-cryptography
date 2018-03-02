import Data.Char(ord, chr)

range l r x = (l <= x) && (x <= r)

encode :: Char -> Int
decode :: Int -> Char
encode c = ord c - if (range 'a' 'z' c) then 0x60 else if (range 'A' 'Z' c) then 0x40 else 0x0
decode n = chr $ fromIntegral (n+0x40)

encodeTwo (x:y:str) = ((encode x)*100 + encode y) : (encodeTwo str)
encodeTwo (x:ys) = [(encode x)*100 + 27]
encodeTwo [] = []

decodeTwo :: [Int] -> [Char]
decodeTwo = foldr (\lval ival -> let (l, r) = dcTwo lval in l:r:ival) ""
  where dcTwo n = let r = n `mod` 100; l = (n - r) `div` 100 in (decode l, decode r)
  
encrypt key modulus = map (\n -> (n+key) `mod` modulus)
decrypt key modulus = let inverse = modulus - key in encrypt inverse modulus
