from clases.vehiculo import Vehiculo, Coche, Moto


def mostrar_menu():
    """Imprime las opciones del menú principal."""
    print("\n========================================")
    print("🚗 SISTEMA DE GESTIÓN DE VEHÍCULOS 🏍️")
    print("========================================")
    print("1. Registrar coche")
    print("2. Registrar moto")
    print("3. Mostrar flota")
    print("4. Encender/Apagar vehículo")
    print("5. Calcular alquiler")
    print("6. Alquilar vehículo")
    print("7. Devolver vehículo")
    print("8. Ver estadísticas")
    print("9. Dar de baja vehículo")
    print("10. Salir")
    print("========================================")


def solicitar_datos_basicos():
    """Solicita y valida marca, modelo, año y precio base."""
    marca = input("Ingrese la marca: ").strip()
    modelo = input("Ingrese el modelo: ").strip()

    if not marca or not modelo:
        raise ValueError("La marca y el modelo no pueden estar vacíos.")

    try:
        año = int(input("Ingrese el año de fabricación: "))
    except ValueError:
        raise ValueError("El año debe ser un número entero.")

    if not Vehiculo.validar_año(año):
        raise ValueError("Año inválido. Debe ser mayor a 1900 y menor o igual al año actual.")

    try:
        precio_base = float(input("Ingrese el precio base: "))
    except ValueError:
        raise ValueError("El precio debe ser un número decimal o entero.")

    if not Vehiculo.validar_precio(precio_base):
        raise ValueError("El precio base debe ser estrictamente positivo.")

    return marca, modelo, año, precio_base


def seleccionar_vehiculo(flota: list) -> int:
    """Solicita la selección de un vehículo por su índice y valida que esté en rango."""
    if not flota:
        print("⚠️ No hay vehículos en la flota.")
        return -1

    print("\n--- Lista de Vehículos ---")
    for idx, v in enumerate(flota):
        print(f"[{idx}] {v.marca} {v.modelo} ({'Coche' if isinstance(v, Coche) else 'Moto'})")

    try:
        indice = int(input("Seleccione el índice del vehículo: "))
        if indice < 0 or indice >= len(flota):
            raise IndexError("Índice fuera de rango. Seleccione un número de la lista.")
        return indice
    except ValueError:
        raise ValueError("Debe ingresar un número entero válido para el índice.")


def main():
    flota = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                print("\n--- REGISTRAR COCHE ---")
                marca, modelo, año, precio_base = solicitar_datos_basicos()
                puertas = int(input("Ingrese el número de puertas: "))
                if puertas <= 0:
                    raise ValueError("El número de puertas debe ser mayor a cero.")

                coche = Coche(marca, modelo, año, precio_base, puertas)
                flota.append(coche)

            elif opcion == "2":
                print("\n--- REGISTRAR MOTO ---")
                marca, modelo, año, precio_base = solicitar_datos_basicos()
                cilindrada = int(input("Ingrese la cilindrada (cc): "))
                if cilindrada <= 0:
                    raise ValueError("La cilindrada debe ser mayor a cero.")

                moto = Moto(marca, modelo, año, precio_base, cilindrada)
                flota.append(moto)

            elif opcion == "3":
                print("\n--- MOSTRAR FLOTA ---")
                if not flota:
                    print("⚠️ La flota se encuentra vacía.")
                else:
                    for idx, v in enumerate(flota):
                        print(f"\nID [{idx}]:")
                        v.mostrar_info()

            elif opcion == "4":
                print("\n--- ENCENDER/APAGAR VEHÍCULO ---")
                idx = seleccionar_vehiculo(flota)
                if idx != -1:
                    vehiculo = flota[idx]
                    accion = input("¿Desea (E)ncender o (A)pagar el motor?: ").strip().upper()
                    if accion == "E":
                        vehiculo.encender()
                    elif accion == "A":
                        vehiculo.apagar()
                    else:
                        print("⚠️ Opción de motor no válida. Use 'E' o 'A'.")

            elif opcion == "5":
                print("\n--- CALCULAR ALQUILER ---")
                idx = seleccionar_vehiculo(flota)
                if idx != -1:
                    vehiculo = flota[idx]
                    if not vehiculo.disponible:
                        raise ValueError("No se puede calcular el alquiler de un vehículo que no está disponible (alquilado).")

                    if isinstance(vehiculo, Coche):
                        tiempo = float(input("Ingrese la cantidad de días de alquiler: "))
                        if tiempo <= 0:
                            raise ValueError("Los días deben ser mayores a cero.")
                        costo = vehiculo.calcular_alquiler(tiempo)
                        print(f"💰 Costo total por {tiempo} día(s): ${costo:.2f}")

                    elif isinstance(vehiculo, Moto):
                        tiempo = float(input("Ingrese la cantidad de horas de alquiler: "))
                        if tiempo <= 0:
                            raise ValueError("Las horas deben ser mayores a cero.")
                        costo = vehiculo.calcular_alquiler(tiempo)
                        print(f"💰 Costo total por {tiempo} hora(s): ${costo:.2f}")

            elif opcion == "6":
                print("\n--- ALQUILAR VEHÍCULO ---")
                idx = seleccionar_vehiculo(flota)
                if idx != -1:
                    flota[idx].alquilar()

            elif opcion == "7":
                print("\n--- DEVOLVER VEHÍCULO ---")
                idx = seleccionar_vehiculo(flota)
                if idx != -1:
                    flota[idx].devolver()

            elif opcion == "8":
                print("\n--- ESTADÍSTICAS DE LA FLOTA ---")
                total_activos = Vehiculo.total_vehiculos()
                encendidos = sum(1 for v in flota if v.encendido)
                coches = sum(1 for v in flota if isinstance(v, Coche))
                motos = sum(1 for v in flota if isinstance(v, Moto))

                print(f"Total de vehículos registrados (contador activo): {total_activos}")
                print(f"Vehículos actualmente encendidos: {encendidos}")
                print(f"Cantidad de coches: {coches}")
                print(f"Cantidad de motos: {motos}")

            elif opcion == "9":
                print("\n--- DAR DE BAJA VEHÍCULO ---")
                idx = seleccionar_vehiculo(flota)
                if idx != -1:
                    vehiculo_eliminado = flota.pop(idx)
                    del vehiculo_eliminado

            elif opcion == "10":
                print("\n🏁 Saliendo del sistema de gestión. ¡Hasta luego!")
                break

            else:
                print("⚠️️ Opción no válida. Por favor, seleccione un número del 1 al 10.")

        except (ValueError, IndexError) as err:
            print(f"❌ Error: {err}")
        except Exception as err:
            print(f"❌ Ocurrió un error inesperado: {err}")


if __name__ == "__main__":
    main()
