import hashlib
import timeit

def crack_password(hash_to_crack):
    with open("Passwords.txt", "r") as file:
        for line in file:
            password = line.strip()
            hashed_password = hashlib.sha1(password.encode()).hexdigest()
            if hashed_password == hash_to_crack:
                return password
    return None

# Función auxiliar para medir el tiempo de ejecución
def measure_time():
    hash_to_check = "de68a951c1586debd9031e55c96f667072382937"
    cracked_password = crack_password(hash_to_check)
    if cracked_password:
        print(f"Contraseña encontrada: {cracked_password}")
    else:
        print("Contraseña no encontrada en el diccionario.")

# Medir el tiempo de ejecución
execution_time = timeit.timeit(measure_time, number=1)

# Imprimir el tiempo de ejecución
print(f"Tiempo de ejecución: {execution_time:.5f} segundos")
