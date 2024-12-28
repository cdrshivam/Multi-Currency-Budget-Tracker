import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from datetime import datetime
import sys
import os

# Add the src directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from data_entry import get_avail_category, get_date, get_transaction_type, get_amount, get_currency, get_category, get_new_category, get_description


@patch("pandas.read_csv")
def test_get_avail_category(mock_read_csv):
    mock_read_csv.return_value = pd.DataFrame({
        "Category_Type": ["Income", "Expense"],
        "Category": ["Salary", "Groceries"]
    })
    result = get_avail_category("Expense")
    assert result == ["Groceries"]

@patch("builtins.input", side_effect=["25-12-2023"])
def test_get_date(mock_input):
    date_format = "%d-%m-%Y"
    result = get_date("Enter date: ")
    assert result == "25-12-2023"

@patch("builtins.input", side_effect=["E"])
def test_get_transaction_type(mock_input):
    result = get_transaction_type()
    assert result == "Expense"

@patch("builtins.input", side_effect=["100.50"])
def test_get_amount(mock_input):
    result = get_amount()
    assert result == "100.50"

@patch("builtins.input", side_effect=["USD"])
def test_get_currency(mock_input):
    result = get_currency()
    assert result == "USD"

@patch("data_entry.get_avail_category", return_value=["Groceries", "Utilities"])
@patch("builtins.input", side_effect=["Groceries"])
def test_get_category(mock_input, get_avail_category):
    result = get_category("Expense")
    assert result == "Groceries"

@patch("builtins.input", side_effect=["Study", "200.00", "150.00", "100.00"])
def test_get_new_category(mock_input):
    result = get_new_category("Expense")
    assert result == {
        "Category": "Study",
        "Category_Type": "Expense",
        "Budget_USD": "200.00",
        "Budget_GBP": "150.00",
        "Budget_EUR": "100.00"
    }

@patch("builtins.input", side_effect=["This is a test description"])
def test_get_description(mock_input):
    result = get_description()
    assert result == "This is a test description"
