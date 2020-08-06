'''
Add up and print the sum of the all of the minimum elements of each inner array:
[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

The expected output is given by:
4 + -1 + 9 + -56 + 201 + 18 = 175
'''

# loop thru array
# check which is min value & add
# return the sum

nums = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]


def sum_min(array):
    sum = 0

    for min_value in nums:
        sum += min(min_value)
    return sum


print(sum_min(nums))
