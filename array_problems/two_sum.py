def twoSum(nums, target):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [2,7,11,15]
target = 9
result = twoSum(nums, target)
print(result)
