class Expense:
    def __init__(self, amount, category, date, description):
        # Attributes: amount, category, date, description
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.description = description
    
    def __str__(self):
        # Formatting for display
        return f"{self.date} | {self.category.upper()}: ₹{self.amount:.2f} - {self.description}"