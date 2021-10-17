class Item:
    def __init__(self, weight, price):
        self.weight = weight
        self.price = price
        self.ratio = price / weight

    def __str__(self):
        return f"weight: {self.weight}, price: {self.price}"


def comprehensive_review(weight, max_weight, price):
    binary_list = []
    for i in range(0, 2 ** len(weight)):
        bin_number = f'{i:0{len(weight)}b}'
        binary_list.append(bin_number)

    best_price = 0
    best_number = ""
    for bin_number in binary_list:
        current_weight = 0
        current_price = 0
        for i in range(0, len(weight)):
            if bin_number[i] == '1':
                current_weight += weight[i]
                current_price += price[i]
        if current_weight < max_weight and current_price > best_price:
            best_price = current_price
            best_number = bin_number

    return best_price, best_number


def heuristic_review(items, max_weight):
    items.sort(key=lambda x: x.ratio, reverse=True)

    packed_items = []
    current_weight = 0
    current_price = 0
    for item in items:
        if item.weight + current_weight <= max_weight:
            current_weight += item.weight
            current_price += item.price
            packed_items.append(item)

    return current_price, packed_items


def main():
    w = [8, 3, 5, 2]
    W = 9
    p = [16, 8, 9, 6]

    items = [Item(w[i], p[i]) for i in range(0, len(w))]

    print(heuristic_review(items, W))
    print(comprehensive_review(w, W, p))


if __name__ == "__main__":
    main()
