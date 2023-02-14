#################################################################################
#                                                                               #
#    Create an algorithm that reads a number and outputs its double, triple,    #
# and square root.                                                              #
#                                                                               #
#################################################################################

n = float(input('Enter an integer: '))
print('The double of {} is {}'.format(n, (n*2)))
print('The triple of {} is {}'.format(n, (n*3)))
print('The root of {} is {:.2f}'.format(n, (n**0.5)))
