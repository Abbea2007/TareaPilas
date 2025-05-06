# Controllers/gestion.py

from templates import mensajes

def registrar_voto(urna, voto):
    urna.registrar_voto(voto)
    print(f"{mensajes.MENSAJE_VOTO_REGISTRADO} Voto: '{voto}'.")

def eliminar_ultimo_voto(urna):
    eliminado = urna.eliminar_ultimo_voto()
    if eliminado:
        print(f"{mensajes.MENSAJE_VOTO_ELIMINADO} Voto eliminado: '{eliminado}'.")
    else:
        print(mensajes.MENSAJE_URNA_VACIA)

def mostrar_ultimo_voto(urna):
    ultimo = urna.ultimo_voto()
    if ultimo:
        print(f"{mensajes.MENSAJE_ULTIMO_VOTO} '{ultimo}'.")
    else:
        print(mensajes.MENSAJE_URNA_VACIA)

def mostrar_todos_votos(urna):
    votos = urna.mostrar_todos_votos()
    if votos:
        print("Votos en la urna:", votos)
    else:
        print(mensajes.MENSAJE_URNA_VACIA)
