import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_attributes(self):
        with self.assertRaises(TypeError) as err:
            Square('no', 7, 0)
        self.assertEqual(str(err.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as err:
            Square(7, 'no', 0)
        self.assertEqual(str(err.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as err:
            Square(7, 5, 'no')
        self.assertEqual(str(err.exception), 'y must be an integer')

        with self.assertRaises(ValueError) as err:
            Square(-7, 5, 0)
        self.assertEqual(str(err.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as err:
            Square(7, -5, 0)
        self.assertEqual(str(err.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as err:
            Square(7, 5, -1)
        self.assertEqual(str(err.exception), 'y must be >= 0')

        square = Square(8)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        square.x = 5
        self.assertEqual(square.x, 5)
        square.y = 7
        self.assertEqual(square.y, 7)
        square = Square(8, id=89)
        self.assertEqual(square.id, 89)

    def test_area(self):
        s = 8
        square = Square(s)
        self.assertEqual(square.area(), s * s)
        square = Square(s, 5, 7)
        self.assertEqual(square.area(), s * s)

    def test_update(self):
        square = Square(1)
        square.update(89, 8, 5, 7)
        attrs = {'id': 89, 'size': 8, 'x': 5, 'y': 7}
        self.assertEqual(square.to_dictionary(), attrs)

        square.update(90, 9, 6, 8, id=11, size=12, x=14, y=15)
        attrs = {'id': 90, 'size': 9, 'x': 6, 'y': 8}
        self.assertEqual(square.to_dictionary(), attrs)

        square.update(id= 11, size=12, x=14, y=15)
        attrs = {'id': 11, 'size': 12, 'x': 14, 'y': 15}
        self.assertEqual(square.to_dictionary(), attrs)

        square.update()
        self.assertEqual(square.to_dictionary(), attrs)

    def test_to_dictionary(self):
        attrs = {'id': 89, 'size': 8, 'x': 5, 'y': 7}
        square = Square(**attrs)
        self.assertEqual(square.to_dictionary(), attrs)

        attrs = {'id': 89, 'size': 8}
        square = Square(**attrs)
        attrs['x'] = 0
        attrs['y'] = 0
        self.assertEqual(square.to_dictionary(), attrs)

        attrs = {'size': 8}
        square = Square(**attrs)
        attrs['id'] = square.id
        attrs['x'] = 0
        attrs['y'] = 0
        self.assertEqual(square.to_dictionary(), attrs)

        attrs = dict()
        square = Square(8, 9, 5)
        attrs['id'] = square.id
        attrs['size'] = square.size
        attrs['x'] = square.x
        attrs['y'] = square.y
        self.assertEqual(square.to_dictionary(), attrs)

    def test_str(self):
        s = 8
        id = 89
        square = Square(s, id=id)
        self.assertEqual(str(square), f'[Square] ({id}) 0/0 - {s}')

        x, y = 5, 7
        square = Square(s, x, y, id=id)
        self.assertEqual(str(square), f'[Square] ({id}) {x}/{y} - {s}')

        square = Square(8, 5, 7)
        self.assertEqual(str(square), f'[Square] ({square.id}) {square.x}/{square.y} - {square.size}')

        square = Square(8, 5, 7, id=89)
        self.assertEqual(str(square), f'[Square] ({square.id}) {square.x}/{square.y} - {square.size}')
