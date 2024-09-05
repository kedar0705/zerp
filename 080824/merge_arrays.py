# nums1 = []
# nums2 = []

# len_num1 = int(input("Enter number of elements : "))
# len_num2 = n = int(input("Enter number of elements in array2 (n) : "))
# m = int(input("m = "))
#
# for i in range(0, len_num1):
#     ele = int(input("Elements of nums1: "))
#     nums1.append(ele)
#
# for j in range(0, len_num2):
#     ele = int(input("Elements of nums2: "))
#     nums2.append(ele)
#
# # x = list(filter(lambda a: a != 0, nums1))

def merge_sorted_array(nums1, m, nums2, n):
    del nums1[-n:]
    nums1 = nums1 + nums2

    if len(nums1) == m + n:
        return sorted(nums1)

    else:
        return "Condition not satisfied"


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

print(merge_sorted_array(nums1, m, nums2, n))