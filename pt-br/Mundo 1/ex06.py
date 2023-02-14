#################################################################################
#                                                                               #
#    Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz  #
# quadrada.                                                                     #
#                                                                               #
#################################################################################

n = float(input('Digite um número: '))
print('O dobro de {} é {}'.format(n, (n*2)))
print('O triplo de {} é {}'.format(n, (n*3)))
print('A raiz de {} é {:.2f}'.format(n, (n**0.5)))
