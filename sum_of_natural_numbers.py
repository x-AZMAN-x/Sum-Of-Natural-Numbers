#Sum Of Natural Numbers
num = int(input("Please Enter The Number Till What You Want To Sum The Numbers: "))
sum = 0
i=0
while(i<=num):
    sum += i
    i+=1
    
print(f"Sum Of First {num} Natural Numbers Are: {sum}")