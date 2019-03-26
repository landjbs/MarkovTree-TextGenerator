def str_check(a,b):
    subject = a.upper()
    check = b.upper()
    if subject == check:
        return 0
    length = min([len(subject),len(check)])
    for i in range(length):
        if ord(subject[i]) > ord(check[i]):
            return -1
        elif ord(subject[i]) < ord(check[i]):
            return 1
    if len(subject) > length:
        return -1
    else:
        return 1

print(str_check("Landz", "Landone"))
