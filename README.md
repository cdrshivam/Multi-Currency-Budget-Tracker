# Multi-Currency Budget Tracker

## Overview

 A Python-based Comman-Line Interface application designed to help users manage their income, expenses, and budgets efficiently. Users can log transactions, view summaries, manage categories, and track budgets in multiple currencies (USD, GBP, EUR).

---

## Features

1. **Add Transactions**:
   - Input income or expense transactions with details such as date, amount, currency, category, and description.
2. **View Transactions**:
   - Display all transactions or filter by date range.
3. **Summary Reports**:
   - View transaction summaries by date range or category.
4. **Category Management**:
   - Add, view, and manage income and expense categories.
   - Set budgets for expense categories in multiple currencies.
5. **Budget Tracking**:
   - Monitor expenses against predefined budgets and highlight overspending.

---

## Setup Instructions

1. **Prerequisites**:
   - Python 3.8+
   - Pandas library

2. **Install Dependencies**:
   Install the required Python libraries:
   ```bash
   pip install pandas
   ```
   For Testing, install pytest:
    ```bash
   pip install -U pytest
   ```

3. **File Setup**:
   Ensure the following CSV files exist in the project directory:
   - `transactions_data.csv` (for transaction records)
   - `category.csv` (for category details)

   If these files are missing, the application will initialize them automatically.

---

## How to Run

Run the main script:
```bash
python src/main.py
```

---

## Application Menu

1. **Enter a transaction**
2. **View all transactions**
3. **View transactions between a certain date range**
4. **View summary for all transactions**
5. **View summary for transactions between a certain date range**
6. **Add category and budget**
7. **View all categories**
8. **View summary by categories**
9. **Exit**

---

## Code Highlights

### Key Modules and Methods:
- **`Transactions` Class**:
  - Manages transaction and category data.
  - Provides methods to add, view, and summarize transactions.

- **Input Functions**:
  - `get_date(prompt, allow_default=False)`: Validates and formats date input.
  - `get_transaction_type()`: Prompts for transaction type (Income/Expense).
  - `get_amount()`: Validates and formats amount input.
  - `get_category(categoryType)`: Fetches or creates a new transaction category.
  - `get_description()`: Captures transaction description.

---

## Sample CSV Format

### Transactions (`transactions_data.csv`):
| Date       | TransactionType | Amount  | Currency | Category     | Description          |
|------------|-----------------|---------|----------|--------------|----------------------|
| 25-12-2023 | Expense         | 100.50  | USD      | Groceries    | Weekly groceries     |
| 01-01-2024 | Income          | 1500.00 | GBP      | Salary       | Monthly paycheck     |

### Categories (`category.csv`):
| Category    | Category_Type | Budget_USD | Budget_GBP | Budget_EUR |
|-------------|---------------|------------|------------|------------|
| Groceries   | Expense       | 500.00     | 400.00     | 450.00     |
| Salary      | Income        |            |            |            |

---

## Future Enhancements

- Add a GUI for easier user interaction.
- Support for additional currencies.
- Export summary reports to PDF or Excel using matplotlib.


---

## Author

**Shivam Bhatia**

---

This project is created and submited as a final project for CS50's Introduction to Programming with Python course conducted by Harvard University