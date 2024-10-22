productos = []

# Función para cargar los datos desde el archivo productos.txt
def cargar_datos():
    try:
        archivo = open("productos.txt", "r")
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            productos.append({"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)})
        archivo.close()
    except:
        print("No se pudo cargar el archivo o no existe.")

# Función para guardar los datos en productos.txt
def guardar_datos():
    archivo = open("productos.txt", "w")
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    archivo.close()
    print("Datos guardados.")

# Función para añadir un nuevo producto
def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    precio = input("Introduce el precio del producto: ")
    cantidad = input("Introduce la cantidad del producto: ")
    
    producto = {"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)}
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

            nuevo_precio = input("Nuevo precio (o presiona Enter para no cambiar): ")
            if nuevo_precio:
                producto["precio"] = float(nuevo_precio)

            nueva_cantidad = input("Nueva cantidad (o presiona Enter para no cambiar): ")
            if nueva_cantidad:
                producto["cantidad"] = int(nueva_cantidad)

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
