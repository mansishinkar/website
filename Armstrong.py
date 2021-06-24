num=int(input("Enter the number"))
order=len(str(num))
sum=0
temp=num
while temp>0:
    r=temp%10
    sum+=r**order
    temp=temp//10

if num==sum:
    print(num,"number is armstrong")
else:
    print(num,"number is not armstrong")
