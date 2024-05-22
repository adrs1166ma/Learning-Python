from zPracicar.persona import Persona




registros = [(1, 'Ana', 'Marin', 'ana@gmail.com'), (2, 'Karla', 'Gomez', 'kgomez@mail.com')]
p = []
for registro in registros:
   persona = Persona(registro[0], registro[1], registro[2], registro[3])
   p.append(persona)

for per in p:
    print(per)



