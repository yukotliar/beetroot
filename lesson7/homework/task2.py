# Create a function which takes as input two dicts with structure mentioned below,
# then computes and returns the total price of stock.

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def total_counter(dict1, dict2):
    for key in dict1:
        dict1[key] *= dict2[key]
    return dict1


print(total_counter(stock, prices))
