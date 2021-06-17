nums = []

for num in range(0, 1001):
    if num % 2:
        nums.append(num**3)

count = 0
while count < 2:

    if count == 1:
        for i, num in enumerate(nums):
            nums[i] += 17

    summa = 0
    for num in nums:
        number = num
        num_sum = 0
        while num % 10 != 0:
            num_sum += num % 10
            num = num // 10

        if num_sum % 7 == 0:
            summa += number
    print(summa)
    count += 1