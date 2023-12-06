def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    p1 = m - 1
    p2 = n - 1
    sert_index = m + n - 1

    while p1 >= 0 or p2 >= 0:

        if nums1[p1] >= nums2[p2]:
            nums1[sert_index] = nums1[p1]
            sert_index -= 1
            p1 -= 1
        elif nums1[p1] < nums2[p2]:
            nums1[sert_index] = nums2[p2]
            sert_index -= 1
            p2 -= 1

    return nums1


if __name__ == '__main__':
    ret = merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    print(ret)
