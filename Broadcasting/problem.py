import numpy as np

prices = np.array([100,200,300, 400])
discount = 10

new_prices = prices - (prices * discount/100)
print(new_prices)