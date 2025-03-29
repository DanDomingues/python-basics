#Ex 6.1
def write_chars():
    file_1 = open("file_1_write.txt", 'w')
    char:str
    while True:
        char = input("Input char to be added (0 to exit) ")
        if char == '0':
            break
        file_1.write(char)
    file_1.close()

    with open("file_1_write.txt", 'r') as file_2:
        print(file_2.read())

#Ex 6.2
file_name = input("Input file to be read ")
with open(f"{file_name}.txt") as file:
    content = file.read()
    vocals = ('a', 'e', 'i', 'o', 'u')
    v_count = len([c for c in content if c in vocals])
    c_count = len(content) - v_count
    print(f"Text in {file_name}.txt has {v_count} vocals and {c_count} consonants")

#Ex 6.3
with open(f"{file_name}.txt") as file:
    l_count = len([c for c in file.read() if c == '\n'])
    print(f"Text in {file_name}.txt has {l_count} lines")