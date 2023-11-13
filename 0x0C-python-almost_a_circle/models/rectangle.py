#!/usr/bin/python3

"""Class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle:
        A rectangle class that inherites from Base class.

    Args:
        Base: The base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor.

        Args:
            id = Instances counter.
            width: Rectangle width.
            height: Rectangle height.
            x:
            y:
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Private attribute property."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Private attribute setter.

        Args:
            value: The attribute new value.

        Raises:
            TypeError: If the value is not int.
            ValueError: If the attribute is less than or equal zero.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Private attribute property."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Private attribute setter.

        Args:
            value: The attribute new value.

        Raises:
            TypeError: If the value is not int.
            ValueError: If the attribute is less than or equal zero.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Private attribute property."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Private attribute setter.

        Args:
            value: The attribute new value.

        Raises:
            TypeError: If the value is not int.
            ValueError: If the attribute is less than or equal zero.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Private attribute property."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Private attribute setter.

        Args:
            value: The attribute new value.

        Raises:
            TypeError: If the value is not int.
            ValueError: If the attribute is less than or equal zero.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Public class method that returns The area value of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Public class method that prints rectangle instance with #."""
        for i in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """Overriding __str__ method."""
        return f"""[Rectangle] ({self.id}) {self.x}/{self.y}\
        \b\b\b\b\b\b\b\b- {self.width}/{self.height}"""
