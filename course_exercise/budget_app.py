class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        title = f'{self.name:*^30}\n'
        items = ''
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'

            total += item['amount']

        output = title + items + 'Total: ' + str(total)
        return output

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        total_money = 0
        for money in self.ledger:
            total_money += money['amount']
        return total_money

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True


def create_spend_chart(categories):
    items = len(categories)
    if items == 0:
        return 'No categories provided'
    chart = 'Percentage spent by category\n'
    data = list()
    lines = 0
    total = 0.00

    for cat in categories:
        # takes longest cat name to set number of lines
        if lines < len(cat.name):
            lines = len(cat.name)

        spent = 0.00
        for wit in cat.ledger:
            if wit['amount'] < 0:
                spent += wit['amount']
        total += spent
        data.append([cat.name, abs(spent)])

    total = abs(total)

    for d in data:
        percent = d[1] / total * 100
        d[1] = percent

    # print(data)
    for n in reversed(range(11)):
        n = n * 10
        num = str(n)
        line = str()
        if num == '0':
            line += ' '
        if num != '100':
            line += ' '
        line += num + '|'

        for d in data:
            if n < d[1]:
                line += ' o '
            else:
                line += '   '

        chart += line + ' \n'

    chart += '    -'
    for n in range(items):
        chart += '---'

    for n in range(lines):
        chart += '\n    '
        for d in data:
            try:
                chart += ' ' + d[0][n] + ' '
            except:
                chart += '   '
        chart += ' '

    return chart
