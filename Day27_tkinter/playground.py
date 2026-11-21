def add(*args): # the * allows the function to accept any number of positional arguments and puts them into a tuple called args
    total = 0
    for num in args:
        total += num
    print(total)


add(1, 2, 3)