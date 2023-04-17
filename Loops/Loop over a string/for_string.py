hello_world = "Hello, World!"

for character in hello_world:  # Print each character from hello_world
    print(character)

length = 0  # Initialize length variable

for character in hello_world:
    length += 1  # Add 1 to the length on each iteration to count the characters

print(len(hello_world) == length)
# convert / cast the integer to type string with the function str()
print(str(len(hello_world)) + " this is the length of the string")
