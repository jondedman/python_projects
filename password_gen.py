import random
import string

alphabet = list(string.printable) #other methods available wold allow me a more customisable solution where i could
#then concatentate the iteratin over each. But this is a quick and straighforward solution.

# print(alphabet)

password = ""
for i in range(16):
    password+= random.choice(alphabet)

print(password)
