import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    
    def test_id(self):
        base = Base()
        self.assertEqual(base.id, 1)
        base = Base()
        self.assertEqual(base.id, 2)
        base = Base(89)
        self.assertEqual(base.id, 89)
