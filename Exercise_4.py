
def append_sequence(length:int = 10):
    """
    Builds a linear int sequence with a determined length
    :parameter length:Outputted list's length
    :returns: Linear int list with the inputted length
    """
    col: list = []
    while len(col) < length:
        inputted_value = int(input(f"Please input value {len(col) + 1}/{length} "))
        col.append(inputted_value)
    print('\n')
    return col

def output_values(col:list):
    for val in col:
        print(val)
    print('\n')

#Ex 4.1
collection = append_sequence(6)
print("Outputting values...")
output_values(collection)

#Ex 4.2
collection = [1, 0, 5, -2, -5, 7]
summed_value : int = collection[0] + collection[1] + collection[5]
print(f"Array of elements [1, 0, 7] has sum of {summed_value}")
collection[5] = 100
print("Set element 5 to 100. Outputting elements...")
output_values(collection)

#Ex 4.3
collection = append_sequence()
print("Outputting even values...")
counter : int = 0
for value in collection:
    if value % 2 == 0:
        counter += 1
print(f"Found {counter} even values")
