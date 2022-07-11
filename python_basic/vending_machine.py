class VendingMachine:
    def __init__(self, num_items, item_price) -> None:
        self.num_items = num_items
        self.item_price = item_price

    def buy(self, req_items, money) -> int:
        if req_items > self.num_items:
            raise ValueError('Not enough items in the machine')

        if req_items * self.item_price > money:
            raise ValueError('Not enough coins')

        self.num_items -= req_items
        return money - req_items * self.item_price

if __name__ == '__main__':
    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            print(change)
        except ValueError as e:
            print(str(e) + "\n")