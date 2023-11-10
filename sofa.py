class Sofa:
    def __init__(self, width, color, length, model, material, price):
        self.__width = width
        self.__color = color
        self.__length = length
        self.__model = model
        self.material = material
        self.price = price

    def get_width(self):
        return self.__width

    def get_color(self):
        return self.__color

    def get_length(self):
        return self.__length

    def get_model(self):
        return self.__model

    def __str__(self):
        return (f"Width: {self.get_width()}, Color: {self.get_color()}, Length: {self.get_length()}, "
                f"Model: {self.get_model()}, Material: {self.material}, Price: {self.price}")

    def __repr__(self):
        return (f"{self.get_width()}, {self.get_color()}, {self.get_length()}, {self.get_model()},"
                f" {self.material}, {self.price}")

    def __del__(self):
        print("good")
