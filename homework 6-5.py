class Stationary:

    def __init__(self, title="Запуск отрисовки"):
        self.title = title

    def draw(self):
        print(f'Начинаем рисовать. {self.title}')

class Pen(Stationary):
    def draw(self):
        print(f'Рисуем ручкой. {self.title}')

class Pencil(Stationary):
    def draw(self):
        print(f'Рисуем карандашем. {self.title}')

class Handle(Stationary):
    def draw(self):
        print(f'Рисуем маркером. {self.title}')

stat = Stationary()
stat.draw()

handle = Handle()
pen = Pen()
pencil = Pencil()

handle.draw()
pen.draw()
pencil.draw()
