from datetime import date
import os

class Budget:
    
    def __init__(self, total_spending, savings):
        # Total_spending is the amount of money I can assign to other budgets.
        self.total_spending = total_spending
        # Savings would be the remaining unspent money.
        self.savings = savings

    # Increase budget spending
    def increase(self, amount):
        self.total_spending += amount

    # Budget's information
    def __str__(self) -> str:
        return f'Total budget: {self.total_spending}\nAvailable savings: {self.savings}'

    def transfer(self, catg, name):
        amount = float(input("Money to transfer: "))
        while self.total_spending - amount < 0:
            amount = float(input(f"Insuficient funds. Current funds: {self.total_spending}\nMoney to transfer: "))
        self.total_spending -= amount
        catg.total_spending += amount
        print("\nUpdated funds")
        print(f"Budget funds: {self.total_spending}")
        print(f"{name} funds: {catg.total_spending}")
        day = str(date.today().strftime("%d %b, %Y"))
        with open('transactions.txt', 'a') as f:
            f.write(f"{day}\t Budget \t {name} \t {amount}\n")
            

class Groceries(Budget):
    def __init__(self, total_spending, savings):
        super().__init__(total_spending, savings)
        pass


def transactions():
    with open('transactions.txt', 'r') as f:
        line = f.readline()
        print(line)
        while line:
            line = f.readline()
            print(line)


b = Budget(1000, 10)
g = Groceries(0, 0)

# Main Loop

option = 1
clear = lambda: os.system('cls')

while option != 0:
    print()
    print("╔═════════════════════════╗")
    print("║        Main Menu        ║")
    print("╚═════════════════════════╝\n")
    print(f"1. Check Budget")
    print(f"2. Transfer Money")
    print(f"3. Check Transaction History")
    print(f"4. Increase Budget Spending")
    print(f"5. Create New Budget")
    print(f"0. Exit")
    
    option = int(input("\nEnter your choice: "))

    match option:
        case 1:
            clear()
            print(b.__str__())
        case 2:
            clear()
            print("Select the category to transfer the money to.")
            print("(G)roceries")
            cat = input().upper()
            match cat:
                case 'G':
                    b.transfer(g, "Groceries")
        case 3:
            clear()
            transactions()
        case 4:
            clear()
            increase_amount = float(input("Charge money: $"))
            b.increase(increase_amount)
        case 0:
            print("See ya!")
    
