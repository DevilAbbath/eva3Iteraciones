def yesno(question):
    while True:
        answer = input(question + " (Si/No): ").lower()
        if answer in ["si", "no"]:
            return answer
        else:
            print("Respuesta no válida. Por favor, responde 'Si' o 'No'.")

def main():
    stimuli = yesno("¿Responde a Estímulos?")
    if stimuli == "si":
        print("Valorar la necesidad de llevarlo al hospital más cercano")
        print("Fin")
    else:
        breath = yesno("¿Respira?")
        if breath == "si":
            print("Permitirle posición de suficiente ventilación")
            print("Fin")
        else:
            print("Administrar 5 Ventilaciones y llamar a Ambulancia")

            while True:
                lifesigns = yesno("¿Signos de Vida?")
                if lifesigns == "si":
                    print("Reevaluar a la espera de la Ambulancia")
                else:
                    print("Administrar Compresiones Torácicas hasta que llegue la ambulancia")

                ambulance = yesno("¿Llego la Ambulancia?")
                if ambulance == "si":
                    print("Fin")
                    break

if __name__ == "__main__":
    main()
