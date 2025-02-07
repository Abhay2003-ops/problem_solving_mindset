#created a basic function in python
#try to understand the basic concept of function in python
# Function definition
#understanding the function calling and how to pass the parameter in function
# Function without parameters - Simple greeting function
def greet():
    """This function prints a simple greeting message."""
    print("Hello! Welcome to the world of Python functions.")

# Function with a parameter - Personalized greeting
def personalized_greet(name):
    """This function prints a personalized greeting message."""
    print(f"Hello, {name}! Hope you’re having a great day.")

# Function demonstrating repeated tasks
def display_greetings():
    """This function calls the greet function multiple times to demonstrate reusability."""
    for _ in range(3):  # Calls greet function 3 times
        greet()

# Main Execution
if __name__ == "__main__":
    # Calling a simple function
    greet()
    
    # Calling a function multiple times using another function
    display_greetings()
    
    # Calling a function with different arguments
    personalized_greet("Abhay")
    personalized_greet("Aman")
