def get_good():
    get_good_input = input("Enter a float between 1 and 100:  ")
    try: 
        get_good_float = float(get_good_input)
        #get_good_int = int(get_good_input)
        if get_good_float >= 1.0 and get_good_float <= 100.0:
            print("Returning, " + str(get_good_float)) 
            return get_good_float
        if get_good_float<= 1.0 or get_good_float >= 100.0:
            print("The number is out of range, returning 0.0")
            return 0.0
    except: 
        print("The number is invalid, returning -1.0")
        return -1.0


def sum_and__avg():
    total = 0
    counter = 0
    one = get_good()
    two = get_good()
    three = get_good()
    four = get_good()
    if type(one) == float and one >= 0.0:
        total += one
        counter += 1
    if type(two) == float and two >= 0.0:
        total += two
        counter += 1
    if type(three) == float and three >= 0.0:
        total += three
        counter += 1
    if type(four) == float and four >= 0.0:
        total += four
        counter += 1
    print("sum:" + str(total))
    print("avg: " + str(total/counter))

print("pwnia", 100)
num = 100
print(str(num*5))
