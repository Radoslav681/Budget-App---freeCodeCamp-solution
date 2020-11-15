class Category:
  '''Instantiate objects based on different budget categories'''
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=''):
    self.ledger.append({'amount': amount, 'description': description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({'amount': -amount, 'description': description})
      return True
    return False

  def get_balance(self):
    balance = 0
    for i in self.ledger:
      balance += i['amount']
    return balance

  def transfer(self, amount, other_category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {other_category.name}")
      other_category.deposit(amount, f"Transfer from {self.name}")
      return True
    return False

  def check_funds(self, amount):
    if self.get_balance() >= amount:
      return True
    return False

  def __str__(self):
    summary = self.name.center(30, "*") + '\n'
    for details in self.ledger:
      summary += f"{details['description'][:23].ljust(23)}{format(details['amount'], '.2f').rjust(7)}\n"
    summary += f"Total: {format(self.get_balance(), '.2f')}"
    return summary

def create_spend_chart(categories):
  category_names = []
  money_spent = []
  percentages = []

  for category_name in categories:
    total = 0
    for amount in category_name.ledger:
      if amount['amount'] < 0:
        total -= amount['amount']
    money_spent.append(round(total,2))
    category_names.append(category_name.name)

  for money in money_spent:
    percentages.append(round(money / sum(money_spent), 2) *100)

  chart = 'Percentage spent by category\n'

  for label in range(100, -10, -10):
    chart += str(label).rjust(3) + '| '
    for percent in percentages:
      if percent >= label:
        chart += 'o  '
      else:
        chart += '   '
    chart += '\n'

  chart += "    ----" + ("---" * (len(category_names) -1))
  chart += "\n     "

  longest_name = 0

  for name in category_names:
    if longest_name < len(name):
      longest_name = len(name)

  for n in range(longest_name):
    for name in category_names:
      if len(name) > n:
        chart += name[n] + "  "
      else:
        chart += "   "
    if n < longest_name - 1:
      chart += '\n     '
  
  return chart