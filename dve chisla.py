a = int(input("Въведете число за а:"))

b = int(input("Въведете число за b:"))

print(a + b)         # Събиране:

print(a - b)         # Изваждане:

print(a * b)         # Умножение:

print(a / b)         # Деление:

# Степенуване:
if a < b:
    print(b ** a)
else:
    print(a ** b)

# Коренуване:
if a < b:
    print(b ** (1/2))
else:
    print(a ** (1/2))

# Логаритъм:
ACC = 0.001
def log(a):
    min = 0
    max = 0

    f = True
    while f:
        crmin = 2 ** min
        crmax = 2 ** max
        if (a < crmin) and (a < crmax):   # проверка дали търсената стойност е под текущият интервал
            max = min
            min = min - 1
        elif (a > crmin) and (a > crmax):    # проверка дали търсената стойност е над текущият интервал
            min = max
            max = max + 1
        else:   # проверка дали търсената стойност е в текущият интервал
            f = False
    # Търсената стойност е в интервала min <= x <= max
    f = True
    while f:
        crmin = 2 ** min
        crmax = 2 ** max
        if a == crmin:
            # print(f'log при основа 2 от {a} е {min}')
            return min
            f = False
        elif a == crmax:
            # print(f'log при основа 2 от {a} е {max}')
            return min
            f = False
        else:
            mid = (min + max) / 2
            crmid = 2 ** mid
            temp = a - crmid
            if temp < 0:
                temp = -1 * temp
            if temp < ACC:
                # print(f'log при основа 2 от {a} е приблизателно {mid} с точност {ACC}')
                return min
                f = False
            elif a < crmid:
                max = mid
            else:
                min = mid
print(log(a))

# Логаритъм при основа 10:

ACC = 0.001
def lg(a):
    min = 0
    max = 0

    f = True
    while f:
        crmin = 10 ** min
        crmax = 10 ** max
        if (a < crmin) and (a < crmax):   # проверка дали търсената стойност е под текущият интервал
            max = min
            min = min - 1
        elif (a > crmin) and (a > crmax):    # проверка дали търсената стойност е над текущият интервал
            min = max
            max = max + 1
        else:   # проверка дали търсената стойност е в текущият интервал
            f = False
    # Търсената стойност е в интервала min <= x <= max
    f = True
    while f:
        crmin = 10 ** min
        crmax = 10 ** max
        if a == crmin:
            # print(f'log при основа 10 от {a} е {min}')
            return min
            f = False
        elif a == crmax:
            # print(f'log при основа 10 от {a} е {max}')
            return min
            f = False
        else:
            mid = (min + max) / 2
            crmid = 10 ** mid
            temp = a - crmid
            if temp < 0:
                temp = -1 * temp
            if temp < ACC:
                # print(f'log при основа 10 от {a} е приблизателно {mid} с точност {ACC}')
                return min
                f = False
            elif a < crmid:
                max = mid
            else:
                min = mid
print(lg(a))