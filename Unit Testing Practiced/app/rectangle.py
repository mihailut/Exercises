class Rectangle:
    length = None
    width = None
    color = None

    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def describe(self):
        print(self.length)
        print(self.width)
        print(self.color)

    def area_rectangle(self):
        area = Rectangle.length * Rectangle.width
        return area

    def perimeter(self):
        perimeter = 2 * (Rectangle.length + Rectangle.width)
        return perimeter

    def change_color(self):
        Rectangle.color = 'green'