name = input("inter your name please:")
name = "Mohammad Wasef Ramadan"
print(f"Hello {name}, nice to meet you")

n = int(input("Input a number, please:"))
if n>0:
    print(f"{n} is positive")
elif n<0:
    print(f"{n} is negative")
else:
    print(f"{n} is equal to zero")

s = set()
s.add(1)
lstNames = ["Mohammad","wasef","Ramadan"]
print(f"The set have {len(s)} elements, and the string have {len(name)} character, and the list have {len(lstNames)} elements")
