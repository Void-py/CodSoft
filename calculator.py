
print("HELLO USER !!\nPLEASE ENTER AN OPERATION TO PROCEED : \n\t1.ADDITION\n\t2.SUBTRACTION\n\t3.MULTIPLICATION\n\t4.DIVSION\n\t5.EXPONENTIAL\n\t6.EXIT")
while True:
    op_ = int(input())
    if op_==1:
        int_1 = int(input("Enter the first number : "))
        int_2 = int(input("Enter the second number : "))
        print("SUM : ",int_1+int_2)
    elif op_==2:
        int_1 = int(input("Enter the first number : "))
        int_2 = int(input("Enter the second number : "))
        print("DIFFERENCE : ",int_1-int_2)
    elif op_==3:
        int_1 = int(input("Enter the first number : "))
        int_2 = int(input("Enter the second number : "))
        print("PRODUCT : ",int_1*int_2)
    elif op_==4:
        int_1 = int(input("Enter the first number : "))
        int_2 = int(input("Enter the second number : "))
        print("QUOTIENT : ",int_1/int_2)
    elif op_==5:
        int_1 = int(input("Enter the first number : "))
        int_2 = int(input("Enter the second number : "))
        print("VALUE : ",int_1**int_2)
    elif op_==6:
        print("THANK YOU")
        break
    else:
        print("PLEASE ENTER A VALID CHOICE")
    print("PLEASE ENTER AN OPERATION TO PROCEED : \n\t1.ADDITION\n\t2.SUBTRACTION\n\t3.MULTIPLICATION\n\t4.DIVSION\n\t5.EXPONENTIAL\n\t6.EXIT")



    
    
