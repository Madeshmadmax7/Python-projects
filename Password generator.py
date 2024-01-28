import random

uppercharacters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercharacters="abcdefghijklmnopqrstuvwxyz"
numbers="1234567890"
specialcharacters="@#$!%&"
while True:
    word=uppercharacters + lowercharacters + specialcharacters + numbers
    i=int(input("Enter the length of the Password : "))
    password="".join(random.sample(word,i))
    print("The password is ",password)
