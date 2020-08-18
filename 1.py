sum=0
count=0
number=int(input("введите число 0 -завершить"))
while number !=0:
    sum=sum+number
    count=count+1
    number=int(input("введите число 0 -завершить"))
print(sum/count)
