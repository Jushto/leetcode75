__0. Merge Strings Alternately__
-input(word1:str, word2:str)
-output(mergedString: str)
-merge the two strings by adding letters in alternating order starting with word1.
-if string is longer than the other, append the additional letters onto the end of the merged string
-word1 = "abc" -word2 = "pqr" -mergedString = "apbqcr"
-word1 = "ab" -word2 = "pqrs" -mergedString = "apbqrs"

__1. GCD of Strings__
-two strings s and t
-t divides s if and only if s = t + t + ... + t
-input(str1, str2)
-output(x:str). The largest string that divides both str1 and str2
-str1 = "abcabc" -str2 = "abc" x = "abc"

__2. Kids with Greatest Number of Candies__
-input(candies: List, extraCandies: int)
-candies[i] represents number of candies ith kid has.
-extraCAndies representes extracandies you have
-return boolean list of length n where result[i] is true if candies[i] + extraCandies will be the greateast among all kids
-false otherwise

__3. Can Place Flowers__
-a long flobwerbed with some plots planted and others not planted
-flowers cannot be planted in adjacent plots
-lowerbed is rep. by an integer array consisting of 0s(empty)and 1s(planted)
-return boolean True if n new flowers can be planted in flowerbed without violating the rules
-flowerbed = [1,0,0,0,1] -n = 1 -output = True
-flowerbed = [1,0,0,0,1] -n = 2 -output = False