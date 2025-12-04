def safe_divide (numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
    
    except ValueError:
        return "Error: Both inputs must be numeric valuess"

    try:
        result = num / den
        return f"Result: {result}"
    
    except ZeroDivisionError:
        return f"Error : Cannot divide by zero"
    
    
    