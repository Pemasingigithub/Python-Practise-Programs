def factorial(user):
   fact=1

   for i in range(1, user+1):
        fact = fact * i
   print(fact)
user = int(input("Enter number:"))
factorial(user)






