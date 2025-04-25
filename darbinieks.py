# darbinieks.py



class Darbinieks:

# Klases mainīgais ID inkrementam

  _id_counter = 1



def __init__(self, vards, uzvards, alga):

 self.name = vards

 self.surname = uzvards

 self.salary = alga

 self.id = Darbinieks._id_counter

Darbinieks._id_counter += 1



def increase_salary(self, procenti):

 self.salary += self.salary * (procenti / 100)



def decrease_salary(self, procenti):

 self.salary -= self.salary * (procenti / 100)



def __str__(self):

 return f"{self.id}-{self.name}-{self.surname}"



