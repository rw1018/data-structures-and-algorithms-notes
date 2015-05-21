#Finding the largest or smallest N items

#You'd use a heap if you are only interested in the smallest value, or the first n #smallest #values, especially if you are interested in those values on an ongoing basis; #adding new #items and removing the smallest is very efficient indeed, more so than #resorting the list #each time you added a value.

import heapq

numbers = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

print(heapq.nlargest(3, numbers)) # Prints [42,37,23]
print(heapq.nsmallest(3, numbers)) # Prints [-4, 1, 2]


portfolio = [
       {'name': 'IBM', 'shares': 100, 'price': 91.1},
       {'name': 'AAPL', 'shares': 50, 'price': 543.22},
       {'name': 'FB', 'shares': 200, 'price': 21.09},
       {'name': 'HPQ', 'shares': 35, 'price': 31.75},
       {'name': 'YHOO', 'shares': 45, 'price': 16.35},
       {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print("cheap: ", cheap)
print("expensive: ", expensive)
