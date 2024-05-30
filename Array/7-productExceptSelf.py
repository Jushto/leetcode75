def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    postfix = [1] * n
    prefix = [1] * n
    ans = [1] * n
    product = 1
    
    for i in range(1, n):
        product *= nums[i - 1]
        prefix[i] = product
    print(prefix)
    
    product = 1
    for i in range(n - 1, -1, -1):
        product *= nums[i]
        postfix[i] = product
    postfix.append(1)
    print(postfix)
    
    for i in range(n):
        product = prefix[i] * postfix[i+1]
        ans[i] = product
    return ans

num = [1,2,3,4]
print(productExceptSelf(num))