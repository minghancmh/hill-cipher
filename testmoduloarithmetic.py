#imports
import numpy as np

#find modulo inverse of number
#n is the number
#m is the modulo
def moduloinverse(n,m):
    multiples = []
    modulos = []
    for i in range(1,100):
        multiples.append(n*i)
        modulos.append(m*i+1)

    
    for number in multiples:
        for item in modulos:
            if number == item:
                return number/n

#find equivalence of number modulo
#n is the number
#m is the modulo
def equivalence(n,m):
    while np.abs(n)>m:
        if n>0:
            n-=m
        elif n<0:
            n+=m
        else:
            n=0
    if n<0:
        n+=m
    return n


#find determinant of 2x2
def determinant_2(x):
    #takes 2x2 numpy array
    a = x[0,0]
    b = x[0,1]
    c = x[1,0]
    d = x[1,1]
    determinant = a*d-b*c
    return determinant

def determinant_3(x):
    #takes 3x3 numpy array
    a = x[0,0]
    b = x[0,1]
    c = x[0,2]
    d = x[1,0]
    e = x[1,1]
    f = x[1,2]
    g = x[2,0]
    h = x[2,1]
    i = x[2,2]
    determinant = a*e*i+b*f*g+c*d*h - g*e*c-h*f*a-i*d*b
    return determinant
    



# print(moduloinverse(equivalence(determinant_2(np.array([[9,4],[5,7]])),26),26))

def two_by_two_inverse(x,m):
    #x is a numpy array, ie your matrix
    #store variables
    a = x[0,0]
    b = x[0,1]
    c = x[1,0]
    d = x[1,1]
    #redefine matrix to swop positions
    y = np.array([[d,-b],[-c,a]])

    
    inv_matrix = y*moduloinverse(equivalence(determinant_2(x),m),m)
    a = inv_matrix[0,0]
    b = inv_matrix[0,1]
    c = inv_matrix[1,0]
    d = inv_matrix[1,1]
    lowest_form_inverse = np.array([[equivalence(a,m),equivalence(b,m)],[equivalence(c,m),equivalence(d,m)]])
    return lowest_form_inverse

#testcase
x = np.array([[7,11],[8,11]])

inv = two_by_two_inverse(x,26)

res = np.array([[9,10] , [18,21]])
k = res@inv%26

hill = np.array([[7,11] , [8,11]])

kinv = two_by_two_inverse(k,26)

message = np.array([[9,10,20,2,19,2,19,7,20,19,5,1,23,17,22,10,7,11,25,8,17,5,4,14], [18,21,8,1,23,10,10,0,9,23,7,24,6,7,0,1,22,3,14,23,3,12,22,6]])

# print(k@hill%26)

print(kinv)
print(kinv@message%26)


#3x3 inverse
def three_by_three_inverse(x,m):
    #x is a numpy array, ie your matrix
    #store variables
    a = x[0,0]
    b = x[0,1]
    c = x[0,2]
    d = x[1,0]
    e = x[1,1]
    f = x[1,2]
    g = x[2,0]
    h = x[2,1]
    i = x[2,2]
    #redefine matrix to swop positions
    a1 = e*i-h*f
    b1 = d*i-g*f
    c1 = d*h-g*e
    d1 = b*i-h*c
    e1 = a*i-g*c
    f1 = a*h-g*b
    g1 = b*f-e*c
    h1 = a*f-d*c
    i1 = a*e-d*b
    y = np.array([[a1,d1,g1],[b1,e1,h1],[c1,f1,i1]])

    #apply cofactor theorem
    inv_matrix = y*moduloinverse(equivalence(determinant_3(x),m),m)
    a = inv_matrix[0,0]
    b = -1*inv_matrix[0,1]
    c = inv_matrix[0,2]
    d = -1*inv_matrix[1,0]
    e = inv_matrix[1,1]
    f = -1*inv_matrix[1,2]
    g = inv_matrix[2,0]
    h = -1*inv_matrix[2,1]
    i = inv_matrix[2,2]
    lowest_form_inverse = np.array([[equivalence(a,m), equivalence(b,m), equivalence(c,m)],
    [equivalence(d,m), equivalence(e,m), equivalence(f,m)],
    [equivalence(g,m), equivalence(h,m), equivalence(i,m)]])
    return lowest_form_inverse

#testcase
# K = np.array([[1,0,12],
# [25,2,1],
# [0,1,1]])

# K_1 = np.array([[1,4,0] , [1,1,0] , [1,1,3]])
# Kinv = three_by_three_inverse(K_1,26)
# P = np.array([[0,21] , [10,14] , [9,0]])
# # print(Kinv@P%26)
# P_2 = np.array([[14,7,2] , [6,7,7] , [6,2,7]])
# # print(Kinv@P_2%26)
# P_3 = np.array([[4,22,2,4,10] , [10,12,0,17,14] , [23,24,17,16,11]])
# # print(Kinv@P_3%26)

# P4 = np.array([[22,3,20] , [22,17,7] , [16,12,11]])
# print(Kinv@P4%26)


#gives result similar to anders one, but all numbers positive, note that they are equivalent, ie 19 equivalent to -7 mod 26
# Kinv = three_by_three_inverse(K,26)

#check
# print(K@Kinv%26)

# P = np.array([[22,11],[0,0],[7,20]])

# print(K@P)
# print(K@P%26)

# newkinv = np.array([[a,b] , [c,d]])
# test = np.array([[9,10] , [18,21]])

# a=0
# b=0
# c=0
# d=0






                    


