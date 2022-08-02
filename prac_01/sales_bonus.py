"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

LESSER_BONUS = 0.1
GREATER_BONUS = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        print(f"User's bonus is {sales * LESSER_BONUS:.2f}")
    else:
        print(f"User's bonus is {sales * GREATER_BONUS:.2f}")
    sales = float(input("Enter sales: $"))
