# # Ex. 2


# from abc import ABC, abstractmethod
#
#
# class geometric_shape(ABC):
#     PI = 3.14
#
#     @abstractmethod
#     def area(self):
#         raise NotImplementedError
#
#     def describe(self):
#         print('I most probably have corners.')
#
#
# class square(geometric_shape):
#
#     def __init__(self, side):
#         self.__side = side
#
#     @property
#     def side(self):
#         return self.__side
#
#     @side.getter
#     def side(self):
#         return self.__side
#
#     @side.setter
#     def side(self, side):
#         print(f'This is new side to square {side}')
#         self.__side = side
#
#     @side.deleter
#     def side(self):
#         print(f'I deleted the side of square.')
#         self.__side = None
#
#     def area(self, area_of_square=None):
#         area_of_square = self.__side * self.__side
#         print(f'The area of square is {area_of_square}')
#
#
# class circle(geometric_shape):
#
#     def __init__(self, ray):
#         self.__ray = ray
#
#     @property
#     def ray(self):
#         return self.__ray
#
#     @ray.getter
#     def ray(self):
#         return self.__ray
#
#     @ray.setter
#     def ray(self, ray):
#         print(f'This is new side to square {ray}')
#         self.__ray = ray
#
#     @ray.deleter
#     def ray(self):
#         print(f'I deleted the ray of circle.')
#         self.__ray = None
#
#     def area(self, are_of_circle=None):
#         are_of_circle = self.PI * (self.__ray * self.__ray)
#         print(f'The area of circle is {are_of_circle}.')
#
#
# def describe():
#     print(f'I don t have corners.')
#
#
# square = square(12)
# square.describe()
# square.area()
# describe()
# square.side = 35
# square.area()
# del square.side
#
# circle = circle(10)
# circle.describe()
# circle.area()
# circle.ray = 2
# describe()
# circle.area()
# del circle.ray