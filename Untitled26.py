#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

