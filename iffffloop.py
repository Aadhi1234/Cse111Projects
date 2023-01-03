a = int(input("number: "))
if n%5==0 and n%10==0:
   print(n,"is divisible by both 5 and 10")
if n%5==0 or n%10==0:
   print(n,"is divisble by either 5 or 10")
else:
    print(n,"is not divisible by 5 and 10")
