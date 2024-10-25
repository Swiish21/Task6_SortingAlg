def find_kth_largest(nums, k):

    nums.sort(reverse=True)
 
    return nums[k-1]


nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print('The length of the list is:', len(nums), '\n')
k = int(input('Enter the value of k: '))
result = find_kth_largest(nums, k)
print('The ', k, 'th largest element is:', result, '\n') 