# Mesa de partes digital - prototipo simple
# Solo recibe solicitudes y las muestra. No asigna código, área ni estado.
# Los datos se guardan en listas (arreglos) y se pierden al cerrar el programa.

MAX = 100
TIPOS = ["Carta de presentación", "Justificación por enfermedad"]

nombres = []
dnis = []
telefonos = []
correos = []
postulantes = []
tipos = []
asuntos = []


def titulo():
    print("****************************")
    print("Mesa de partes digital")
    print("Colegio Italiano Antonio Raimondi")
    print("****************************")


def pedir_texto(mensaje):
    # Repite la pregunta hasta que el campo no esté vacío.
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Error: este campo es obligatorio.")


def pedir_dni():
    # El DNI debe tener exactamente 8 dígitos.
    while True:
        dni = input("DNI (8 dígitos): ").strip()
        if len(dni) == 8 and dni.isascii() and dni.isdigit():
            return dni
        print("Error: el DNI debe tener exactamente 8 dígitos.")


def pedir_tipo():
    print("Tipo de documento:")
    for i in range(len(TIPOS)):
        print("[" + str(i + 1) + "] " + TIPOS[i])
    while True:
        opcion = input("Elegir tipo: ").strip()
        if opcion.isdigit() and 1 <= int(opcion) <= len(TIPOS):
            return TIPOS[int(opcion) - 1]
        print("Error: elegir un número entre 1 y " + str(len(TIPOS)) + ".")


def registrar_solicitud():
    print("***** REGISTRAR SOLICITUD *****")
    if len(nombres) >= MAX:
        print("Llegamos a la capacidad máxima.")
        return False
    nombres.append(pedir_texto("Nombres y apellidos: "))
    dnis.append(pedir_dni())
    telefonos.append(pedir_texto("Teléfono: "))
    correos.append(pedir_texto("Correo electrónico: "))
    postulantes.append(pedir_texto("Nombre del postulante: "))
    tipos.append(pedir_tipo())
    asuntos.append(pedir_texto("Asunto: "))
    return True


def mostrar():
    print("***** SOLICITUDES RECIBIDAS *****")
    if len(nombres) == 0:
        print("No hay solicitudes por mostrar.")
        return
    for i in range(len(nombres)):
        print(str(i + 1) + ".- " + nombres[i] + " | DNI: " + dnis[i])
        print("     Teléfono: " + telefonos[i] + " | Correo: " + correos[i])
        print("     Postulante: " + postulantes[i])
        print("     Documento: " + tipos[i])
        print("     Asunto: " + asuntos[i])
    print("Total: " + str(len(nombres)))


def pausar():
    input("\nPresiona Enter para volver al menú...")


def main():
    opc = 0
    while opc != 3:
        titulo()
        print("*****MENU PRINCIPAL*****")
        print("[1] Registrar solicitud")
        print("[2] Mostrar solicitudes recibidas")
        print("[3] Salir")
        texto = input("Ingresar opción: ").strip()
        if not texto.isdigit():
            print("Error, debe ingresar un valor numérico.")
            continue
        opc = int(texto)
        if opc < 1 or opc > 3:
            print("Error, opción fuera de rango [1-3].")
            continue
        if opc == 1:
            if registrar_solicitud():
                print("\nSolicitud recibida correctamente.")
            pausar()
        elif opc == 2:
            mostrar()
            pausar()
        else:
            print("Gracias por usar el sistema.")


if __name__ == "__main__":
    main()