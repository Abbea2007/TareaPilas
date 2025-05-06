from banco import Bancos

def mostrar_menu():
    print("\n------MENU DEL BANCO--------")
    print("1. Llegada del cliente")
    print("2. Atender al cliente")
    print("3. Mostrar clientes en memoria")
    print("4. Salir")


def main():
    banco = Bancos()
    while True: 
        mostrar_menu()
        opcion = input("Selecciona ina opcion: ")

        if opcion =="1":
            nombre = input("Ingrese el nombre del cliente:  ")
            banco.llega_cliente(nombre)
        elif opcion == "2":
            banco.atender_cliente()
        elif opcion == "3":
          clientes = banco.obtener_clientes_en_espera()
          if clientes: 
              print("Clientes en espera: ", ", ".join(clientes))
          else:
              print("No hay clientes en espera.")
              break
        elif opcion == "4":
            print("Gracias por isar el sistema del banco.")
            break
        else: 
            print("Opcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    main()


            