text="1 lakshn 1 0 1 0 01"
count_1=0
count_0=0
for words in text:
    for word in words:
        if word=='1':
            count_1+=1
        elif word=='0':
            count_0+=1

if count_1==count_0:
    print("Same count")
else:
    print("Not Same")
            
