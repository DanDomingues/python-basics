#Ex 2.1
v1 = int(input("Input value A "))
v2 = int(input("Input value B "))

if v1 > v2:
    print("A > B")
elif v1 < v2:
    print("B > A")
else:
    print("A == B")

#Ex2.2
if v1 > 0:
    print(f"Root of {v1} is {v1**2}")
else:
    print("A is either negative or zero")

#Ex2.3
if v2 % 2 == 0:
    print("B is even")
else:
    print("B is odd")