from get_prices import currencies, fetch_price
import math

def get_price_matrix():
    price_matrix = [[0 for i in range(len(currencies))] for j in range(len(currencies))]
    for i, c0 in enumerate(currencies):
        for j, c1 in enumerate(currencies):
            if c0 == c1:
                price_matrix[i][j] = 0.0
                continue

            price_matrix[i][j] = -1*math.log(fetch_price(c0, c1))
        
    return price_matrix

