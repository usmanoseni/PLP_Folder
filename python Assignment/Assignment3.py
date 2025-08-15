# code  that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters.

# User define function
def calculate_discount(price, discount_percent):
    holder = price - (price * (discount_percent / 100))
    return holder


# code that prompt and accepts user input for the original price and discount percentage, then calls the function to calculate and print the final price.
print("welcome User, please enter the original price and discount percentage to calculate the final price after discount.")
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function to calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price after discount
print(f"The final price after a discount of {discount_percent}% on the original price of ${price} is: ${final_price}")
