#Unpacking a sequence into seperate variables
p = (4,5)
x, y = p
# returns 4
# return 5


data = ["hello", 50, 32.22, (2012,12,21)]
name, shares, price, date = data

#use a throwaway variable to discard certain values
name, _, price, (year, mon, day) = data

#Unpack elements from iterables of arbitrary length N
record = ('Ronald', 'ronald@email.com', '123 456 7890', '888 888 8888')
name, email, *phone_numbers = record
#phone_numbers is a list: ['123 456 7890', '888 888 8888']

#Star syntax is especially useful when iterating over sequences of tuples of varying length
data = [
    ("Dave", 1, 2),
    ("Dave", "World",2),
    ("Joe", "Bar"),
]

def print_dave(x,y):
    print("Dave",x,y)

def print_joe(s):
    print("Joe", s)

for name, *args in data:
    if name == "Dave":
        print_dave(*args)
    elif name == "Joe":
        print_joe(*args)
