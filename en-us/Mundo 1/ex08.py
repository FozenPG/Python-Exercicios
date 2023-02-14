#################################################################################
#                                                                               #
#    Write an algorithm that reads a value in meters and displays it converted  #
# to centimeters and millimeters.                                               #
#                                                                               #
#################################################################################

n = float(input('Enter a measurement in meters: '))
print('{:.2f}m equals {:.2f}cm'.format(n, n*100))
print('{:.2f}m equals {:.2f}mm'.format(n, n*1000))