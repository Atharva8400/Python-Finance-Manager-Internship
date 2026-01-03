import csv
import shutil
import os
from src.expense import Expense

# Path to data folder
DATA_FILE = 'data/expenses.csv'

def save_expenses(expenses):
    if not os.path.exists('data'):
        os.makedirs('data')
    with open(DATA_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])
        for exp in expenses:
            writer.writerow([exp.date, exp.category, exp.amount, exp.description])

def load_expenses():
    expenses = []
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(Expense(row['Amount'], row['Category'], row['Date'], row['Description']))
    return expenses

def backup_data():
    if os.path.exists(DATA_FILE):
        if not os.path.exists('backups'):
            os.makedirs('backups')
        shutil.copy2(DATA_FILE, 'backups/expenses_backup.csv')
        print("\n✅ Backup created in 'backups' folder.")
    else:
        print("\n❌ No data file found to backup.")

def restore_data():
    if os.path.exists('backups/expenses_backup.csv'):
        shutil.copy2('backups/expenses_backup.csv', DATA_FILE)
        print("\n✅ Data restored from backup!")
        return True
    return False