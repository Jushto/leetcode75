def compress(chars: str) -> int:
    i = j = 0
    n = len(chars)
    s = []
    
    i = 0
    while i < n:
        char = chars[i]
        j = i
        count = 0
        while j < n and char == chars[j]:
            count += 1
            j += 1
        
        s.append(char)
        i += count
        
        if count > 1:
            count = str(count)
            for d in count:
                s.append(d)
        
    n = len(s)
    for i in range(len(s)):
        chars[i] = s[i]
    
    return(n)
    
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))  
            
        