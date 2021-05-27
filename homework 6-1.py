from time import sleep
class TrafficLight:
    __color = ""
    def running(self):
        while True:
            print('Красный')
            sleep(7)
            print('Желтый')
            sleep(2)
            print('Зеленый')
            sleep(7)
trafficlight = TrafficLight()
trafficlight.running()
