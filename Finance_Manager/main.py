from src.expense import Expense
from src import file_manager
from src import reports

def main():
    expenses = file_manager.load_expenses()
    
    while True:
        print("\n1. Add Expense | 2. View All | 3. Report | 4. Backup | 5. Restore | 6. Exit")
        choice = input("Choice (1-6): ")
        
        if choice == '1':
            try:
                amt = input("Amount: ")
                cat = input("Category: ")
                dt = input("Date (YYYY-MM-DD): ")
                desc = input("Description: ")
                expenses.append(Expense(amt, cat, dt, desc))
                print("✅ Added!")
            except ValueError:
                print("❌ Invalid amount.")
        elif choice == '2':
            for exp in expenses: print(exp)
        elif choice == '3':
            reports.generate_summary(expenses)
        elif choice == '4':
            file_manager.backup_data()
        elif choice == '5':
            if file_manager.restore_data(): expenses = file_manager.load_expenses()
        elif choice == '6':
            file_manager.save_expenses(expenses)
            break

if __name__ == "__main__":
    main()