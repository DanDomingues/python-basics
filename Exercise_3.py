
#Ex 3.1
start = 0
counter = 0
divider = 3
target = 5

print(f"Finding first {target} divisible numbers by {divider}")
while counter < target:
    start += 1
    if start % divider == 0:
        counter += 1
        print(f"{start} is divisible by {divider}")

#Ex 3.2
print("\n")
print("Starting countdown...")

start = 10
while start >= 0:
    print(start)
    start -= 1
print("End!")

#Ex 3.3
print("\n")
start = 0
target = 100_000
step = 1000

while start <= target:
    print(start)
    start += step
