def reverseVowels(s:str)->str:
    s = list(s)
    len_s = len(s)
    vowels = ['a','e','i','o','u', 'A','E','I','O','U']
    i = 0
    j = len_s - 1
    
    while i < j:
        if s[i] in vowels:
            while j > i:
                if s[j] in vowels:
                    s[i],s[j] = s[j], s[i]
                    j -= 1
                    break
                j -= 1
        i += 1
    
    return ''.join(s)
    
print(reverseVowels('leetcode'))