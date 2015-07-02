input()
nums = [int(x) for x in input().split()]
nums.sort()
high_count = nums.count(nums[-1])
print(nums[-high_count -1])
