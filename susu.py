
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
    
    

