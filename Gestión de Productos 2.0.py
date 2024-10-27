productos = []

# Función para cargar los datos desde el archivo productos.txt
def cargar_datos():
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append({"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)})
    except FileNotFoundError:
        print("Archivo no encontrado. Se creará uno nuevo al guardar los datos.")
    except ValueError:
        print("Error en el formato del archivo. Verifique que los datos estén en el formato correcto.")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")

# Función para guardar los datos en productos.txt
def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados.")

# Función para añadir un nuevo producto
def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break
        except ValueError:
            print("Error: el precio debe ser un valor numérico.")

    while True:
        try:
            cantidad = int(input("Introduce la cantidad del producto: "))
            break
        except ValueError:
            print("Error: la cantidad debe ser un valor entero.")

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(producto)
    print("Producto añadido.")

# Función para ver todos los productos
def ver_productos():
    if len(productos) == 0:
        print("No hay productos disponibles.")
    else:
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

# Función para actualizar un producto
def actualizar_producto():
    ver_productos()
    nombre_producto = input("Introduce el nombre del producto que deseas actualizar: ")

    for producto in productos:
        if producto["nombre"] == nombre_producto:
            print("Producto encontrado.")
            nuevo_nombre = input("Nuevo nombre (o presiona Enter para no cambiar): ")
            if nuevo_nombre:
                producto["nombre"] = nuevo_nombre

            while True:
                nuevo_precio = input("Nuevo precio (o presiona Enter para no cambiar): ")
                if nuevo_precio:
                    try:
                        producto["precio"] = float(nuevo_precio)
                        break
                    except ValueError:
                        print("Error: el precio debe ser un valor numérico.")
                else:
                    break

            while True:
                nueva_cantidad = input("Nueva cantidad (o presiona Enter para no cambiar): ")
                if nueva_cantidad:
                    try:
                        producto["cantidad"] = int(nueva_cantidad)
                        break
                    except ValueError:
                        print("Error: la cantidad debe ser un valor entero.")
                else:
                    break

            print("Producto actualizado.")
            return
    print("Producto no encontrado.")

# Función para eliminar un producto
def eliminar_producto():
    ver_productos()
    nombre_producto = input("Introduce el nombre del producto que deseas eliminar: ")

    for producto in productos:
        if producto["nombre"] == nombre_producto:
            productos.remove(producto)
            print("Producto eliminado.")
            return
    print("Producto no encontrado.")

# Menú del sistema
def menu():
    cargar_datos()
    while True:
        print("\n--- Menú de Gestión de Productos ---")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el menú
menu()
