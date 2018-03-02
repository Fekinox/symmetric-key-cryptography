import Data.Char(ord, chr)

range l r x = (l <= x) && (x <= r)

encode :: Char -> Int
decode :: Int -> Char
encode c | range 'a' 'z' c = ord c - 0x60
encode c | range 'A' 'Z' c = ord c - 0x40
encode _ = 27
decode n = chr $ fromIntegral (n+0x40)

encodeTwo (x:y:str) = ((encode x)*100 + encode y) : (encodeTwo str)
encodeTwo (x:ys) = [(encode x)*100 + 27]
encodeTwo [] = []

decodeTwo :: [Int] -> [Char]
decodeTwo = foldr (\lval ival -> let (l, r) = dcTwo lval in l:r:ival) ""
  where dcTwo n = let r = n `mod` 100; l = (n - r) `div` 100 in (decode l, decode r)
  
encrypt key modulus = map (\n -> (n+key) `mod` modulus)
decrypt key modulus = let inverse = modulus - key in encrypt inverse modulus

encodeAndEncrypt key modulus = encrypt key modulus . encodeTwo
decodeAndDecrypt key modulus = decodeTwo . decrypt key modulus

splitIntoBlocks bs string | string /= [] = let (left, right) = splitAt bs string in left:(splitIntoBlocks bs right)
splitIntoBlocks _ _ = []

encodeBlocks blocksize string
  | string == []  = []
  | otherwise = map encodeBlock (splitIntoBlocks blocksize string)
  where encodeBlock chars = sum $ zipWith (\c n -> (encode c)*(100^n)) (chars++(repeat '\0')) [blocksize-1,blocksize-2..0]
