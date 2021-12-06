
def noteikt_diapazonu(d1, d2, sk):
  rezultats = 'Skaitlis nav diapazona!'
  if d1>=sk>=d2:
    rezultats = 'Skaitlis ir diapazona!'
  return rezultats 
  
  
  
  
d1  = int(input('Ievadi diapazona sakumu:'))
d2 = int(input('Ievadi diapazona beigas:'))
sk = int(input('Ievadi skaitli:'))
rez = noteikt_diapazonu(d1, d2, sk)
print(rez)