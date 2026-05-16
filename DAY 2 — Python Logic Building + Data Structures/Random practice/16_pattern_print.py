# Print this patterns:
# *
# **
# ***
# ****
# *****
# ******
# *******

#        *
#       **
#      ***
#     ****
#    *****
#   ******
#  *******

#        *
#       ***
#      *****
#     *******
#    *********
#   ***********
#  *************

rows = int(input("Enter number of rows: "))

for i in range(rows):
    print("*"*i) #left
    # print(" "*(rows-i)+ "*"*i) #right
    # print(" "*(rows-i) + "*"*(2*i-1)) #pyramid