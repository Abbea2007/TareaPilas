from models.urna import UrnaDigital
from controllers import gestion

def mostrar_menu():
    print("\n=== Menú del Sistema de Registro de Votos ===")
    print("1. Registrar un voto")
    print("2. Eliminar el último voto")
    print("3. Mostrar el último voto")
    print("4. Mostrar todos los votos")
    print("5. Salir")

def main():
    print("¡Bienvenido al sistema de registro de votos para elecciones estudiantiles!")
    urna = UrnaDigital()

    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de opción: ").strip()

        if opcion == "1":
            voto = input("Ingrese el nombre del votante: ").strip()
            gestion.registrar_voto(urna, voto)

        elif opcion == "2":
            gestion.eliminar_ultimo_voto(urna)

        elif opcion == "3":
            gestion.mostrar_ultimo_voto(urna)

        elif opcion == "4":
            gestion.mostrar_todos_votos(urna)

        elif opcion == "5":
            print("👋 Saliendo del sistema. ¡Gracias por usar el registro de votos!")
            break

        else:
            print(" Opción inválida. Por favor, ingrese un número del 1 al 5.")

if __name__ == "__main__":
    main()
