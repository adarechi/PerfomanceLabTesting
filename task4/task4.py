#task4
import sys

# получение массива из аргументов консоли
f = open(sys.argv[1])
text = f.read().split("\n")
nums = [int(num) for num in text]

# получение минимального количества ходов
counter = 0
nums.sort()
mediana = nums[len(nums)//2]
for num in nums:
    if abs(mediana - num) != 0:
        counter += abs(mediana - num)

# вывод минимального количества ходов
print(counter)
