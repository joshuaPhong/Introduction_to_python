animals = ["elephant", "lion", "tiger", "giraffe"]  # Create a new list
print(animals)

animals += ["monkey", "dog"]  # Add two items to the list
print(animals)

animals.append("dino")  # Add one more item to the list using append() method
print(animals)
length = len(animals) - 1
animals[length] = "dinosaur"
print(animals)
print(len(animals))
