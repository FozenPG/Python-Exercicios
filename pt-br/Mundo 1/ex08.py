#################################################################################
#                                                                               #
#    Escreva um algoritmo que leia um valor em metros e o exiba convertido em  #
# centímetros e milímetros.                                                     #
#                                                                               #
#################################################################################

n = float(input('Digite uma medida em metros: '))
print('{:.2f}m equivale a {:.2f}cm'.format(n, n*100))
print('{:.2f}m equivale a {:.2f}mm'.format(n, n*1000))