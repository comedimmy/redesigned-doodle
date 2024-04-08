amount=1
count=0
i=1
j=1

while i<=10:
    print(i) 
    
    amount *=i    
    
    count+=amount
    
    i+=1  
print("10!=",amount,"\n1+2!+3!+.....10!=",count)
