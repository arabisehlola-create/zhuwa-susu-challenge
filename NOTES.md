# Project Notes — Susu Group Tracker

## Assumptions and Decisions

1. **Contribution currency:** The challenge uses GHS (Ghanaian cedi). The program uses Python's `Decimal` type to avoid floating-point rounding errors.
2. **Fixed contribution:** Every member must contribute the same fixed amount each week.
3. **Partial payments:** Members can pay in multiple instalments during the current week.
4. **Week closing:** A week can close only when every member has paid the full weekly contribution.
5. **Payout order:** Members receive the pot in the order they joined the group. After the last member receives the pot, the order starts again.
6. **Payout amount:** The pot equals the weekly contribution multiplied by the number of members.
7. **Member names:** Member names must not be empty or duplicated.
8. **Member removal:** A member who has made a contribution cannot be removed.
9. **Payment validation:** The program rejects unknown members, zero or negative payments, and payments greater than the remaining amount owed.
10. **Data storage:** Group information is stored in memory and is not saved after the program exits.
11. **Interface:** A command-line menu lets users manage members, record payments, close weeks, and view reports.

## Testing

The project uses Python's built-in `unittest` framework. The tests cover member management, contribution calculations, partial payments, invalid payments, week closing, payout rotation, and payment reports.

Run the tests with:

```bash
python3 -m unittest -v
```

## Possible Improvements

- Support unique member IDs in addition to unique names.
- Allow reports for previous weeks.
- Improve member-management rules once a savings cycle has started.
- Add more tests for invalid inputs and unusual situations.
- Save group data between program runs.