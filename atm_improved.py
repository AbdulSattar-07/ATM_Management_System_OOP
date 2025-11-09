"""
Improved ATM Console Application
Features:
- Input validation
- Looping menu
- Better error handling
- Cleaner messages
"""

class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    
    def menu(self):
        """Main menu loop"""
        while True:
            print("\n" + "="*40)
            print("          ATM MENU")
            print("="*40)
            choice = input("""
    1 - Create PIN
    2 - Change PIN
    3 - Deposit
    4 - Withdraw
    5 - Check Balance
    6 - Exit
    
Enter your choice: """)
            
            if choice == "1":
                self.create_pin()
            elif choice == "2":
                self.change_pin()
            elif choice == "3":
                self.deposit()
            elif choice == "4":
                self.withdraw()
            elif choice == "5":
                self.check_balance()
            elif choice == "6":
                if self.exit():
                    break
            else:
                print("❌ Invalid option! Please try again.")
                
    def create_pin(self):
        """Create a new PIN with validation"""
        if self.pin:
            print("⚠️  PIN already exists. Use 'Change PIN' option instead.")
            return
        
        while True:
            new_pin = input("Enter your new PIN (4-6 digits): ")
            if not new_pin.isdigit():
                print("❌ PIN must contain only numbers.")
            elif len(new_pin) < 4 or len(new_pin) > 6:
                print("❌ PIN must be 4-6 digits long.")
            else:
                self.pin = new_pin
                print("✅ Your PIN has been created successfully!")
                break
    
    def change_pin(self):
        """Change existing PIN"""
        if not self.pin:
            print("⚠️  No PIN set. Please create a PIN first.")
            return
        
        old_pin = input("Enter your old PIN: ")
        if old_pin != self.pin:
            print("❌ Invalid old PIN.")
            return
        
        while True:
            new_pin = input("Enter your new PIN (4-6 digits): ")
            if not new_pin.isdigit():
                print("❌ PIN must contain only numbers.")
            elif len(new_pin) < 4 or len(new_pin) > 6:
                print("❌ PIN must be 4-6 digits long.")
            else:
                self.pin = new_pin
                print("✅ Your PIN has been changed successfully!")
                break
        
    def deposit(self):
        """Deposit money with validation"""
        if not self.pin:
            print("⚠️  No PIN set. Please create a PIN first.")
            return
        
        temp = input("Enter your PIN: ")
        if temp != self.pin:
            print("❌ Invalid PIN.")
            return
        
        try:
            amount = int(input("Enter amount to deposit: "))
            if amount <= 0:
                print("❌ Amount must be greater than 0.")
                return
            self.balance += amount
            print(f"✅ Amount {amount} deposited successfully!")
            print(f"💰 Current balance: {self.balance}")
        except ValueError:
            print("❌ Invalid amount. Please enter a number.")
               
    def withdraw(self):
        """Withdraw money with validation"""
        if not self.pin:
            print("⚠️  No PIN set. Please create a PIN first.")
            return
        
        temp = input("Enter your PIN: ")
        if temp != self.pin:
            print("❌ Invalid PIN.")
            return
        
        try:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("❌ Amount must be greater than 0.")
                return
            if amount > self.balance:
                print(f"❌ Insufficient funds. Available balance: {self.balance}")
                return
            self.balance -= amount
            print(f"✅ Amount {amount} withdrawn successfully!")
            print(f"💰 Current balance: {self.balance}")
        except ValueError:
            print("❌ Invalid amount. Please enter a number.")
    
    def check_balance(self):
        """Check current balance"""
        if not self.pin:
            print("⚠️  No PIN set. Please create a PIN first.")
            return
        
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            print(f"💰 Your available balance is: {self.balance}")
        else:
            print("❌ Invalid PIN.")
    
    def exit(self):
        """Exit the ATM"""
        if not self.pin:
            print("👋 Goodbye!")
            return True
        
        temp = input("Enter your PIN to exit: ")
        if temp == self.pin:
            print("👋 Thank you for using our ATM. Goodbye!")
            return True
        else:
            print("❌ Invalid PIN.")
            return False


if __name__ == "__main__":
    print("🏦 Welcome to the ATM!")
    atm = ATM()
