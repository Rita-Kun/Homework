a=input()
b=input()
a=int(str(a),2)
b=int(str(b),2)
print(bin(a+b)[2:])


alp=[' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=int(input())
num1=num//26
num2=num%26
print(str(alp[num1])+str(alp[num2]))