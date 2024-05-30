def reverseWords(s: str) -> str:
    words = s.split()
    final_s = words[::-1]
    
    return ' '.join(final_s)
    
s = "the sky    is blue"
print(reverseWords(s))