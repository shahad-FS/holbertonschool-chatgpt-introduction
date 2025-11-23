#!/usr/bin/env python3


class Checkbook:
    def __init__(self):
        """
        Function Description:
            Initializes a new Checkbook instance with a starting balance of $0.0.

        Parameters:
            None

        Returns:
            None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
            Adds the specified amount to the current account balance
            and displays the updated balance.

        Parameters:
            amount (float): The amount of money to deposit into the checkbook.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
            Attempts to withdraw a specified amount from the account.
            If the withdrawal exceeds the available balance, it notifies the user.

        Parameters:
            amount (float): The amount of money to withdraw from the checkbook.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function Description:
            Displays the current account balance.

        Parameters:
            None

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Function Description:
        Provides an interactive menu for the user to deposit, withdraw,
        check balance, or exit the Checkbook program. Includes error handling
        for invalid inputs to prevent program crashes.

    Parameters:
        None

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Exiting the Checkbook program. Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    print("Amount must be positive!")
                    continue
                cb.deposit(amount)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    print("Amount must be positive!")
                    continue
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

