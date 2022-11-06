#TharukDamsilu Re-submit the task...
import random
import string

char = int(input('Enter the password lenght (Ex: 12): '))

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers   = string.digits
symbols   = string.punctuation

all = lowercase + uppercase + numbers + symbols

x = random.sample(all, char)
password = "".join(x)
print(password)