# Define a list of name
names = names = ["Mohammad","Medhat","Wasef","Ramadan"]

print(f"first name is {names[0]} and the last name is {names[-1]}")

names.append("Ouglo")
print("appended name is :  "+names[-1])

names.sort()
print(f"names after sort is:   {names}")
# print(f"names after sort is:   "+names)
# TypeError: can only concatenate str (not "list") to str