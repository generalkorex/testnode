from uuid import uuid4
from datetime import datetime
#Creating a class Expense
class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
#Updating the title and the amount.    
    def update(self, title=None, amount=None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.utcnow()
#Returning a dictionary representation of the expense.
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
#Creating the ExpenseDB
class ExpenseDatabase:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        self.expenses = [i for i in self.expenses if i.id != expense_id]

    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expenses_by_title(self, title):
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]

expense_db = ExpenseDatabase()

expense1 = Expense("food", 25000.0)
expense2 = Expense("transport", 1700.0)
expense3 = Expense("Miscellanous", 10000.0)

expense_db.add_expense(expense1)
expense_db.add_expense(expense2)
expense_db.add_expense(expense3)
print(expense_db.to_dict())
