# Stage 1
"""
print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")
"""

# Stage 2
"""
print("Write how many cups of coffee you will need:")
num_cups = int(input())
print("For", num_cups, "cups of coffee you will need:")
print(num_cups * 200, "ml of water")
print(num_cups * 50, "ml of milk")
print(num_cups * 15, "g of coffee beans")
"""

# Stage 3
"""
print("Write how many ml of water the coffee machine has:")
water = int(input())
print("Write how many ml of milk the coffee machine has:")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
coffee = int(input())
print("Write how many cups of coffee you will need:")
cups = int(input())

max_cups = min(water // 200, milk // 50, coffee // 15)

if cups == max_cups:
    print("Yes, I can make that amount of coffee ")
elif cups < max_cups:
    print("Yes, I can make that amount of coffee (and even", max_cups - cups, "more than that)")
elif cups > max_cups:
    print("No, I can make only", max_cups, "cups of coffee")
"""

# Stage 4
"""
# Defining actions
BUY = "buy"
FILL = "fill"
TAKE = "take"

# Initial state
water = 400
milk = 540
coffee = 120
cups = 9
money = 550

# Functions to print the current state & to carry out each action
def print_current_state():
    global water, milk, coffee, cups, money
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(coffee, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")

def buy_action():
    global water, milk, coffee, cups, money
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    choice = input()
    if choice == "1":
        water -= 250
        coffee -= 16
        cups -= 1
        money += 4
    elif choice == "2":
        water -= 350
        milk -= 75
        coffee -= 20
        cups -= 1
        money += 7
    elif choice == "3":
        water -= 200
        milk -= 100
        coffee -= 12
        cups -= 1
        money += 6

def fill_action():
    global water, milk, coffee, cups, money
    print("Write how many ml of water you want to add:")
    add_water = int(input())
    print("Write how many ml of milk you want to add:")
    add_milk = int(input())
    print("Write how many grams of coffee beans you want to add:")
    add_coffee = int(input())
    print("Write how many disposable coffee cups you want to add:")
    add_cups = int(input())
    water += add_water
    milk += add_milk
    coffee += add_coffee
    cups += add_cups

def take_action():
    global money
    print("I gave you $" + str(money))
    money = 0

# Main function
print_current_state()
print()
print("Write action (buy, fill, take):")
action = input()

if action == BUY:
    buy_action()
elif action == FILL:
    fill_action()
elif action == TAKE:
    take_action()

print()
print_current_state()
"""

# Stage 5
"""
# Defining actions
BUY = "buy"
FILL = "fill"
TAKE = "take"
REMAINING = "remaining"
EXIT = "exit"

# Initial state
water = 400
milk = 540
coffee = 120
cups = 9
money = 550

# Functions to print the current state & to carry out each action
def print_current_state():
    global water, milk, coffee, cups, money
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(coffee, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")

def buy_action():
    global water, milk, coffee, cups, money
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    choice = input()
    if choice == "1":
        if water < 250:
            print("Sorry, not enough water!")
        elif coffee < 16:
            print("Sorry, not enough coffee!")
        elif cups < 1:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 250
            coffee -= 16
            cups -= 1
            money += 4
    elif choice == "2":
        if water < 350:
            print("Sorry, not enough water!")
        elif milk < 75:
            print("Sorry, not enough milk!")
        elif coffee < 20:
            print("Sorry, not enough coffee!")
        elif cups < 1:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 350
            milk -= 75
            coffee -= 20
            cups -= 1
            money += 7
    elif choice == "3":
        if water < 200:
            print("Sorry, not enough water!")
        elif milk < 100:
            print("Sorry, not enough milk!")
        elif coffee < 12:
            print("Sorry, not enough coffee!")
        elif cups < 1:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 200
            milk -= 100
            coffee -= 12
            cups -= 1
            money += 6
    elif choice == "back":
        pass

def fill_action():
    global water, milk, coffee, cups, money
    print("Write how many ml of water you want to add:")
    add_water = int(input())
    print("Write how many ml of milk you want to add:")
    add_milk = int(input())
    print("Write how many grams of coffee beans you want to add:")
    add_coffee = int(input())
    print("Write how many disposable coffee cups you want to add:")
    add_cups = int(input())
    water += add_water
    milk += add_milk
    coffee += add_coffee
    cups += add_cups

def take_action():
    global money
    print("I gave you $" + str(money))
    money = 0


# Main function
while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    
    if action == EXIT:
        break
    elif action == BUY:
        buy_action()
    elif action == FILL:
        fill_action()
    elif action == TAKE:
        take_action()
    elif action == REMAINING:
        print_current_state()
"""

# Stage 6

# Action Strings
BUY = "buy"
FILL = "fill"
TAKE = "take"
REMAINING = "remaining"
EXIT = "exit"
BACK = "back"

# State Strings
MAIN_MENU = "main menu"
BUY_MENU = "buy menu"
ADDING_WATER = "adding water"
ADDING_MILK = "adding milk"
ADDING_COFFEE = "adding coffee"
ADDING_CUPS = "adding cups"
    
class CoffeeMachine():
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550
        self.state = MAIN_MENU
    
    def print_current_resources(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")
    
    def main_function(self, user_input):
        # MAIN_MENU state, options are BUY, FILL, TAKE, REMAINING, EXIT
        if self.state == MAIN_MENU:
            if user_input == BUY:
                self.state = BUY_MENU
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            elif user_input == FILL:
                self.state = ADDING_WATER
                print("Write how many ml of water you want to add:")
            elif user_input == TAKE:
                print(f"I gave you ${self.money}")
                self.money = 0
            elif user_input == REMAINING:
                self.print_current_resources()
                print("Write action (buy, fill, take, remaining, exit):")
            elif user_input == EXIT:
                pass
            else:
                print("Write action (buy, fill, take, remaining, exit):")
        # BUY_MENU state, options are 1, 2, 3, BACK
        elif self.state == BUY_MENU:
            if user_input == "1":
                if self.water < 250:
                    print("Sorry, not enough water!")
                elif self.coffee < 16:
                    print("Sorry, not enough coffee!")
                elif self.cups < 1:
                    print("Sorry, not enough cups!")
                else:
                    print("I have enough resources, making you a coffee!")
                    self.water -= 250
                    self.coffee -= 16
                    self.cups -= 1
                    self.money += 4
                self.state = MAIN_MENU
                print("Write action (buy, fill, take, remaining, exit):")
            elif user_input == "2":
                if self.water < 350:
                    print("Sorry, not enough water!")
                elif self.milk < 75:
                    print("Sorry, not enough milk!")
                elif self.coffee < 20:
                    print("Sorry, not enough coffee!")
                elif self.cups < 1:
                    print("Sorry, not enough cups!")
                else:
                    print("I have enough resources, making you a coffee!")
                    self.water -= 350
                    self.milk -= 75
                    self.coffee -= 20
                    self.cups -= 1
                    self.money += 7
                self.state = MAIN_MENU
                print("Write action (buy, fill, take, remaining, exit):")
            elif user_input == "3":
                if self.water < 200:
                    print("Sorry, not enough water!")
                elif self.milk < 100:
                    print("Sorry, not enough milk!")
                elif self.coffee < 12:
                    print("Sorry, not enough coffee!")
                elif self.cups < 1:
                    print("Sorry, not enough cups!")
                else:
                    print("I have enough resources, making you a coffee!")
                    self.water -= 200
                    self.milk -= 100
                    self.coffee -= 12
                    self.cups -= 1
                    self.money += 6
                self.state = MAIN_MENU
                print("Write action (buy, fill, take, remaining, exit):")
            elif user_input == BACK:
                self.state = MAIN_MENU
                print("Write action (buy, fill, take, remaining, exit):")
        # ADDING RESOURCES states
        elif self.state == ADDING_WATER:
            self.water += int(user_input)
            self.state = ADDING_MILK
            print("Write how many ml of milk you want to add:")
        elif self.state == ADDING_MILK:
            self.milk += int(user_input)
            self.state = ADDING_COFFEE
            print("Write how many grams of coffee beans you want to add:")
        elif self.state == ADDING_COFFEE:
            self.coffee += int(user_input)
            self.state = ADDING_CUPS
            print("Write how many disposable coffee cups you want to add:")
        elif self.state == ADDING_CUPS:
            self.cups += int(user_input)
            self.state = MAIN_MENU
            print("Write action (buy, fill, take, remaining, exit):")
        else:
            print("Unknown state")
    
    
# Main script

virtual_coffee_machine = CoffeeMachine()
print("Write action (buy, fill, take, remaining, exit):")

while True:
    user_input = input()
    if user_input == EXIT:
        break
    else:
        virtual_coffee_machine.main_function(user_input)
