import random
coin=['H','T']
x=random.choice(coin)

 
p1=input("choose to flip or keep:")
p2=input("choose to flip or keep:")
print("random no.",x)
if p1=='flip':
   if x=='H':
     x = 'T'
   else:
     x = 'H'
if p2=='flip':
   if x=='H':
     x = 'T'
   else:
     x = 'H'
if x=='H':
   print("p1 wins")
else:
   print("p2 wins")