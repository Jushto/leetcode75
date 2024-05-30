def kidsWithCandies(candies, extraCandies):
    max_n = max(candies)
    len_candies = len(candies)
    result = [False] * len_candies
    
    for i in range(len_candies):
        if (candies[i] + extraCandies) >= max_n:
            result[i] = True
    
    return(result)
    
can = [12,1,12]
extr = 10
print(kidsWithCandies(can, extr))