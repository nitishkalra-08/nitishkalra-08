import json
import datetime

class PersonalFinanceTracker:
    def __init__(self):
        self.transactions = []
        self.categories = set()

    def add_transaction(self, amount, category, description=""):
        transaction = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.transactions.append(transaction)
        self.categories.add(category)
        print(f"Transaction added: {transaction}")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions found.")
            return

        print("\nAll Transactions:")
        for i, transaction in enumerate(self.transactions, start=1):
            print(f"{i}. Amount: {transaction['amount']}, Category: {transaction['category']}, Description: {transaction['description']}, Date: {transaction['date']}")

    def calculate_total_spending(self):
        total = sum(t["amount"] for t in self.transactions if t["amount"] < 0)
        print(f"Total spending: {abs(total)}")
        return total

    def calculate_total_income(self):
        total = sum(t["amount"] for t in self.transactions if t["amount"] > 0)
        print(f"Total income: {total}")
        return total

    def save_to_file(self, filename="finance_data.json"):
        with open(filename, "w") as file:
            json.dump(self.transactions, file, indent=4)
        print(f"Data saved to {filename}")

    def load_from_file(self, filename="finance_data.json"):
        try:
            with open(filename, "r") as file:
                self.transactions = json.load(file)
                self.categories = {t['category'] for t in self.transactions}
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with empty tracker.")

    def view_category_summary(self):
        if not self.transactions:
            print("No transactions available to summarize.")
            return

        summary = {}
        for transaction in self.transactions:
            category = transaction["category"]
            summary[category] = summary.get(category, 0) + transaction["amount"]

        print("\nCategory Summary:")
        for category, total in summary.items():
            print(f"{category}: {total}")


def main():
    tracker = PersonalFinanceTracker()
    tracker.load_from_file()

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add transaction")
        print("2. View transactions")
        print("3. View category summary")
        print("4. Calculate total spending")
        print("5. Calculate total income")
        print("6. Save data")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount (use negative for spending): "))
                category = input("Enter category: ")
                description = input("Enter description (optional): ")
                tracker.add_transaction(amount, category, description)
            except ValueError:
                print("Invalid amount. Please try again.")

        elif choice == "2":
            tracker.view_transactions()

        elif choice == "3":
            tracker.view_category_summary()

        elif choice == "4":
            tracker.calculate_total_spending()

        elif choice == "5":
            tracker.calculate_total_income()

        elif choice == "6":
            tracker.save_to_file()

        elif choice == "7":
            tracker.save_to_file()
            print("Exiting. Data saved.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
