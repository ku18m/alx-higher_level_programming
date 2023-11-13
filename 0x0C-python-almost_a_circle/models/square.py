#!/usr/bin/python3

"""Class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square:
        A Square class that inherites from Rectangle class.

    Args:
        Rectangle: The base class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor.

        Args:
            id = Instances counter.
            size: Square size.
            x: Rectangle Vertical position.
            y: Rectangle Horizontal position.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overriding __str__ method."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.height)

    @property
    def size(self):
        """Private attribute property."""
        return self.height

    @size.setter
    def size(self, value):
        """
        Private attribute setter.

        Args:
            value: The attribute new value.

        Raises:
            TypeError: If the value is not int.
            ValueError: If the attribute is less than or equal zero.
        """
        self.width = value
        self.height = value
