def check_sign(number):
    # Write your code here
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
    
    pass

number = int(input("enter the num:"))
result = check_sign(number)
print(result)