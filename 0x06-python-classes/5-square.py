#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    @property
    def size(self):
        """Get the size of the square.
        Returns: size (int) : The size of the square.
        """
        return self.__size

    @size.setter
    def set_size(self, value):
        """Set the size of the square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
        
    def area(self):
        """Return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size**2
    
    def my_print(self):
        if self.size == 0:
            print()
        else:
            for row in range(0, self.__size):
                for col in range(0, self.__size):
                    print('#', end="")
                print()
            
    
