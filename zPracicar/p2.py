s = 'SELECT * FROM persona WHERE id_persona id_persona IN %s'

entrada = input('pon los id a buscar (por comas)')
pk = (tuple(entrada.split(',')),)

print(s, pk)