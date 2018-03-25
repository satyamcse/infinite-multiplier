no1=[]
no2=[]
result=[]
x=raw_input("Enter I number: ")
for i in x:
    no1.append(int(i))
x=raw_input("Enter II number: ")
for i in x:
    no2.append(int(i))
for i in range(0,len(no1)+len(no2)):
    result.append(0)
j=-1
times=-len(no1)
for i in range(0,len(no2)):
    p=i
    k=-1
    while k>=times:
        mul=no2[j]*no1[k]
        result[p]+=mul
        if result[p]>=10:
            temp=result [p]
            result[p]=temp%10
            result[p+1]+=temp/10
        k-=1
        p+=1
    j-=1
x=""
result.reverse()
for i in result:
    x+=str(i)
print "Result = "+x
