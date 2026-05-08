salary = float(input("Enter annual salary: "))

if salary > 12000:
    tax = (salary - 12000) * 0.15
    print("Result:", tax)
else:
    print("No taxes to pay.")
    