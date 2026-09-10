class Coffee:
    def __init__(self):
        self.size = input("Enter the coffee size (Small, Medium, Large): ")

        price_input = input("Enter the price: ")
        try:
            price_input = float(price_input)
        except ValueError:
            price_input = 0.0
        self.price = price_input

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value not in ("Small", "Medium", "Large"):
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    def tip(self):
        print("This coffee is great, here's a tip!")
        self.price += 1