# Importo la libreria sys para recoger argumentos y, en este caso, tambien para
# poder utilizar la funcion exit() para terminar el programa.
import sys

# Variable donde se van a guardar todos los argumentos que se pasen.
arg = ""
# Variable donde se guardara la cadena swapeada y ledia al reves.
text = ""
if len(sys.argv) == 1:  # Si no se pasan argumentos
	# sys.stdout.write("")  # Igual que un print pero en la misma linea de la consola.
	sys.exit()  # Termina el programa.
else:
	"""
	PRIMER BUCLE:
		Desde el primer argumento (0 no porque que seria el nombre
		del archivo) hasta el final del array de argumentos, guarda
		el contenido del array en la variable arg
	SEGUNDO BUCLE:
		Desde el final de la cadena argv, hasta el principio quitando
		el espacio (1) y yendo desde atras hacia delante (-1),
		guarda en la variable text el contenido de arg mientras que
		intercambias la mayuscula por la minuscula y viceversa.
	"""
	for j in range(1, len(sys.argv)):
		arg += " " + sys.argv[j]
	for i in range(len(arg), 1, -1):
		text += arg[i - 1].swapcase()
	# Finalmente, imprimimos el resultado final.
	print(text)
