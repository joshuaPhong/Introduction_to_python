a = 1
b = 2
# We'll explain the expression str(a) later in the course.
# For now: it is used to convert the variable "a" into a string.
print("a = " + str(a))

# Assign "greetings" to the variable using the assignment operator
greetings = "greetings"
print("greetings = " + str(greetings))
# Reassign anything to the variable here
greetings = b
print("greetings = " + str(greetings))
a = b = 2
print("a = " + str(a))
print("b = " + str(b))