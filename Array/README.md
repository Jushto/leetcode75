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

__4. Reverse Vowels of a String__
-given a string s, reverse only all the vowels and return it
-vowles are 'a','e', 'i', 'o', and 'u' in upper and lowercase more than once
-s = "hello" -output = 'holle'
-s = 'leetcode' -output = 'leotcede'

__5. Reverse Words in a String__
-given a string s, reverse the order of words
-a word is a sequenxe of non-space character
    -words in original string will be separated by at least one space
-Return a string of the words in reverse order concatenated by a single space
    -eliminate unnecessary white space

__6. Increasing Triplet Subsequence__
-given an integer arry nums
-return true if there exists a triple of indices (i< j< k) and nums[i] < nums[j]< nums[k]
-false otherwise
-nums = "[1,2,3,4,5] -true

__7. Product of Array Except Self__
-given an array nums, return an array answer such that answer[i] is equal fo product of all elements of nums except nums[i]
-must be in O(n) and not use division operator
-nums = [1,2,3,4] -ans = [24,12,8,6]

__8. String Compression__
-compress an array of characters chars
-compression algorithm:
    -begin with an empty string s
    -for each group of conecutive repeating characters in chars:
        -if group's length is 1, append the character to s
        -otherwise append character followerd by group length
            -split group lengths greater than 10 into multiple characters in chars
    -compressed string s should be stored in input character array
    -return new length of array
-only use constant extra space
-chars = ["a","a","b","b","c","c","c"] - output = 6 -chars = ["a","2","b","2","c","3"]
-chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"] - output = 4 -chars =["a","b","1","2"]
