import numpy as np

houses = np.array([
    [50, 1],
    [70, 2],
    [90, 3],
    [120, 3],
    [150, 4]
])

prices = np.array([100, 140, 180, 230, 290])
d = np.array([])
new_house_area = 100
bedrooms = 3
current_distance = 0
current_iteration_distance = 0
for distance in range(5):
    current_distance = houses[distance, 0]
    current_bedroom = houses[distance, 1]
    current_iteration_distance = np.sqrt((new_house_area - current_distance) ** 2 + (bedrooms - current_bedroom) ** 2)
    d = np.append(d, current_iteration_distance)
d = np.round(d)
sorted_indexes = np.argsort(d)
smallest = prices[sorted_indexes[0]]
closest = prices[sorted_indexes[1]]

prediction = (smallest + closest) / 2

print(prediction)