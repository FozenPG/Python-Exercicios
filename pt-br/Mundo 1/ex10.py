#################################################################################
#                                                                               #
#    Crie um programa que leia quanto dinheiro uma pessoa tem e mostre quantos  #
# euros ele pode comprar.                                                       #
#    Considere que 1€ = R$5.58                                                  #
#                                                                               #
#################################################################################

n = float(input('Quanto dinheiro voce tem: '))
print('com R${:.2f} você pode comprar {:.2f}€'.format(n, (n/5.58) ))