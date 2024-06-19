# a = 5
# b = 6
# a, b = b, a
# print(a, b)

# side = 5
# height = side*(3**0.5)
# square = 1/2*side*height
# perimetr = float(side*3)
# print("Высота: ", round(height, 1))
# print("Площадь: ", round(square, 1))
# print("Периметр: ", perimetr)

k = 3875
remaining_seconds = k % 3600
hour = k//3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print("hour = ", hour)
print("minutes = ", minutes)
print("seconds = ", seconds)
print(hour, ":", minutes, ":", seconds)