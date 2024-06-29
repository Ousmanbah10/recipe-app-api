"""
Sample test
"""
from django.test import SimpleTestCase

from app import calc


class Calctest(SimpleTestCase):
    """Test the calc method"""
    
    def test_add_numbers(self):
        """test adding numbers"""
        res = calc.add(5, 6)
        
        self.assertEqual(res, 11)
    
    def test_subtract_numbers(self):
        """TEST Subtract numbers"""
        res = calc.subtract(10, 15)
        
        self.assertEqual(res, 5)
