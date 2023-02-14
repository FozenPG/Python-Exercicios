#################################################################################
#                                                                               #
#    Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo    #
# primitivo e todas as informações possíveis sobre ela.                         #
#                                                                               #
#################################################################################

args = input('Digite algo: ')
print('Só tem espaços? {}'.format(args.isspace()))
print('É um número? {}'.format(args.isnumeric()))
print('É alfabético? {}'.format(args.isalpha()))
print('É alfanumérico? {}'.format(args.isalnum()))
print('Está em maiusculas? {}'.format(args.isupper()))
print('Está em minusculas? {}'.format(args.islower()))
print('Está capitalizada? {}'.format(args.istitle()))