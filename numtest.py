num = input("enter any number")
newstr=''
for i in range(0, int(num) + 1, 2):
   newstr += str(i)+','

print(newstr.rstrip('20'))

