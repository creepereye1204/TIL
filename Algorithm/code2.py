fruit = ["apple", "banana", "cherry", "kiwi", "watermelon", "strawberry"]
fruitLen = list(map(len, fruit))
fruitZip = list(zip(fruit, fruitLen))
fruitSort = sorted(fruitZip, key=lambda x: x[1], reverse=True)
for i, j in fruitSort:
    print("{:<13}\t{:>2}".format(i, j))
