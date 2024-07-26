import sys
import json

def main():
    if len(sys.argv) != 2:
        print("Uso: python mayor_a.py <umbral>")
        sys.exit(1)

    try:
        umbral = int(sys.argv[1])
    except ValueError:
        print("El umbral debe ser un número entero.")
        sys.exit(1)

    with open('ventas.json', 'r') as file:
        datos = json.load(file)

    filtrados = {mes: valor for mes, valor in datos.items() if valor > umbral}
    print(filtrados)

if __name__ == "__main__":
    main()