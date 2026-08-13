def calculate(first_number, second_number, operator):
    # Write your code here
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        if second_number != 0:
            return first_number / second_number
        pass

first_number = int(input("enter first num:"))
second_number = int(input("enter second num:"))
operator = input("enter operator:").strip()

result = calculate(first_number, second_number, operator)
print(result)