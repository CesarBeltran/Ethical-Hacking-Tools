import hashlib


def crack_password(hash_to_crack):
    with open("passwords.txt", "r") as file:
        for line in file:
            password = line.strip()
            hashed_password = hashlib.sha1(password.encode()).hexdigest()
            if hashed_password == hash_to_crack:
                return password
    return None

# Ejemplo de uso

hash_to_check = "8cb2237d0679ca88db6464eac60da96345513964"

#hash_to_check = "de68a951c1586debd9031e55c96f667072382937"
cracked_password = crack_password(hash_to_check)

if cracked_password:
    print(f"Contraseña encontrada: {cracked_password}")
else:
    print("Contraseña no encontrada en el diccionario.")
