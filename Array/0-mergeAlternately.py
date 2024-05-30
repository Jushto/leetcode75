def mergeAlternately(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    loop_len = min(len1, len2)
    mergedString = []
    i = 0
    
    while i < loop_len:
        mergedString.append(word1[i])
        mergedString.append(word2[i])
        i += 1
    
    if len1 > loop_len:
        mergedString.append(word1[i:])
    elif len2 > loop_len:
        mergedString.append(word2[i:])
        
    return ''.join(mergedString)

w1 = "abcd"
w2 = "pq"
print(mergeAlternately(w1,w2))
