

from susu import SusuGroup

group = SusuGroup(100)

group.add_member("Arabi")
group.add_member("Thandi")
group.add_member("Arabi")  # Duplicate
group.add_member("")       # Empty name
group.add_member("   ")    # Spaces only
group.add_member("  Sipho  ")  # Spaces around a valid name

print("Final members:", group.members)


