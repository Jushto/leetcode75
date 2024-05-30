from math import gcd

def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    
    len1 = len(str1)
    len2 = len(str2)
    x = gcd(len1, len2)
    return(str1[:x])

st1 = "abcab"
st2 = 'abc'
print(gcdOfStrings(st1, st2))