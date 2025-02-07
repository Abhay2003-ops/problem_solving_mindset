# Global variable - This remains constant throughout the program
# combined the various programming concepts 
# use input() function to take user input
# the program will calculate the net salary of an employee after tax deduction
TAX_RATE = 0.10  # 10% tax deduction

# Function to calculate the net salary after tax deduction
def calculate_net_salary(base_salary, bonus):
    """
    This function calculates the net salary of an employee after adding 
    a performance bonus and deducting tax.
    
    Parameters:
        base_salary (float): The basic salary of the employee.
        bonus (float): Additional performance bonus received.

    Returns:
        float: Net salary after tax deduction.
    """
    gross_salary = base_salary + bonus  # Total salary before tax
    tax_deduction = gross_salary * TAX_RATE  # Tax to be deducted
    net_salary = gross_salary - tax_deduction  # Final salary after tax

    return net_salary  # Returning the calculated net salary

# Function to demonstrate local and global variable scope
def salary_increment():
    """
    This function demonstrates the use of local and global variables.
    It temporarily increases the TAX_RATE for calculation but does not affect the global value.
    """
    local_tax_rate = 0.15  # Local variable (only used inside this function)
    print("\nInside salary_increment function, temporary tax rate is:", local_tax_rate)

    # Note: Changing local_tax_rate here does NOT affect the global TAX_RATE variable.

# Function to calculate the percentage of bonus received
def bonus_percentage(base_salary, bonus):
    """
    This function calculates how much percentage of the base salary 
    is given as a performance bonus.
    
    Parameters:
        base_salary (float): The basic salary of the employee.
        bonus (float): The additional performance bonus.

    Returns:
        float: The percentage of the bonus in relation to the base salary.
    """
    if base_salary == 0:
        return 0.0  # Avoiding division by zero error
    bonus_percent = (bonus / base_salary) * 100  # Calculating bonus percentage
    return bonus_percent  # Returning the bonus percentage

# ---------------------------
# Taking User Input
# ---------------------------
try:
    # Taking user input for base salary and bonus
    base_salary = float(input("Enter your base salary: "))
    bonus = float(input("Enter your performance bonus: "))

    # Validating that salary and bonus are not negative
    if base_salary < 0 or bonus < 0:
        print("Salary and bonus cannot be negative. Please enter valid values.")
    else:
        # Calling function to calculate net salary
        net_salary = calculate_net_salary(base_salary, bonus)  
        print("\nNet salary after tax deduction:", net_salary)

        # Displaying the global tax rate
        print("\nGlobal TAX_RATE:", TAX_RATE)

        # Calling function to demonstrate local vs global variable scope
        salary_increment()

        # Calling function to calculate bonus percentage
        bonus_percent = bonus_percentage(base_salary, bonus)
        print(f"\nBonus Percentage of base salary: {bonus_percent:.2f}%")
except ValueError:
    print("Invalid input! Please enter numeric values for salary and bonus.")
