num = int(input("Enter a number: "))
square = num * num
if square % (10**len(str(num))) == num:
    print(num, "is an automorphic number.")
else:
    print(num, "is not an automorphic number.")
