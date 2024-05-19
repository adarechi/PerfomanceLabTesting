#task2
import sys, math

def is_point_in_circle(point: list, center_of_circle: list, radius: float) -> int: # функция расчета положения точки относительно окружности
    from_center_to_point = math.sqrt((point[0] - center_of_circle[0]) ** 2 + (point[1] - center_of_circle[1]) ** 2)
    if from_center_to_point == radius:
        return 0 # точка лежит на окружности
    elif from_center_to_point < radius:
        return 1 # точка внутри окружности
    elif from_center_to_point > radius:
        return 2 # точка снаружи окружности

# парсинг file 1
f1 = open(sys.argv[1])
text1 = f1.read().split("\n")
center_of_circle = [float(num) for num in text1[0].split()]
radius = float(text1[1])


# парсинг file 2
f2 = open(sys.argv[2])
points = [pair.split() for pair in f2.read().split("\n")]
for point in points:
    point[0] = float(point[0])
    point[1] = float(point[1])

# расчет положения точек относительно окружности и вывод полученных результатов
for point in points:
    print(is_point_in_circle(point, center_of_circle, radius))
