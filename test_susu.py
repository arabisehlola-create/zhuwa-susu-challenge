
from susu import SusuGroup

# Create a savings group
group = SusuGroup(100)

# Add two members
group.add_member("Arabi")
group.add_member("Thandi")
group.add_member("Arabi")  # Attempt to add a duplicate member

# Display the members
print("Final members:", group.members)

