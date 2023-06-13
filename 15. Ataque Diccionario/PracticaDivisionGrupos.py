##################################################
####   💻  Práctica: Dividir en grupos  💻  #####
##################################################

## 👇 Escriba su código DEBAJO de esta línea 👇 ##


# Reciba n y x de la entrada con la función 'input'. 
# No olvide convertir las cadenas en números con 'int'.

n=int(input())
x=int(input())

# Calcula el número de grupos de tamaño x que se pueden formar.

g=n//x


# Calcula el número de estudiantes sobrantes asignados a la calificación.
# (Este número debe ser menor que x)
NC=n%x



# Calcula el número de reportes entregados por los estudiantes.

R=NC*g


# Imprime en la salida el número correspondiente para las preguntas del enunciado.

print(g)
print(R)