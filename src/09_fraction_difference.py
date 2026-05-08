num1 = int(input("Enter numerator of first fraction: "))
den1 = int(input("Enter denominator of first fraction: "))

num2 = int(input("Enter numerator of second fraction: "))
den2 = int(input("Enter denominator of second fraction: "))

result_num = (num1 * den2) - (num2 * den1)
result_den = den1 * den2

print("Result:", f"{result_num}/{result_den}")
