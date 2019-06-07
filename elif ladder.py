
# coding: utf-8

# In[7]:


s1 = int(input("enter s1 marks: "))
s2 = int(input("enter s2 marks: "))
s3 = int(input("enter s3 marks: "))
s4 = int(input("enter s4 marks: "))
s5 = int(input("enter s5 marks: "))
g_m = s1+s2+s3+s4+s5
avg = g_m/500
per = avg*100
if (per > 70):
    print("A")
elif(per > 60):
    print("B")
elif(per > 40):
    print("C")
else:
    print("Better luck next time")

