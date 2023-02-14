#################################################################################
#                                                                               #
#    Create a program that reads how much money a person has and shows how many #
# euros he can buy.                                                             #
#    Consider that 1€ = US$0.93                                                 #
#                                                                               #
#################################################################################

n = float(input('How much money do you have: '))
print('With US${:.2f} you can buy {:.2f}€'.format(n, (n/0.93) ))