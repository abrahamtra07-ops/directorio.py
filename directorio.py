def mostrar_menu():
    print("\n--- Directorio de la Unidad de Investigación ---")
    print("1. Agregar o actualizar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Buscar un contacto")
    print("4. Eliminar un contacto")
    print("5. Salir")

def principal():
    # Creación de la colección de datos (diccionario)
    contactos_unidad = {}

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción del menú (1-5): ")

        if opcion == '1':
            # Funcionalidad para insertar/agregar datos
            nombre = input("Ingresa el nombre del investigador o contacto: ")
            telefono = input("Ingresa el número telefónico: ")
            contactos_unidad[nombre] = telefono
            print(f"✅ Contacto '{nombre}' registrado exitosamente.")

        elif opcion == '2':
            # Mostrar de forma clara la información almacenada
            if not contactos_unidad:
                print("⚠️ El directorio está vacío.")
            else:
                print("\n--- Lista de Contactos Activos ---")
                # Operación adicional: Recorrer elementos
                for nombre, telefono in contactos_unidad.items():
                    print(f"👤 Nombre: {nombre} | 📞 Teléfono: {telefono}")

        elif opcion == '3':
            # Operación básica adicional: Buscar
            nombre = input("Ingresa el nombre del contacto que deseas buscar: ")
            if nombre in contactos_unidad:
                print(f"🔍 El teléfono de {nombre} es: {contactos_unidad[nombre]}")
            else:
                print("❌ Contacto no encontrado en la base de datos.")

        elif opcion == '4':
            # Operación básica adicional: Eliminar
            nombre = input("Ingresa el nombre del contacto a eliminar: ")
            if nombre in contactos_unidad:
                del contactos_unidad[nombre]
                print(f"🗑️ Contacto '{nombre}' eliminado del sistema.")
            else:
                print("❌ Contacto no encontrado.")

        elif opcion == '5':
            print("Saliendo del sistema del directorio...")
            break
        else:
            print("⚠️ Opción no válida. Por favor, selecciona un número del 1 al 5.")

if __name__ == "__main__":
    principal()
