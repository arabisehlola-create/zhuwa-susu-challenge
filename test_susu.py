

from susu import SusuGroup

group = SusuGroup(100)

group.add_member("Arabi")
group.add_member("Thandi")
group.add_member("Sipho")

print("Before removal:", group.members)

group.remove_member("Thandi")

print("After removal:", group.members)

group.remove_member("Lebo")

print("Final members:", group.members)

print("Weekly payout:", group.calculate_payout())



