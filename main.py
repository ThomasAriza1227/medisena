from src.cita import CitaMedica
from src.gestion_datos import cargar_citas, guardar_citas


def listar_citas(citas: list):
    if not citas:
        print("\nNo hay citas registradas.")
        return
    print("\n--- LISTA DE CITAS MÉDICAS ---")
    for c in citas:
        tipo = "Urgencia" if c["es_urgencia"] else "Programada"
        print(
            f"ID: {c['id_cita']} | Paciente: {c['paciente']} | Especialidad: {c['especialidad']} | Médico: {c['medico_asignado']} | Tipo: {tipo} | Costo Final: ${c['costo_final']}"
        )


def registrar_cita(citas: list):
    print("\n--- REGISTRAR NUEVA CITA ---")
    id_cita = input("Ingrese ID de la cita (ej: CIT-2026-01): ").strip()

    if any(c["id_cita"] == id_cita for c in citas):
        print("Error: Ya existe una cita registrada con ese ID.")
        return

    paciente = input("Nombre completo del paciente: ").strip()
    especialidad = input("Especialidad médica: ").strip()
    medico_asignado = input("Nombre del médico asignado: ").strip()

    try:
        costo_consulta = float(input("Costo de la consulta: "))
    except ValueError:
        print("Error: El costo debe ser un número válido.")
        return

    urgencia_input = input("¿Es urgencia? (s/n): ").strip().lower()
    es_urgencia = True if urgencia_input == "s" else False

    nueva_cita = CitaMedica(
        id_cita, paciente, especialidad, medico_asignado, costo_consulta, es_urgencia
    )
    citas.append(nueva_cita.a_diccionario())
    guardar_citas(citas)
    print("Cita registrada exitosamente.")


def consultar_ingresos(citas: list):
    total = sum(c["costo_final"] for c in citas)
    print(f"\nTotal de ingresos proyectados: ${total}")


def main():
    citas = cargar_citas()
    while True:
        print("\n=== SISTEMA MEDISENA ===")
        print("1. Listar citas")
        print("2. Registrar nueva cita")
        print("3. Consultar total de ingresos proyectados")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            listar_citas(citas)
        elif opcion == "2":
            registrar_cita(citas)
        elif opcion == "3":
            consultar_ingresos(citas)
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
