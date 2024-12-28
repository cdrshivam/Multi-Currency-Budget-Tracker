import sys
import pandas as pd
from datetime import datetime
import csv

class Transactions:
    
    date_format = '%d-%m-%Y'
    COLUMNS_TRANSACTIONS = ['Date', 'TransactionType', 'Amount', 'Currency', 'Category', 'Description']
    COLUMNS_CATEGORY = ['Category', 'Category_Type', 'Budget_USD', 'Budget_GBP', 'Budget_EUR']
    currencyList = ['USD', 'GBP', 'EUR']
    CSV_TRANSACTIONS = 'transactions_data.csv'
    CSV_CATEGORY = 'category.csv'

    def check_budget(row):
        if row['Currency'] == 'USD':
            budget = row['Budget_USD']
        elif row['Currency'] == 'GBP':
            budget = row['Budget_GBP']
        elif row['Currency'] == 'EUR':
            budget = row['Budget_EUR']
        else:
            budget = None

        if pd.notnull(budget) and row['Total_Expense'] > budget:
            return 'Over Budget'
        return 'Within Budget'        

    @classmethod
    def initializeTransactionsCSV(self):
        try:
            pd.read_csv(self.CSV_TRANSACTIONS)
        except FileNotFoundError:
            df = pd.DataFrame(columns=self.COLUMNS_TRANSACTIONS)
            df.to_csv(self.CSV_TRANSACTIONS, index=False)


    @classmethod
    def initializeCategoryCSV(self):
        try:
            pd.read_csv(self.CSV_CATEGORY)
        except FileNotFoundError:
            df = pd.DataFrame(columns=self.COLUMNS_CATEGORY)
            df.to_csv(self.CSV_CATEGORY, index=False)
    
    @classmethod
    def add_transaction(self, date, transactionType, amount, currency, category, description):
        new_entry = {
            'Date': date,
            'TransactionType' : transactionType,
            'Amount': amount,
            'Currency': currency,
            'Category': category,
            'Description': description
        }
        
        with open(self.CSV_TRANSACTIONS, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.COLUMNS_TRANSACTIONS)
            writer.writerow(new_entry)
        
        print('Entry added successfully !')    

    @classmethod
    def view_transaction(self, start_date='01-01-1995', end_date=datetime.today().strftime(format=date_format)):
        try:
            df =  pd.read_csv(self.CSV_TRANSACTIONS)
            df['Date'] = pd.to_datetime(df['Date'], format = self.date_format)
            start_date = pd.to_datetime(start_date, format = self.date_format)
            end_date = pd.to_datetime(end_date, format = self.date_format)
            new_df = df.loc[(df['Date']>=start_date) & (df['Date']<=end_date)]
            print(new_df.sort_values('Date'))
        except FileNotFoundError as e:
            print('Error Loading the file: {e}')


    @classmethod
    def view_summary(self, start_date='01-01-1995', end_date=datetime.today().strftime(format=date_format)):
        try:
            df =  pd.read_csv(self.CSV_TRANSACTIONS)
            df['Date'] = pd.to_datetime(df['Date'], format = self.date_format)
            start_date = pd.to_datetime(start_date, format = self.date_format)
            end_date = pd.to_datetime(end_date, format = self.date_format)
            new_df = df.loc[(df['Date']>=start_date) & (df['Date']<=end_date)]

            for _ in self.currencyList:
                currency_df = new_df.loc[new_df['Currency']==_]
                income = currency_df.loc[currency_df['TransactionType']=='Income']['Amount'].sum()
                expense = currency_df.loc[currency_df['TransactionType']=='Expense']['Amount'].sum()
                balance = income - expense

                print(f'\nSummary of your {_} account:')
                print(f'Total Income: {income:.2f}')
                print(f'Total Expense: {expense:.2f}')
                print(f'Total Balance: {balance:.2f}')

        except FileNotFoundError as e:
            print('Error Loading the file: {e}')
    

    @classmethod
    def add_category(self,  new_category):
        with open(self.CSV_CATEGORY, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.COLUMNS_CATEGORY)
            writer.writerow(new_category)
        
        print('Category added successfully !')   

    @classmethod
    def view_category(self):
        try:
            df =  pd.read_csv(self.CSV_CATEGORY)
            income_df = df.loc[df['Category_Type']=='Income']
            expense_df = df.loc[df['Category_Type']=='Expense']
            print('\nYou are viewing Income categories\n')
            print(income_df)
            print('\nYou are viewing Expense categories\n')
            print(expense_df)
        except FileNotFoundError as e:
            print(f'Error Loading the file: {e}')

    @classmethod
    def view_summary_category(self, start_date='01-01-1995', end_date=datetime.today().strftime(format=date_format)):
        try:
            transactions = pd.read_csv(self.CSV_TRANSACTIONS)
            categories = pd.read_csv(self.CSV_CATEGORY)
            merged_data = pd.merge(transactions, categories, on='Category', how='left')

            income_data = merged_data[merged_data['TransactionType'] == 'Income']
            expense_data = merged_data[merged_data['TransactionType'] == 'Expense']

            income_summary = income_data.groupby(['Category', 'Currency']).agg(
                Total_Income=('Amount', 'sum')
            ).reset_index()

            expense_summary = expense_data.groupby(['Category', 'Currency']).agg(
                Total_Expense=('Amount', 'sum')
            ).reset_index()

            expense_summary = pd.merge(expense_summary, categories, on='Category', how='left')

            expense_summary['Budget_Status'] = expense_summary.apply(self.check_budget, axis=1)

            print('\nIncome Summary')
            print(income_summary.sort_values('Currency'))

            print('\nExpense Summary')
            print(expense_summary.sort_values('Currency'))

            return {
                'Income_Summary': income_summary,
                'Expense_Summary': expense_summary
            }
                
        except FileNotFoundError as e:
            print('Error Loading the file: {e}')


