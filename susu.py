
from decimal import Decimal


class SusuGroup:
    def __init__(self, weekly_contribution):
        self.weekly_contribution = Decimal(str(weekly_contribution))
        self.members = []
        self.current_week = 1
        self.payout_history = []

    
    def add_member(self, name):
        name = name.strip()

        if not name:
            print("Error: Member name cannot be empty.")
        elif name in self.members:
            print(f"{name} is already a member.")
        else:
            self.members.append(name)
            print(f"{name} has been added successfully.")


  
        