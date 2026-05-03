def order_menu():
    print("\n --- Order Type ---")
    order_type = [
        ["Pickup", 0.00],
        ["Delivery", 3.49]
]
    return_order = ["Pickup", "Delivery"]
    count = 1
    for order in order_type:
        print(f"{count}. {order[0]}")
        count += 1
    while True:
        try:
            choice_order_type = int(input("\nEnter your option:")) 
            if choice_order_type == 1:
                print("Pickup is free and should be ready in 5-10 minites")
                return return_order[0], order_type[0][1]
            elif choice_order_type == 2:
                print("Delivery is $3.49 , Orders talke 5-10 minites after order") 
                return return_order[1], order_type[1][1]
            else:
                print("Invalid choice Please enter a number between 1 or 2")    
        except ValueError:
            print("Invalid input Please enter a valid number")



def size_menu():
    print("\n--- Drink Size ---")
    
    drink_size = [
        ["Small", 5.00],
        ["Medium", 6.50],
        ["Large", 7.50]
  
    ]
    return_sizes = ["Small", "Medium", "Large"]
    count = 1
    for drink in drink_size:
        print(f"{count}. {drink[0]} - ${drink[1]:.2f}")
        count += 1
    while True: 
        try:
            drink_choice = int(input("Enter your Drink Size: ")) 
            if 1 <= drink_choice <= 3:   
                return return_sizes[drink_choice - 1], drink_size[drink_choice - 1][1]
             
            else:
                print("Invalid choice Please enter a number between 1 and 3")    
        except ValueError:
            print("Invalid input Please enter a valid number")  


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
       
                return selected_drink
            else:
                print("Invalid choice Please enter a number between 1 and 3")  
        except ValueError:
            print("Invalid input Please enter a valid number")
    

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
                print(f"Adding drink {return_caff[caffeinated_choice - 1]} to your order.")
                return return_caff[caffeinated_choice - 1]
            else:
                print("Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    

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
                print(f"Adding drink {return_fruit[fruit_choice - 1]} to your order.")
                return return_fruit[fruit_choice - 1]
            else:
                print("Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    

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
                print(f"Adding drink {return_cream[cream_choice - 1]} to your order.")
                return return_cream[cream_choice - 1]
            else:
                print("Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def toppings_menu():
    print("\n--- Toppings Drinks Menu ---")
    toppings = [
        ["Whipped Cream", 1.00],
        ["Chocolate Drizzle", 0.50],
        ["Caramel Drizzle", 0.50],
        ["Oreo's", 1.50],
        ["Sprinkles", 0.50]
    ]
    return_toppings = ["Whipped Cream", "Chocolate Drizzle", "Caramel Drizzle", "Oreo's", "Sprinkles"]
    count = 1 
    for top in toppings:
        print(f"{count}. {top[0]} - ${top[1]:.2f}")
        count += 1
       
    while True:
        try:
            toppings_choice = int(input("Select Your toppings:"))
            if 1 <= toppings_choice <= 5:
                print(f"Adding {return_toppings[toppings_choice - 1]} to your Drink")
                return return_toppings[toppings_choice - 1], toppings[toppings_choice - 1][1]

            else:
                print("Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        

def main():
    print("\n--- Welcome to Dash'n Drinks ---")
    order_type, delivery_fee = order_menu()
    size_choice, size_price = size_menu() 
    drink_choice = drink_menu()
    topping_choice, topping_price = toppings_menu()
    total = size_price + topping_price + delivery_fee
    print("\n--- Dash'n Drinks  ---")
    print("\n--- RECEIPT  ---")
    print("--------------------")
    print("\nYour Order;")
    print(f"\nService: {order_type}")
    print(f"\nSize:{size_choice} ")
    print(f"\nDrink:{drink_choice} ")
    print(f"\nToppings:{topping_choice} ")
    print("--------------------")
    print("\n--- PRICE --- ")
    print(f"\n {order_type}: ${delivery_fee:.2f} ")
    print(f"\n {size_choice}: ${size_price:.2f}  ")
    print(f"\n {topping_choice}: ${topping_price:.2f}  ")

    print(f"\nTotal Price: ${total:.2f}") 
    print("-------------------------")
    




  


main()