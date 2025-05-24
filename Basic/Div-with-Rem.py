# Q.Write a program where the user is asked to enter two integers (divisor and dividend) 
# and the quotient and the remainder of their division is computed.(Both divisor and dividend should be integers.)

dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))
print("Quotient:", dividend // divisor)
print("Remainder:", dividend % divisor)
