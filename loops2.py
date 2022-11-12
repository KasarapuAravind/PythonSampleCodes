sum = 0
for i in range(1, 101):
    sum = sum + i

print(sum)

total = 0
for num in range(1,101):
    if num % 2 == 0:
        total += num
print(total)


for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
