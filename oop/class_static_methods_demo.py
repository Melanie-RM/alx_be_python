class Calculator:
    calculation_type = "Arithmetic Operations"

    def add (a,b):
        return a + b

    def multiply(cls,a,b):
        print(f"Calcultion Type:{cls.calculation_type}")
        return a * b
    
if __name__ == "__main__":
    sum_result = Calculator.add(10,5)
    print(f"Sum:{sum_result}")

    product_result = Calculator.multiply(1,4,3)
    print(f"Product:{product_result}")