def canPlaceFlowers(flowerbed: list[int], n:int)->bool:
    len_bed = len(flowerbed)
    count = 0
    
    if flowerbed[0] == 0:
        if len_bed == 1:
            flowerbed[0] = 1
            count += 1
        else:
            if flowerbed[1] == 0:
                flowerbed[0] = 1
                count += 1
    
    if flowerbed[-1] ==  0 and flowerbed[-2] == 0:
        flowerbed[-1] = 1
        count += 1
    
    i = 1
    while i < (len_bed - 1):
        if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
            flowerbed[i+1] = 1
            count += 1
        i += 1
            
    if count >= n:
        return True
    return False

flow = [1,0,0,0,1]
print(canPlaceFlowers(flow,1))