
#Ex 1
print("Please input your name")
name = input()

print("Please input your age")
age = input()
age = int(age)

#print('Hello %s (%s)' % (name, age))
print(f"Hello {name} ({age})")

#Ex 2 and 3
print("\n")
v1 = int(input("Please input value 1 "))
v2 = int(input("Please input value 2 "))
v3 = int(input("Please input value 3 "))

print("\n")
print(f"sum is {v1 + v2 + v3}")
print(f"quad sum is {(v1**2)+(v2**2)+(v3**2)} ({v1**2} + {v2**2} + {v3**2})")