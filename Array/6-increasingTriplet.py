def increasingTriplet(nums: list[int])-> bool:
    smallest = float('inf')
    second_smallest = float('inf')
    
    for num in nums:
        if num <= smallest:
            smallest = num
        elif num <= second_smallest:
            second_smallest = num
        else:
            return True
    return False

num = [2,1,5,0,4,6]
print(increasingTriplet(num))