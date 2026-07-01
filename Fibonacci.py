# Fibonacci sequence up to n-th term
# Fibonacci numbers form a recursive sequence where each 
#   number is the sum of the two preceding ones, starting with 0 and 1

nth_terms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nth_terms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nth_terms == 1:
   print("Fibonacci sequence up to ",nth_terms,": ")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence: ")
   while count < nth_terms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1