# Ejercicio 1: Factorial de un número

def factorial(n):
    # Escriba su codigo acontinuacion
   if n==0 or n==1:
    return 1
   else:
     return n* factorial(n-1)
