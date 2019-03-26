from datetime import datetime

def str_check(a,b):
    '''
    purpose: determine which of two strings comes first alphabetically
    args: a - subject string
          b - string to be checked against
    returns: 0 if words are the same
             1 if subject string is alphabetically first
             -1 if check string is alphabetically first
             str_check("fo", "foo") returns 1
    '''
    #take strings to uppercase
    subject = a.lower()
    check = b.lower()
    #determine if strings are the same
    if subject == check:
        return 0
    #take length of shortest string
    length = min([len(subject),len(check)])
    #iterate through letters to determine first string
    for i in range(length):
        if ord(subject[i]) > ord(check[i]):
            return -1
        elif ord(subject[i]) < ord(check[i]):
            return 1
    #if the letters are the same, shortest string is first alphabetically
    if len(subject) > length:
        return -1
    else:
        return 1

def time_function(f):
    start=datetime.now()

    f

    print(datetime.now()-start)

time_function((3 + 4))
