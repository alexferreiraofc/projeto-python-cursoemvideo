frase = 'Curso em vídeo'
print(frase.count('o'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.lower().find('curso'))

#_________________________________________________
#USANDO SPLIT

frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido)

#os COLCHETES DETERMINAM

print(dividido[2])          #<------ ELE MOSTRA APENAS O [2] segundo CONJUNTO DE PALAVRAS DO COLCHETES
print(dividido[2][3]) # <-- ELE VAI PEGAR O CONJUNTO [2] no PRIMEIRO COLCHETES E MOSTRAR APENAS A [3] letra da STRING
