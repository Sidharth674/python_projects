import random
import string

vals = (string.ascii_letters + string.punctuation + string.digits)

password = ("")
pass_len = int(input("Enter the length of password you want to get:  "))

for i in range(pass_len):
    password += (random.choice(vals))
        
print("Your password is" , password)