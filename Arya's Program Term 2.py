def menu():
    print("\n--- Welcome to Dash Drink ---")
    order_menu()


def order_menu():
    print("\n --- Order Type ---")
    order_type = [
    "1. Pickup",
    "2. Delivery"

    ]
    return_order = ["Pickup", "Delivery"]
    for order in order_type:
        print(order) 
    while True:
        try:
            choice_order_type = int(input("\nEnter your option:")) 
            if choice_order_type in [1, 2]:   
                break 
            else:
                print("Invalid choice Please enter a number between 1 or 2")    
        except ValueError:
            print("Invalid input Please enter a valid number")
    if choice_order_type == 1:
            print("Pickup is free and should be ready in 5-10 minites")
    elif choice_order_type == 2: 
            print("Delivery is $3.49 , Orders talke 5-10 minites after order")
    return return_order[choice_order_type - 1]


def size_menu():
    print("\n--- Drink Size ---")
    
    drink_size = [
    "1. Small - $5.00",
    "2. Medium- $6.50",
    "3. Large- $7.50",
  
    ]
    return_sizes = ["Small", "Medium", "Large"]
    for drink in drink_size:
        print(drink)
    while True: 
        try:
            drink_choice = int(input("Enter your Drink Size: ")) 
            if drink_choice in [1, 2, 3]:   
                break 
            else:
                print("Invalid choice Please enter a number between 1 and 3")    
        except ValueError:
            print("Invalid input Please enter a valid number")  
    return return_sizes[drink_choice - 1]


def drink_menu():
    print("\n--- Drinks Type ---")
    drink_type = [
    "1. Caffeinated Drinks",
    "2. Fruit Refreshers",
    "3. Cream-Based Refreshers"
    ]
    for drink in drink_type:
        print(drink)
    while True:
        try:
            drink_type_choice = int(input("Enter your Drink Type: "))
            if drink_type_choice in [1, 2, 3]:
                if drink_type_choice == 1:
                    selected_drink = caffeinated_menu()  
                elif drink_type_choice == 2:
                    selected_drink =  Fruit_menu()
                elif drink_type_choice == 3:
                    selected_drink =  cream_menu() 
       
                break
            else:
                print("Invalid choice Please enter a number between 1 and 3")  
        except ValueError:
            print("Invalid input Please enter a valid number")
    return selected_drink 



def caffeinated_menu():
    print("\n--- Caffeinated Drinks Menu ---")
    caff_drinks = [
        "1. Espresso",
        "2. Latte",
        "3. Flat White",
        "4. Mocha",
        "5. Tea"
    ]

    return_caff = ["Espresso", "Latte", "Flat White", "Mocha", "Tea"]
    for drink in caff_drinks:
        print(drink)
    while True:
        try:
            caffeinated_choice = int(input("Select your drink: "))
            if 1 <= caffeinated_choice <= 5:
                print(f"Adding drink {caffeinated_choice} to your order.")
                break
            else:
                print("Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return return_caff[caffeinated_choice - 1]


def Fruit_menu():
    print("\n--- Fruit Refreshers Drinks Menu ---")
    fruit_drinks = [
        "1. Strawberry Refreshers",
        "2. Watermellon Refreshers",
        "3. Mango Refreshers",
        "4. Lemonade Refreshers",
        "5. Blueberry Refreshers"
    ]
    return_fruit = ["Strawberry Refreshers", "Watermellon Refreshers", "Mango Refreshers", "Lemonade Refreshers", "Blueberry Refreshers"]
    for drink in fruit_drinks:
        print(drink)
    while True:
        try:
            fruit_choice = int(input("Select your drink: "))
            if 1 <= fruit_choice <= 5:
                print(f"Adding drink {fruit_choice} to your order.")
                break
            else:
                print("Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return return_fruit[fruit_choice - 1]

def cream_menu():
    print("\n--- Cream-based Drinks Menu ---")
    cream_drinks = [
        "1. Strawberry Frappuccino",
        "2. Caramel Frappuccino",
        "3. Vanilla Bean  Frappuccino",
        "4. Dragon Fruit Frappuccino",
        "5. Banana Frappuccino"
    ]
    return_cream = ["Strawberry Frappuccino", "Caramel Frappuccino", "Vanilla Bean Frappuccino", "Dragon Fruit Frappuccino", "Banana Frappuccino"]
    for drink in cream_drinks:
        print(drink)
    while True:
        try:
            cream_choice = int(input("Select your drink: "))
            if 1 <= cream_choice <= 5:
                print(f"Adding drink {cream_choice} to your order.")
                break
            else:
                print("Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        return return_cream[cream_choice - 1]


def toppings_menu():
    print("\n--- Toppings Drinks Menu ---")
    toppings = [
        "1. Whipped Cream",
        "2. Chocolate Drizzle ",
        "3. Caramel Drizzle",
        "4. Oreo's",
        "5. Sprinkles"
    ]
    return_toppings = ["Whipped Cream", "Chocolate Drizzle", "Caramel Drizzle", "Oreo's", "Sprinkles"]
    for top in toppings:
        print(top)
    while True:
        try:
            toppings_choice = int(input("Select Your toppings:"))
            if 1 <= toppings_choice <= 5:
                print(f"Adding {return_toppings[toppings_choice - 1]} to your Drink")
                break
            else:
                print("Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    return return_toppings[toppings_choice - 1]


def main():
    order_type = order_menu()
    size_choice = size_menu()
    drink_choice = drink_menu()
    topping_choice = toppings_menu()
    print(f"\nYour Order: {size_choice} {drink_choice} with {topping_choice}")
    print(f"Service: {order_type}")


main()