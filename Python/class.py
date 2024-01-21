class model:
    def __init__(self, color, price, model):
        self.color = color
        self.price = price
        self.model = model

    def car(self):
        if self.model >= 2018:
            self.price += 30
            print(f"new price is {self.price}")
        else:
            self.price -= 10
            print(f"new price is {self.price}")


Bmw = model("red", 20, 2020)
ford = model("black", 40, 2017)
Bmw.car()
ford.car()
