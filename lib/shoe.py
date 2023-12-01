#!/usr/bin/env python3

class Shoe:
    pass
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
        self.condition = "New"

    def get_size(self):
        return self._size

    def set_size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    
    size = property(get_size, set_size)
