class Tab:

    menu = {
        'Wine': 11,
        'Beer': 5,
        'Soft drink': 3,
        'Chicken': 10,
        'Steak': 18,
        'Desert': 9
    }

    def __init__(self):
        self.total = 0
        self.items = []

    def add(self, item):
        self.items.append(item)
        self.total += self.menu[item]

    def print_bill(self, tax, service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total
        total = self.total + tax + service

        for item in self.items:
            print(f'{item:20} £{self.menu[item]}')
        
        print(f'{"Total":20} £{total:.2f}')