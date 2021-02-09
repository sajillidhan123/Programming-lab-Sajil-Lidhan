a=int(input("Enter  the final year"))
i=2021
while i<=a:
    flag=0
    while(i%100==0 and i%100==0 or i%4==0):
        flag=1
        break
    if(flag==1):
        print(i)
    i=i+1