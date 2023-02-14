#################################################################################
#                                                                               #
#    Faça um programa que leia um número inteiro e mostre na tela sua tabuada de#
# 1 até 10.                                                                      #
#                                                                               #
#################################################################################

n = int(input('Digite um número inteiro: '))

for i in range(1,11):
    print('{} x {} = {}'.format(n, i, n*i))