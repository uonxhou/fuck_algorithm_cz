from typing import List

nums = [2, 1, 12, 5, 100, 4, 17, 24, 3]


def quick_sort(nums: List, left: int, right: int) -> None:
    if right <= left:
        return

    pivot = nums[left]
    low = left
    high = right
    print(f"l:{left}, r:{right}")

    while left < right:
        print(right)
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]

        while left < right and nums[left] <= pivot:
            left += 1
        nums[left], nums[right] = nums[right], nums[left]

    quick_sort(nums, low, left - 1)
    quick_sort(nums, left + 1, high)


if __name__ == '__main__':
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
