#################################################################################
#                                                                               #
#    Write a program that reads something from the keyboard and displays its    #
# primitive type and all possible information about it on the screen.           #
#                                                                               #
#################################################################################

args = input('Digite algo: ')
print('Just spaces? {}'.format(args.isspace()))
print('Is number? {}'.format(args.isnumeric()))
print('Is alphabetical? {}'.format(args.isalpha()))
print('Is alphanumeric? {}'.format(args.isalnum()))
print('Is uppercase? {}'.format(args.isupper()))
print('Is lowercase? {}'.format(args.islower()))
print('Is capitalized? {}'.format(args.istitle()))