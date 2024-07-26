from string import ascii_lowercase
import getpass

pwd = getpass.getpass("Ingresa la contraseña: ").lower()

if "ñ" not in pwd:
    c = 0
    letters = list(pwd)
    characters = list(ascii_lowercase)
    
    for letter in letters:
        if letter in characters:
            c += characters.index(letter) + 1

    print (f'La contraseña fue forzada en {c} intentos')

else:

    print ("Contraseña no Valida")
    print ('La contraseña no debe incluir la letra "Ñ"\n')