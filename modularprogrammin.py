'''
parts of function :
1) function declaration / function signature 
2) function body 
3) function call 

# function categories 
1) fucntion with no argument / parameter and no return type
2) fucntion with argument / parameter and  return type
3) fucntion with no argument / parameter BUT return type
4) fucntion with  argument / parameter BUT  no return type


-- paramters :  variable / data passed during function declaration 
 types :
 1) formal paramter
 : values . variables they are created / use / define during the function declaration 
 2) actual paramter 
 : values . variables they are created / use / define inside the driveer code . mainly in the function call 

 THE VALUE OF FORMAL PARAMTER REFLECTS TO THE VALUE OF ACTUAL PARAMETER ..


-- arguments : variable /data passed during the function call 



'''
# def show(username):   # function declaration
#     return username  # function body 


# # driver code :
# print(show("mk")) # function call 

'''
task 01 : program to  write all the logical op using function
task 02 : program to write function categories 3, 4 

'''
def max (a, b ):  # formal 
    if a>b :
        return a
    else:
        return b 

x=int(input(" enter a number ?"))
y=int(input(" enter anu number again ?"))
print(max(x,y ))  # actual parametr  
