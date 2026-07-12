details = {
    "Name": "Deepika Barnikala",
    "ATM PIN": "4455",
    "Balance": 50000,
    "Transaction": []
}


def withdraw():
    amount = int(input("Enter amount to withdraw: "))
    if amount <= details["Balance"] and amount % 100 == 0:
        details["Balance"] -= amount
        details["Transaction"].append(f"Withdraw: {amount}")
        print(f"Successfully withdrawn ₹{amount}")
        print(f"Available Balance: ₹{details['Balance']}")
    else:
        print("Insufficient balance or enter amount in multiples of 100.")


def deposit():
    amount = int(input("Enter amount to deposit: "))
    if amount % 100 == 0:
        details["Balance"] += amount
        details["Transaction"].append(f"Deposit: {amount}")
        print(f"Successfully deposited ₹{amount}")
        print(f"Available Balance: ₹{details['Balance']}")
    else:
        print("Deposit amount should be in multiples of 100.")


def check_balance():
    print(f"\nAvailable Balance: ₹{details['Balance']}")
    details["Transaction"].append(f"Balance: {details['Balance']}")


def change_pin():
    attempts = 3

    while attempts > 0:
        old_pin = input("Enter old PIN: ")

        if old_pin == details["ATM PIN"]:
            new_pin = input("Enter new 4-digit PIN: ")

            if len(new_pin) != 4 or not new_pin.isdigit():
                print("PIN should contain exactly 4 digits.")
                return

            confirm_pin = input("Confirm new PIN: ")

            if new_pin == confirm_pin:
                details["ATM PIN"] = new_pin
                details["Transaction"].append(f"PIN Changed to: {new_pin}")
                print("PIN changed successfully.")
            else:
                print("PIN confirmation failed.")
            return

        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect old PIN. {attempts} attempts left.")
            else:
                print("PIN change failed.")


def transaction_history():
    print("\n------ Transaction History ------")

    if len(details["Transaction"]) == 0:
        print("No Transactions.")
    else:
        for i in details["Transaction"]:
            print(i)


def menu():
    while True:
        print("\n========== ATM MENU ==========")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Balance Enquiry")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            withdraw()

        elif choice == "2":
            deposit()

        elif choice == "3":
            check_balance()

        elif choice == "4":
            change_pin()

        elif choice == "5":
            transaction_history()

        elif choice == "6":
            print("\nThank you for using our ATM.")
            break

        else:
            print("Invalid Choice.")


def login():
    attempts = 3

    while attempts > 0:
        pin = input("\nEnter your 4-digit ATM PIN: ")

        if len(pin) != 4 or not pin.isdigit():
            print("Please enter exactly 4 digits.")
            continue

        if pin == details["ATM PIN"]:
            print(f"\nWelcome {details['Name']}!")
            menu()
            return

        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect PIN. {attempts} attempts left.")
            else:
                print("Your card is blocked. Please contact the bank.")


def main():
    print("===================================")
    print("        WELCOME TO ATM")
    print("===================================")

    login()


main()
