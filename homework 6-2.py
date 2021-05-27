class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_of_asphalt(self):
        return f"{self._length} м * {self._width} м * 25 кг * 5 см = {(self._length * self._width * 25 * 5) / 1000} т"

road_1 = Road(100, 5)
print(road_1.weight_of_asphalt())
