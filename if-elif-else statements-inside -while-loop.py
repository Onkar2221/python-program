# z = 0

# while  z < 5 :
#     if z == 0 :
#         print("z is" , z)
#     elif z == 1:
#         print("z is" , z)
#     elif z == 2 :
#         print("z is" , z)
#     else:
#         print(z)

# output == z is 0 print infinte time



z = 0

while  z < 5 :
    if z == 0 :
        print("z is" , z)
        z = z + 1
    elif z == 1:
        print("z is" , z)
        z = z + 1
    elif z == 2 :
        print("z is" , z)
        z = z + 1
    else:
        print(z)

# output == 
        # z is 0
        # z is 1
        # z is 2
        # 3
        # 3
        # 3
        # 3 infinite time
