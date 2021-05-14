import random
list1 = (random.sample((1,2,3,4,5,6,7,8,9),4))
tries = 0
while tries<5:
    x = list(input())
    korova = 0
    for i in x:
        num = int(i)
        if num in list1:
            korova+=1
    count = 0
    for index, i in enumerate(x):
        x[index] = int(i)
        if x[index] == list1[index]:
            count+=1
    korova2 = korova - count
    if count == 4:
        print("byk:",count)
    else:
        print("korova:",korova2,'byk:',count)
    tries+=1
    if count == 4 and korova == 4:
        print("congrats, you win")
        break

print(list1)