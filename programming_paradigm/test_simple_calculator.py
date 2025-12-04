import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.Test.Case):
    def setUp(self):
    self.calc = SimpleCalculator()

#addition tests
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(5,3),8)
    
    def test_add_negative_numbers(self):
         self.assertEqual(self.calc.add(-2,-4),-6)

    #subtraction tests
    def test_subtract_positive_numbers(self):
         self.assertEqual(self.calc.subtract(10,4),6)
    
    def test_subtract_negative_numbers(self):
          self.assertEqual(self.calc.subtract(-3,-7),-4)
    
    #multiplication tests
    def test_multiply_numbers(self):
          self.assertEqual(self.calc.multiply(4,5),20)
    
    def test_multiply_by_zero(self):
          self.assertEqual(self.calc.multiply(10,0),0)
    
    #division tests
    def test_divide_numbers(self):
          self.assertEqual(self.calc.devide(20,5),4)
    
    def test_devide_floats(self):
          self.assertEqual(self.calc.devide(7,2),3.5)
    
    def test_divide_by_zero(self):
          self.assertEqual(self.calc.devide(10,0))

if __name__=="__main__":
     unittest.main()

    


