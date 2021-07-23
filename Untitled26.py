#Write a program that reads numbers from the console (one per line) until the sum of the numbers entered equals 0 and immediately after that prints the 
#sum of the squares of all the numbers read.
#It is guaranteed that at some point the sum of the entered numbers will be equal to 0, after which there is no need to continue reading.
#In the example, we read the numbers 1, -3, 5, -6, -10, 13; at this moment we notice that the sum of these numbers is equal to zero and we display 
#the sum of their squares, not paying attention to the fact that there are still unread values.


sum1, z, h=0, int(input()), []
h.append(z)
while z!=0:
    a=int(input())
    h.append(a)
    z+=a
    if z==0:
        break
for pug in h:
    sum1+=pug**2
print(sum1)

