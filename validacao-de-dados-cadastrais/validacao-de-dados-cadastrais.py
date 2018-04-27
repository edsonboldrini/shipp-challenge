import sys

arrayNumber = []

fileTest = open(sys.argv[1], "r")
cpf = fileTest.readline()

for i in range(len(cpf)-2):
  print(cpf[i])
  arrayNumber.append(cpf[i]*10-i)