#2. uzdevums
n = int(input("ievadi skaitli:"))
summa= 0
for i in range (1,1 + n):
        summa += i
print("skaitļu summa no 1 līdz n ir:", summa)

#1 uzdevums

n = int(input("ievadi skaitli:"))
faktorials = 1
for i in range (1,1 + n):
  faktorials *= i

print("skaitļu faktorials no 1 līdz n ir:", faktorials)

#6. uzdevums
import random

min_skaitlis = 1
max_skaitlis = 100
iedomata_skaitlis = random.randint(min_skaitlis,max_skaitlis)
print(f"Ludzu uzminet skaitli intervala no {min_skaitlis}")
minesanas_reizes = 0
while True:
    lietotaja_ievade = int(input("levadi savu minējumu:"))
    minesanas_reizes += 1
    if lietotaja_ievade < iedomata_skaitlis:
            print("Lielaks!")
    elif lietotaja_ievade < iedomata_skaitlis:
        print( "Mazāks!")
    else:
            print(f"Uzminets! Skaitlis ir {iedomata_skaitlis}.")
            break
print(f"Skatijãt minesanu {minesanas_reizes} reizes.")
#4 uzdevums
n = int(input("ievadi skakitli"))
