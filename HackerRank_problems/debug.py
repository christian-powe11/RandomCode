n = 4 

if n % 2 == 0:
    if n <= 5 and n >= 2:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")


def is_leap(year):
    leap = False
    
    if year % 4 == 0 and year % 400 == 0:
        leap = True
    elif year % 4 == 0:
        leap = True

    return leap

print(is_leap(2100))

def str_cat(number):
    string = ''
    for i in range(1,n+2):
        string = string + str(i)
    return string

print(str_cat(5))