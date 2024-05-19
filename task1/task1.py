#task1
import sys

def move(arr: list, shift: int) -> list: # функция "смещения" массива
    new_arr = []
    shift -= len(arr)
    if shift < 0:
        shift *= -1

    for i in range(len(arr)):
        index = (i + shift) % len(arr)
        new_arr.append(arr[index])
    return new_arr

# ввод и инициализация
n, m = sys.argv[1].split()
n = int(n)
m = int(m)
arr = []
for i in range(1, n+1):
    arr.append(i)

# рассчет пути
first_element = arr[0]
road = [first_element]
while(True):
    for i in range(m):
        current_element = arr[i]
        if i == m - 1 and arr[i] != first_element:
            road.append(current_element)
    if current_element == first_element:
        break
    arr = move(arr, -m + 1)

# вывод пути
print(*road, sep="")
