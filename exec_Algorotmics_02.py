from this import d


n = int(input("Numero de personas: "))
players = {}
    
for i in range(n):
    name = input("Nombre: ")
    size = input("Talla: ")    
    players[name]= size

name = input("Ingresa el nombre de la persona: ")
if name in players:
    print(players[name])
else:
    print("No Existe dicha persona")
