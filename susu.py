
from decimal import Decimal


class SusuGroup:
    def __init__(self, weekly_contribution):
        self.weekly_contribution = Decimal(str(weekly_contribution))

        if self.weekly_contribution <= 0:
            raise ValueError("Weekly contribution must be greater than zero.")

        self.members = []
        self.current_week = 1
        self.payout_history = []
        self.contributions = {}

    def add_member(self, name):
        name = name.strip()

        if not name:
            raise ValueError("Member name cannot be empty.")

        if name in self.members:
            raise ValueError(f"{name} is already a member.")

        self.members.append(name)

    def remove_member(self, name):
        name = name.strip()

        if name not in self.members:
            raise ValueError(f"{name} is not a member.")

        if any(name in payments for payments in self.contributions.values()):
            raise ValueError(
                "Cannot remove a member who has made contributions."
            )

        self.members.remove(name)

    def record_contribution(self, name, amount):
        name = name.strip()
        amount = Decimal(str(amount))

        if name not in self.members:
            raise ValueError("Member does not exist.")

        if not amount.is_finite() or amount <= 0:
            raise ValueError("Contribution must be a positive amount.")

        if self.current_week not in self.contributions:
            self.contributions[self.current_week] = {}

        week_payments = self.contributions[self.current_week]

        already_paid = week_payments.get(name, Decimal("0.00"))
        amount_owed = self.weekly_contribution - already_paid

        if amount > amount_owed:
            raise ValueError("Payment exceeds the amount owed.")

        week_payments[name] = already_paid + amount

        return week_payments[name]

    def calculate_payout(self):
        return self.weekly_contribution * len(self.members)

    def close_week(self):
        if not self.members:
            raise ValueError("Cannot close a week without members.")

        week_payments = self.contributions.get(
            self.current_week, {}
        )

        unpaid_members = []

        for name in self.members:
            amount_paid = week_payments.get(
                name, Decimal("0.00")
            )
            amount_owed = self.weekly_contribution - amount_paid

            if amount_owed > 0:
                unpaid_members.append(name)

        if unpaid_members:
            raise ValueError(
                f"Cannot close week. Members still owe money: "
                f"{', '.join(unpaid_members)}"
            )

        recipient_index = (self.current_week - 1) % len(self.members)
        recipient = self.members[recipient_index]
        pot = self.calculate_payout()

        self.payout_history.append({
            "week": self.current_week,
            "recipient": recipient,
            "amount": pot
        })

        self.current_week += 1

        return {
            "week": self.current_week - 1,
            "recipient": recipient,
            "amount": pot
        }

    def get_week_report(self):
        week_payments = self.contributions.get(
            self.current_week, {}
        )

        report = []

        for name in self.members:
            amount_paid = week_payments.get(
                name, Decimal("0.00")
            )
            amount_owed = self.weekly_contribution - amount_paid

            report.append({
                "name": name,
                "amount_paid": amount_paid,
                "amount_owed": amount_owed,
                "paid_in_full": amount_owed == 0
            })

        return report


def main():
    print("Welcome to Susu Group Tracker!")

    try:
        weekly_amount = input("Enter weekly contribution in GHS: ")
        group = SusuGroup(weekly_amount)
    except ValueError as error:
        print(f"Error: {error}")
        return

    while True:
        print("\n--- Susu Group Tracker ---")
        print(f"Current week: {group.current_week}")
        print("1. Add member")
        print("2. Record contribution")
        print("3. Close week")
        print("4. View payment report")
        print("5. View payout history")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        try:
            if choice == "1":
                name = input("Enter member name: ")
                group.add_member(name)
                print(f"{name.strip()} added successfully.")

            elif choice == "2":
                name = input("Enter member name: ")
                amount = input("Enter payment amount in GHS: ")
                total_paid = group.record_contribution(name, amount)
                print(f"Total paid this week: GHS {total_paid}")

            elif choice == "3":
                result = group.close_week()
                print(f"Week {result['week']} closed successfully.")
                print(f"Recipient: {result['recipient']}")
                print(f"Pot paid: GHS {result['amount']}")

            elif choice == "4":
                report = group.get_week_report()

                if not report:
                    print("There are no members to report.")

                for member in report:
                    status = (
                        "Paid in full"
                        if member["paid_in_full"]
                        else "Payment outstanding"
                    )
                    print(
                        f"{member['name']}: "
                        f"Paid GHS {member['amount_paid']}, "
                        f"Owes GHS {member['amount_owed']} "
                        f"({status})"
                    )

            elif choice == "5":
                if not group.payout_history:
                    print("No payouts have been recorded yet.")
                else:
                    for payout in group.payout_history:
                        print(
                            f"Week {payout['week']}: "
                            f"{payout['recipient']} received "
                            f"GHS {payout['amount']}"
                        )

            elif choice == "6":
                print("Thank you for using Susu Group Tracker!")
                break

            else:
                print("Invalid option. Please choose 1 to 6.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()


    

    







