def fizz_buzz():
    for i in range(100):
        if i % 3 == 0 and i % 5 == 0:
            print("i={} -> fizzbuzz".format(i))
        elif i % 3 == 0:
            print("i={} -> fizz".format(i))
        elif i % 5 == 0:
            print("i={} -> buzz".format(i))
