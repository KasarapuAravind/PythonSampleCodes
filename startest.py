
for row in range(0,5):
    for col in range(0,5):
        print('* ', end = ' ')
    print("\n")


# *  *  *  *  *  

# *  *  *  *  *

# *  *  *  *  *

# *  *  *  *  *

# *  *  *  *  *

for row in range(0,5):
    for col in range(0, row + 1):
        print('*',end = ' ')
    print()


# *  

# *  *  

# *  *  * 

# *  *  *  *  

# *  *  *  *  *

n=5
for i in range(0,n):
    for j in range(0, n-i-1):
        print(end=" ")
    for j in range(i + 1):
        print("*", end = ' ')
    print()

#      *   6
 
#     *  *  5

#    *  *  *  4

#   *  *  *  *  3

#  *  *  *  *  *  2



#  *  *  *  *  *
#    *  *  *  
