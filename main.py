def oddeven(a):
  if a%2==0:
      print (a,"it is a even")
  else:
      print (a,"it is a odd")
def prime (a):
  if a%2!=0:
   if a%3!=0:
       if a%5!=0:
           if a%7!=0:
               print (a,"it is a prime")
  else:
      print(a,"it is a even")

a=int(input("enter "))
c=(input("choice odd or prime"))

if c=="odd":
    print (oddeven(a))
elif c=="prime":
    print (prime(a))


