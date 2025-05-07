def registrar_voto(urna, voto):
    urna.registrar_voto(voto)
    print(f"Voto registrado exitosamente: '{voto}'.")

def eliminar_ultimo_voto(urna):
    eliminado = urna.eliminar_ultimo_voto()
    if eliminado:
        print(f"Último voto eliminado: '{eliminado}'.")
    else:
        print("La urna está vacía. No hay votos para eliminar.")

def mostrar_ultimo_voto(urna):
    ultimo = urna.ultimo_voto()
    if ultimo:
        print(f"El último voto registrado es: '{ultimo}'.")
    else:
        print("La urna está vacía.")

def mostrar_todos_votos(urna):
    votos = urna.mostrar_todos_votos()
    if votos:
        print("Lista de todos los votos registrados:")
        for i, voto in enumerate(votos, 1):
            print(f"{i}. {voto}")
    else:
        print("La urna está vacía. No hay votos registrados.")
