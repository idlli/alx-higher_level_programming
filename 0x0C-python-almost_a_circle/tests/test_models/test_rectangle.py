import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_attributes(self):
        with self.assertRaises(TypeError) as err:
            Rectangle('no', 7, 0, 0)
        self.assertEqual(str(err.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as err:
            Rectangle(7, 'no', 0, 0)
        self.assertEqual(str(err.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as err:
            Rectangle(7, 5, 'no', 0)
        self.assertEqual(str(err.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as err:
            Rectangle(7, 5, 0, 'no')
        self.assertEqual(str(err.exception), 'y must be an integer')

        with self.assertRaises(ValueError) as err:
            Rectangle(-7, 5, 0, 0)
        self.assertEqual(str(err.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as err:
            Rectangle(7, -5, 0, 0)
        self.assertEqual(str(err.exception), 'height must be > 0')
        with self.assertRaises(ValueError) as err:
            Rectangle(7, 5, -1, 0)
        self.assertEqual(str(err.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as err:
            Rectangle(7, 5, 0, -1)
        self.assertEqual(str(err.exception), 'y must be >= 0')

        rect = Rectangle(8, 9)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 9)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        rect.x = 5
        self.assertEqual(rect.x, 5)
        rect.y = 7
        self.assertEqual(rect.y, 7)
        rect = Rectangle(8, 9, id=89)
        self.assertEqual(rect.id, 89)

    def test_area(self):
        w, h = 8, 9
        rect = Rectangle(w, h)
        self.assertEqual(rect.area(), w * h)
        rect = Rectangle(w, h, 5, 7)
        self.assertEqual(rect.area(), w * h)

    def test_update(self):
        rect = Rectangle(1, 1)
        rect.update(89, 8, 9, 5, 7)
        attrs = {'id': 89, 'width': 8, 'height': 9, 'x': 5, 'y': 7}
        self.assertEqual(rect.to_dictionary(), attrs)

        rect.update(90, 9, 10, 6, 8, id=11, width=12, height=13, x=14, y=15)
        attrs = {'id': 90, 'width': 9, 'height': 10, 'x': 6, 'y': 8}
        self.assertEqual(rect.to_dictionary(), attrs)

        rect.update(id= 11, width=12, height=13, x=14, y=15)
        attrs = {'id': 11, 'width': 12, 'height': 13, 'x': 14, 'y': 15}
        self.assertEqual(rect.to_dictionary(), attrs)

        rect.update()
        self.assertEqual(rect.to_dictionary(), attrs)

    def test_to_dictionary(self):
        attrs = {'id': 89, 'width': 8, 'height': 9, 'x': 5, 'y': 7}
        rect = Rectangle(**attrs)
        self.assertEqual(rect.to_dictionary(), attrs)

        attrs = {'id': 89, 'width': 8, 'height': 9}
        rect = Rectangle(**attrs)
        attrs['x'] = 0
        attrs['y'] = 0
        self.assertEqual(rect.to_dictionary(), attrs)

        attrs = {'width': 8, 'height': 9}
        rect = Rectangle(**attrs)
        attrs['id'] = rect.id
        attrs['x'] = 0
        attrs['y'] = 0
        self.assertEqual(rect.to_dictionary(), attrs)

        attrs = dict()
        rect = Rectangle(8, 9, 5, 7)
        attrs['id'] = rect.id
        attrs['width'] = rect.width
        attrs['height'] = rect.height
        attrs['x'] = rect.x
        attrs['y'] = rect.y
        self.assertEqual(rect.to_dictionary(), attrs)

    def test_str(self):
        w, h = 8, 9
        id = 89
        rect = Rectangle(w, h, id=id)
        self.assertEqual(str(rect), f'[Rectangle] ({id}) 0/0 - {w}/{h}')

        x, y = 5, 7
        rect = Rectangle(w, h, x, y, id=id)
        self.assertEqual(str(rect), f'[Rectangle] ({id}) {x}/{y} - {w}/{h}')

        rect = Rectangle(8, 9, 5, 7)
        self.assertEqual(str(rect), f'[Rectangle] ({rect.id}) {rect.x}/{rect.y} - {rect.width}/{rect.height}')

        rect = Rectangle(8, 9, 5, 7, id=89)
        self.assertEqual(str(rect), f'[Rectangle] ({rect.id}) {rect.x}/{rect.y} - {rect.width}/{rect.height}')
