# Initializing the Stack class
class Stack:
# Defining the attributes of the Stack Class
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

# Initializing a method to push (add) items into the stack
    def push(self, item):
        self.items.append(item)

# Initializing a method to extract items from the stack
    def pop(self):
        # Checks if there are items in the stack
        if len(self.items) == 0:
            return False
        else:
            return self.items.pop()

# Initializing a method to check if the stack is empty
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False


# Creating a class that reverses a string using the methods inherited from the Stack class
class StringReverse(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.items = []

# Initializing a method to print out the characters in the original string
    def original_string(self):
        print(f"Original String: {str(self.items)}")

# Initializing a method to reverse the string using the pop() method
    # This method is based on the amount of characters pushed into the stack
    def reverse_string(self):
        return print(f"Reversed String: {self.items.pop()}"
                     f"{self.items.pop()}{self.items.pop()}"
                     f"{self.items.pop()}{self.items.pop()}"
                     f"{self.items.pop()}")


# Main() driver
# Creating an instance for the StringReverse class
stack = StringReverse()

#Pushing the characters of the string into the stack
stack.push("M")
stack.push("a")
stack.push("r")
stack.push("v")
stack.push("i")
stack.push("n")

# Printing out the original string
stack.original_string()

# Printing out the reversed string
stack.reverse_string()

