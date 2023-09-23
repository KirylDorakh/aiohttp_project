def calc():
    history = []
    result = 0
    while True:
        x, y = (yield result)
        if x == 'h':
            print(history)
            continue
        result = x + y
        print(result)
        history.append(result)


c = calc()

print(type(c))

next(c)
# Необходимая инициация. Можно написать c.send(None)
c.send((1, 2))
c.send((100, 30)) # Выведет 130
c.send((666, 0)) # Выведет 666
c.send(('h',0)) # Выведет [3, 130, 666]
c.close() # Закрывем генератор

