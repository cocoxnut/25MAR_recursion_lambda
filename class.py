num1 = int(input("Enter lenghth of the pool: "))
num2 = int(input("Enter width of the pool: "))
num3 = int(input("Enter depth of the pool: "))
multiply = lambda num1, num2, num3: num1 * num2 * num3
print("Volume of pool is", multiply(num1, num2, num3))