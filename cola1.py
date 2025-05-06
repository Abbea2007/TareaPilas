from collections import deque

#Crear una cola de clientes

cola = deque()

#Anadir elementos a la cola

cola.append("Cliente-001")
cola.append("Cliente-002")
cola.append("Cliente-003")
cola.append("Cliente-004")
cola.append("Cliente-005")

#Mostrar en la cola

print("Cola de clientes:")
for cliente in cola:
    print(cliente)

#Eliminar el primer cliente de la cola

print("\Atendiendo al primer cliente...")
cliente_atendido = cola.popleft()
print(f"Cliente atendido: {cliente_atendido}")

#Mostrar la cola despues de atender el primr cliente

print("\Cola de clientes despues de atender el primer cliente")
for cliente in cola: 
    print(cliente)

    