def bubble_sort(nums):
    is_sorted = False
    sort_counter = 0

    while not is_sorted:
        is_sorted = True
        for j in range(1, len(nums) - sort_counter):
            i = j - 1
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                is_sorted = False

        sort_counter += 1

numbers = list(map(int, input().split()))
bubble_sort(numbers)
print(*numbers)