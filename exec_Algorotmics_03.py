def make_list(number):
    names = []
    for item in number: # Aqui esta el error
        names.append(input("Enter your name with a capital letter: "))
    print(names)

number =  int(input("How many names needs to be entere: "))
names =  make_list(number) # Aqui esta el segundo error
for name in names: 
    if name [1] == "A":
        print("Name", name," Start with A")
        