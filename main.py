import os

DIVIDER = "-" * 20

# display cart function: this function displays the current items in the cart
def display_cart(cart):
    print(DIVIDER)
    if not cart:
        print("Your cart is empty.")
    else:
        print("Current cart:")
        for idx, item in enumerate(cart, 1):
            print(f"{idx}. {item['name']} - Qty: {item['qty']} - Price: {item['price']} each")
    print(DIVIDER)

# display all carts function: this function displays all carts with their item counts
def display_all_carts(carts):
    print(DIVIDER)
    if not carts:
        print("No carts available.")
    else:
        print(f"You have {len(carts)} cart(s):")
        for idx, cart in enumerate(carts, 1):
            print(f"Cart {idx}: {len(cart)} item(s)")
    print(DIVIDER)

# modify cart function: this function allows adding or removing items from a specific cart
def modify_cart(cart):
    while True:
        os.system('cls')  # Clear terminal before each cart modification prompt
        display_cart(cart)
        print("Modify Cart Menu")
        print(DIVIDER)
        choice = input("Add item (a), Remove item (r), or Finish cart (f)? Choices: a/r/f: ").strip().lower()
        print(DIVIDER)
        if choice == 'a':
            item_name = input("Enter item name: ").strip()
            try:
                qty = int(input("How many qty? "))
                price = int(input("Price of item? "))
            except ValueError:
                print("Please enter valid numbers for quantity and price.")
                input("Press Enter to continue...")
                continue
            cart.append({'name': item_name, 'qty': qty, 'price': price})
        elif choice == 'r':
            if not cart:
                print("Cart is empty, nothing to remove.")
                input("Press Enter to continue...")
                continue
            display_cart(cart)
            try:
                idx = int(input("Enter item number to remove: ")) - 1
                if 0 <= idx < len(cart):
                    removed = cart.pop(idx)
                    print(f"Removed {removed['name']} from cart.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Please enter a valid number.")
            input("Press Enter to continue...")
        elif choice == 'f':
            print("Final cart:")
            display_cart(cart)
            input("Press Enter to return to main menu...")
            break
        else:
            print("Invalid option. Please choose a, r, or f.")
            input("Press Enter to continue...")

# show totals function: this function calculates and displays totals for all carts
def show_totals(carts):
    os.system('cls')
    print(DIVIDER)
    print("Cart Totals Summary")
    print(DIVIDER)
    if not carts:
        print("Bossing, wala ka pang cart.")
        print(DIVIDER)
        input("Press Enter to continue...")
        return

    total_all_carts = 0
    cart_totals = []
    for cart in carts:
        cart_total = sum(item['qty'] * item['price'] for item in cart)
        cart_totals.append(cart_total)
        total_all_carts += cart_total

    for idx, cart_total in enumerate(cart_totals, 1):
        avg = cart_total / len(carts[idx-1]) if carts[idx-1] else 0
        print(f"Cart {idx}: Total = {cart_total}, Average per item = {avg:.2f}")

    most_expensive = max(cart_totals) if cart_totals else 0
    if most_expensive > 0:
        most_expensive_idx = cart_totals.index(most_expensive) + 1
        print(DIVIDER)
        print(f"Most expensive cart: Cart {most_expensive_idx} with total price {most_expensive}")
    print(DIVIDER)
    print(f"Total price of all carts: {total_all_carts}")
    print(DIVIDER)
    input("Press Enter to continue...")

# main function: this function runs the main menu loop
def main():
    carts = []

    while True:
        os.system('cls')  # Clear terminal at the start of each main menu loop
        print(DIVIDER)
        print("Main Menu:")
        print(DIVIDER)
        print("1. Add cart")
        print("2. Remove cart")
        print("3. See list of carts")
        print("4. Modify a cart")
        print("5. Show total")
        print("6. Exit")
        print(DIVIDER)
        choice = input("Choose an option (1-6): ").strip()
        print(DIVIDER)

        if choice == '1':
            carts.append([])
            print(f"Added new cart. You now have {len(carts)} cart(s).")
            print(DIVIDER)
            input("Press Enter to continue...")
        elif choice == '2':
            if not carts:
                print("No carts to remove.")
                print(DIVIDER)
                input("Press Enter to continue...")
                continue
            display_all_carts(carts)
            try:
                idx = int(input("Enter cart number to remove: ")) - 1
                if 0 <= idx < len(carts):
                    carts.pop(idx)
                    print(f"Removed cart {idx + 1}.")
                else:
                    print("Invalid cart number.")
            except ValueError:
                print("Please enter a valid number.")
            print(DIVIDER)
            input("Press Enter to continue...")
        elif choice == '3':
            display_all_carts(carts)
            for idx, cart in enumerate(carts, 1):
                print(f"\nCart {idx}:")
                display_cart(cart)
            input("Press Enter to continue...")
        elif choice == '4':
            if not carts:
                print("No carts to modify.")
                print(DIVIDER)
                input("Press Enter to continue...")
                continue
            display_all_carts(carts)
            try:
                idx = int(input("Input which cart would you want to modify (number): ")) - 1
                if 0 <= idx < len(carts):
                    modify_cart(carts[idx])
                else:
                    print("Invalid cart number.")
            except ValueError:
                print("Please enter a valid number.")
            print(DIVIDER)
            input("Press Enter to continue...")
        elif choice == '5':
            show_totals(carts)
        elif choice == '6':
            print("Exiting the shopping cart system.")
            print(DIVIDER)
            break
        else:
            print("Invalid option. Please choose 1-6.")
            print(DIVIDER)
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()