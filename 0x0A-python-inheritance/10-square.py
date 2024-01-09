#!/usr/bin/python3
'''Will contains 10-square.py'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A representation of a square'''
    def __init__(self, size):
        '''Instantiation of the square'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Returns the area'''
        return self.__size ** 2
