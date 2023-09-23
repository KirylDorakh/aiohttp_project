def calc():
    history = []
    result = 0
    while True:
        x, y = (yield result)
        if x == 'h':
            print(history)
            continue
        result = x + y
    history.append(result)


c = calc()

next(c)           # Необходимая инициация. Можно написать c.send(None)
print(c.send((1, 2)))   # Выведет и вернёт 3
print(c.send((100, 30))) # ничего не выведет и вернёт None
print(c.send((666, 0))) # Выведет и вернёт 666
c.send(('h', 0))
