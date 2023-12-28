import numpy as np 





n = 6
m = 100
numberOfStreaks = 0 
for i in range(0,10000):
    a = np.random.randint(0,2,m)
    #a = np.random.randchoice(['1','0'],size=100)
    b = a.astype(str)
    b = "".join(a.astype(str))
    if "0"*n  in b or "1"*n in b:
            numberOfStreaks+=1
print('Chance of streak: %s%%' % (numberOfStreaks / m))
    


def create_transition_matrix(n):
    a = np.array([])
    for i in range(n):
        b = np.zeros(n)
        if i == n-1:
            b[i] = 1
        else:
            b[0] = 1/2
            b[i+1] = 1/2
        a = np.concatenate((a,b))
    b = a.reshape(n,n)
    return b


print(create_transition_matrix(n))
result = np.linalg.matrix_power(create_transition_matrix(n),m-1)
#print(result)
print(result[0][n-1])
print('sucess')

a= np.array([
    [.5,.5,0,0,0,0],
    [.5,0,.5,0,0,0],
    [.5,0,0,.5,0,0],
    [.5,0,0,0,.5,0],
    [.5,0,0,0,0,.5],
    [0 ,0,0,0,0,1]])
# print(a)


result = np.linalg.matrix_power(a, 99)
# print(result)
# print(result[0][5])



