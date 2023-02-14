#################################################################################
#                                                                               #
#    Write a program that reads a whole number and displays its table from 1 to #
# 10 on the screen.                                                             #
#                                                                               #
#################################################################################

n = int(input('Enter an integer: '))

for i in range(1,11):
    print('{} x {} = {}'.format(n, i, n*i))