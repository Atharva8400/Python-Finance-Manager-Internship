def generate_summary(expenses):
    if not expenses:
        print("\nNo data available.")
        return

    summary = {}
    total = 0
    for exp in expenses:
        summary[exp.category] = summary.get(exp.category, 0) + exp.amount
        total += exp.amount

    print("\n--- CATEGORY-WISE REPORT ---")
    for cat, amt in summary.items():
        print(f"{cat.capitalize()}: ₹{amt:.2f}")
    print(f"TOTAL: ₹{total:.2f}")
    print(f"AVERAGE: ₹{total/len(expenses):.2f}")