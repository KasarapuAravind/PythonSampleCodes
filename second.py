fname = input("enter your name")
sname = input("enter your crush name")
print("ye")

fullname = fname + sname
print(fullname)
tcount = fullname.lower().count("t")
rcount = fullname.lower().count("r")
ucount = fullname.lower().count("u")
ecount = fullname.lower().count("e")

truecount = sum([tcount,rcount,ucount,ecount])

lcount = fullname.lower().count("l")
ocount = fullname.lower().count("o")
vcount = fullname.lower().count("v")
lovecount = sum([lcount,ocount,vcount,ecount])
print(f"the love percentage for you both is {truecount}{lovecount}%")