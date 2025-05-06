# main.py

from models.urna import UrnaDigital
from controllers.gestion import registrar_voto, eliminar_ultimo_voto, mostrar_ultimo_voto, mostrar_todos_votos
from templates import mensajes

def main():
    print(mensajes.MENSAJE_BIENVENIDA)
    urna = UrnaDigital()

    while True:
        print(mensajes.MENSAJE_MENU)
        opcion = input("Ingrese el número de opción: ").strip()

        if opcion == "1":
            voto = input("Ingrese el nombre del votante: ").strip()
            registrar_voto(urna, voto)
        elif opcion == "2":
            eliminar_ultimo_voto(urna)
        elif opcion == "3":
            mostrar_ultimo_voto(urna)
        elif opcion == "4":
            mostrar_todos_votos(urna)
        elif opcion == "5":
            print(mensajes.MENSAJE_SALIR)
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
