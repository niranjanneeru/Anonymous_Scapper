def for_(data, per):
    for i in data:
        print(i[0], i[1] * (100 / per) - i[2])