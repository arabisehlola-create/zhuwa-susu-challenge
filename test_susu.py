
import unittest
from susu import SusuGroup


class TestSusuGroup(unittest.TestCase):

    def test_group_starts_with_no_members(self):
        group = SusuGroup(100)
        self.assertEqual(group.members, [])

    def test_add_member(self):
        group = SusuGroup(100)
        group.add_member("Arabi")
        self.assertIn("Arabi", group.members)

    def test_prevent_duplicate_member(self):
        group = SusuGroup(100)
        group.add_member("Arabi")
        group.add_member("Arabi")
        self.assertEqual(len(group.members), 1)

    def test_remove_member(self):
        group = SusuGroup(100)
        group.add_member("Arabi")
        group.remove_member("Arabi")
        self.assertNotIn("Arabi", group.members)

    def test_calculate_weekly_contributions(self):
        group = SusuGroup(100)
        group.add_member("Arabi")
        group.add_member("Sipho")
        self.assertEqual(group.calculate_payout(), 200)


if __name__ == "__main__":
    unittest.main()




