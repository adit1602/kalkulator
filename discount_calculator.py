def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive whole number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def calculate_total(price, discount_rate, quantity):
    subtotal = price * quantity
    discount_amount = subtotal * (discount_rate / 100)
    total = subtotal - discount_amount
    return subtotal, discount_amount, total


def main():
    print("=== Discount Calculator ===")
    price = get_positive_float("Enter item price: ")
    discount_rate = get_positive_float("Enter discount rate (%): ")
    quantity = get_positive_int("Enter quantity: ")

    subtotal, discount_amount, total = calculate_total(price, discount_rate, quantity)

    print("\n--- Receipt ---")
    print(f"Unit price:      {price:.2f}")
    print(f"Quantity:        {quantity}")
    print(f"Subtotal:        {subtotal:.2f}")
    print(f"Discount ({discount_rate:.1f}%):  -{discount_amount:.2f}")
    print(f"Total price:     {total:.2f}")


if __name__ == "__main__":
    main()
