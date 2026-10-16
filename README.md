# Susu Group Tracker

## Project Overview

Susu Group Tracker is a Python command-line project that manages a rotating savings group.

Members contribute a fixed amount each week. When all members have paid their full contributions, the collected pot is paid to the next member in joining order.

## Features

- Add members and prevent duplicate names.
- Remove members when they have not made contributions.
- Record full and partial weekly contributions.
- Reject invalid payments and unknown members.
- Prevent a week from closing when members still owe money.
- Pay the pot to members in rotating joining order.
- Record payout history.
- Generate a report showing payments and outstanding amounts.
- Use Python's `Decimal` type for accurate money calculations.
- Run automated tests using Python's built-in `unittest` framework.

## Requirements

- Python 3
- No external Python packages are required.

## How to Run the Application

Open a terminal in the project folder and run:

```bash
python3 susu.py
```

Follow the menu to add members, record contributions, close weeks, and view reports or payout history.

## How to Run the Tests

Open a terminal in the project folder and run:

```bash
python3 -m unittest -v
```

## Project Files

- `susu.py` — contains the Susu group logic.
- `test_susu.py` — contains automated tests.

## Current Status

The core group management, contribution recording, week-closing, payout rotation, and payment-report features have automated tests.

## Current Limitations

- Group data is stored in memory and is lost when the program exits.
- The application manages one savings group at a time.

## Author

Arabi Sehlola