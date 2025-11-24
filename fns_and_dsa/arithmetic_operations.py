def perform_operations():
    num1 = float(input("enter a number"))
    num2 = float(input("enter a second number"))
    operation = input("choose an operation(add,subtract,divide or multiply)")
    answer = 0

    
    if operation == "devide" :
        if num1>= num2:
            answer = num1 / num2
            #print(answer)
        elif num1 > 0 or num2 > 0:
            answer = num2 / num1
            
        elif num1 == 0 or num2 == 0:
            answer = "Cannot devide by zero"
        #print(answer)
        else:
            answer = num2/num1
        #print(answer)

    elif operation == "add":
        answer = num1 + num2
        #print(answer)
    
    elif operation == "multiply" :
        answer = num1 * num2
        #print(answer)

    elif operation == "subtract":
        if num1 > num2:
            answer = num1 - num2
            #print(answer)
        else :
            answer = num2 - num1
            #print(answer)
    print( answer)
perform_operations()
    
