


from tokenize import String


d = [60 ,65 ,70 ,75,80]
for i in d:
    x = ((i*1.6)+(i*1.25*1.6)+(i*1.25*1.25*1.6))
    s = str(x)
    print(s + ",", end = '')