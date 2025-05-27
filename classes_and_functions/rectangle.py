# Rectangle: width, height


class BeautifulRectangle:

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


while True:
    num_1 = int(input("Ingrese un número: "))
    num_2 = int(input("Ingrese un número: "))

    if num_1 == num_2:
        print("Eso no es un rectangulo :v")
    else:
        rect = BeautifulRectangle(num_1, num_2)
        print(rect.area())
        break
