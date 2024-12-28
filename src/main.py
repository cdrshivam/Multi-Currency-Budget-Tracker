from transaction import Transactions as trans
from data_entry import get_amount, get_category, get_currency, get_date, get_description, get_transaction_type, get_new_category


def main():
    print('\nPersonal Finance Portal')
    print('\nWelcome Back Shivam!')

    while True:
        print('\n1. Enter a transaction')

        print('2. View all transactions')
        print('3. View transactions between a certain date range')
        print('4. View Summary for all transactions')
        print('5. View Summary for transactions between a certain date range')
        print('6. Add category and budget')
        print('7. View all categories')
        print('8. View Summary by categories')
        print('9. Exit')

        choice = input('\nEnter your choice: ')
        match choice:
            case '1': 
                date = get_date('Enter transaction date (dd-mm-yyyy): ', allow_default=True)
                transactionType = get_transaction_type()
                Amount = get_amount()
                Currency = get_currency()
                Category = get_category(transactionType)
                Description = get_description()
                trans.initializeTransactionsCSV()
                trans.add_transaction(date, transactionType, Amount, Currency, Category, Description)
            case '2': 
                trans.view_transaction()
            case '3': 
                start_date = get_date('Enter start date (dd-mm-yyyy): ', allow_default=True)
                end_date = get_date('Enter end date (dd-mm-yyyy): ', allow_default=True)
                trans.view_transaction(start_date, end_date)
            case '4':
                trans.view_summary()
            case '5':
                start_date = get_date('Enter start date (dd-mm-yyyy): ', allow_default=True)
                end_date = get_date('Enter end date (dd-mm-yyyy): ', allow_default=True)
                trans.view_summary(start_date, end_date)
            case '6':
                trans.initializeCategoryCSV()
                trans.add_category(get_new_category())
            case '7':
                trans.view_category()
            case '8':
                trans.view_summary_category()
            case '9':
                break
            case _:
                print('Please enter a valid choice')


if __name__ == '__main__':
    main()