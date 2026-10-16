
import unittest
from decimal import Decimal
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

        with self.assertRaises(ValueError):
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

        self.assertEqual(
            group.calculate_payout(),
            Decimal("200")
        )

    def test_record_partial_contribution(self):
        group = SusuGroup(50)
        group.add_member("Ama")

        paid = group.record_contribution("Ama", 20)

        self.assertEqual(paid, Decimal("20"))

    def test_reject_zero_contribution(self):
        group = SusuGroup(50)
        group.add_member("Ama")

        with self.assertRaises(ValueError):
            group.record_contribution("Ama", 0)

    def test_reject_payment_above_amount_owed(self):
        group = SusuGroup(50)
        group.add_member("Ama")

        with self.assertRaises(ValueError):
            group.record_contribution("Ama", 60)

    def test_reject_unknown_member_contribution(self):
        group = SusuGroup(50)

        with self.assertRaises(ValueError):
            group.record_contribution("Lebo", 20)

    
    def test_week_cannot_close_if_member_owes_money(self):
        group = SusuGroup(50)
        group.add_member("Ama")
        group.add_member("Kojo")

        group.record_contribution("Ama", 50)
        group.record_contribution("Kojo", 20)

        with self.assertRaises(ValueError):
            group.close_week()

        self.assertEqual(group.current_week, 1)
        self.assertEqual(group.payout_history, [])

    
    def test_successful_payout_and_rotation(self):
        group = SusuGroup(50)
        group.add_member("Ama")
        group.add_member("Kojo")

        group.record_contribution("Ama", 50)
        group.record_contribution("Kojo", 50)

        result = group.close_week()

        self.assertEqual(result["recipient"], "Ama")
        self.assertEqual(result["amount"], Decimal("100"))
        self.assertEqual(group.current_week, 2)
        self.assertEqual(len(group.payout_history), 1)

        group.record_contribution("Ama", 50)
        group.record_contribution("Kojo", 50)

        result = group.close_week()

        self.assertEqual(result["recipient"], "Kojo")
        self.assertEqual(group.current_week, 3)
        self.assertEqual(len(group.payout_history), 2)


    
    def test_week_report_shows_amount_paid_and_owed(self):
        group = SusuGroup(50)
        group.add_member("Ama")
        group.add_member("Kojo")

        group.record_contribution("Ama", 50)
        group.record_contribution("Kojo", 20)

        report = group.get_week_report()

        self.assertEqual(report[0]["amount_paid"], Decimal("50"))
        self.assertEqual(report[0]["amount_owed"], Decimal("0"))
        self.assertTrue(report[0]["paid_in_full"])

        self.assertEqual(report[1]["amount_paid"], Decimal("20"))
        self.assertEqual(report[1]["amount_owed"], Decimal("30"))
        self.assertFalse(report[1]["paid_in_full"])
    
    
        



if __name__ == "__main__":
    unittest.main()





