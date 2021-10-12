w = [8, 3, 5, 2]
W = 9
p = [16, 8, 9, 6]


def comprehensive_review(weight, max_weight, price):
    binary_list = []
    for i in range(0, 2 ** len(weight)):
        bin_number = f'{i:04b}'
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


def ratio(weigth, price):
    ratio = []
    for i in range(len(weigth)):
        ratio.append(price[i] / weigth[i])
    return ratio


def main():
    print(comprehensive_review(w, W, p))


if __name__ == "__main__":
    main()
