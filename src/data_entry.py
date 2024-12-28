import sys
import pandas as pd
from datetime import datetime
import csv
from transaction import Transactions as trans


date_format = '%d-%m-%Y'
CATEGORY_CSV = 'category.csv'
COLUMNS_CATEGORY = ['Category', 'Category_Type', 'Budget_USD', 'Budget_GBP', 'Budget_EUR']
currencyList = ['USD', 'GBP', 'EUR']

def get_avail_category(transactionType):
    try:
        df =  pd.read_csv(CATEGORY_CSV)
        new_df = df.loc[df['Category_Type']==transactionType]
        if len(new_df) == 0:
            return []
        else:
            return new_df['Category'].to_list()
    except FileNotFoundError:
        print('Categories file not found')
        return []

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError as e:
        print(f'Invalid Date Format. Please enter in dd-mm-yyyy format - {e}')
        return get_date(prompt, allow_default)
    

def get_transaction_type():
    while True:
        trans_type = input("Enter Transaction Type ('I' for Income & 'E' for Expense): ")
        if trans_type.capitalize() == 'I' :
            return 'Income'
        elif trans_type.capitalize() == 'E':
            return 'Expense'
        else:
            continue

def get_amount(prompt = 'Enter the amount: '):
    try:
        amount = float(input(prompt))
        return f'{amount:.2f}'
    except ValueError:
        print('Please enter correct amount')
        get_amount()


def get_currency():
    while True:
        print(f'We only support {currencyList}')
        currency = input('Enter the currency of transaction: ').upper()
        if currency in currencyList:
            return currency
        else:
            continue


def get_category(categoryType):
    category_list = get_avail_category(categoryType)
    if len(category_list) == 0:
        print(f'No {categoryType} categories available.\nCreate a new {categoryType} category')
        trans.initializeCategoryCSV()
        new_category = get_new_category(categoryType)
        trans.add_category(new_category)
        return new_category['Category']
    else:
        print('Available categories :')
        print(category_list)
        while True:
            category =  input('Enter transactional category: ')
            if category in category_list:
                return category
            else:
                print('The category you entered is not available')
                print('1. Continue with existing catories')
                print('2. Create a new category')
                option = input("Enter your choice: ")
                match option:
                    case '1': continue
                    case '2': 
                        trans.initializeCategoryCSV()
                        new_category = get_new_category(categoryType)
                        trans.add_category(new_category)
                        return new_category['Category']
                    case _: continue
                


def get_new_category(categoryType=None):
    category_Type = categoryType
    if categoryType == None: 
        category_Type = get_transaction_type()
    category = input('Enter transactional category: ')
    if category_Type == 'Income':
        print(f'For income categories, you can not set any limits')
        budget_usd = None
        budget_gbp = None
        budget_eur = None

    else:
        budget_usd = get_amount(prompt=f'Enter {category}\'s budget for USD account: ')
        budget_gbp = get_amount(prompt=f'Enter {category}\'s budget for GBP account: ')
        budget_eur = get_amount(prompt=f'Enter {category}\'s budget for EUR account: ')

    new_category = {
            'Category': category,
            'Category_Type': category_Type,
            'Budget_USD': budget_usd,
            'Budget_GBP': budget_gbp,
            'Budget_EUR': budget_eur
        }
    return new_category


def get_description():
    return input('Enter transaction description (optional): ')