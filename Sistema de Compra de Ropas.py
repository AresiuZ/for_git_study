# Clase base Prenda con encapsulamiento
class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre  # Atributo público
        self.precio = precio  # Atributo público
        self.cantidad = cantidad  # Atributo público

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.cantidad}")

    def reducir_stock(self, cantidad_vendida):
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
            print(f"Stock de {self.nombre} actualizado a {self.cantidad}")
        else:
            print(f"No hay suficiente stock de {self.nombre}")

# Clase RopaHombre que hereda de Prenda
class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")

# Clase RopaMujer que hereda de Prenda
class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")

# Clase Inventario que abstrae el manejo de prendas
class Inventario:
    def __init__(self):
        self.prendas = []

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

    def mostrar_inventario(self):
        print("Inventario de Tienda:")
        for prenda in self.prendas:
            prenda.mostrar_info()

    def buscar_prenda(self, nombre):
        for prenda in self.prendas:
            if prenda.nombre.lower() == nombre.lower():
                return prenda
        return None

# Clase Tienda para procesar las compras
class Tienda:
    def __init__(self, inventario):
        self.inventario = inventario

    def comprar_prenda(self, nombre, cantidad):
        prenda = self.inventario.buscar_prenda(nombre)
        if prenda:
            if prenda.cantidad >= cantidad:
                prenda.reducir_stock(cantidad)
                total = prenda.precio * cantidad
                print(f"Compra exitosa. Total a pagar: ${total}")
            else:
                print(f"No hay suficiente stock para {cantidad} de {nombre}")
        else:
            print(f"El artículo {nombre} no está en el inventario.")

# Ejemplos de artículos de ropa
camisa = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
pantalon = RopaHombre("Pantalón de Hombre", 30.00, 30, "L")
chaqueta = RopaHombre("Chaqueta de Hombre", 55.00, 20, "XL")
falda = RopaMujer("Falda de Mujer", 28.00, 15, "S")
blusa = RopaMujer("Blusa de Mujer", 22.00, 40, "M")
vestido = RopaMujer("Vestido de Mujer", 45.00, 10, "L")
zapatos_hombre = RopaHombre("Zapatos de Hombre", 60.00, 25, "42")
zapatos_mujer = RopaMujer("Zapatos de Mujer", 50.00, 20, "38")

# Crear el inventario y agregar los productos
inventario = Inventario()
inventario.agregar_prenda(camisa)
inventario.agregar_prenda(pantalon)
inventario.agregar_prenda(chaqueta)
inventario.agregar_prenda(falda)
inventario.agregar_prenda(blusa)
inventario.agregar_prenda(vestido)
inventario.agregar_prenda(zapatos_hombre)
inventario.agregar_prenda(zapatos_mujer)

# Crear la tienda y mostrar inventario
tienda = Tienda(inventario)
inventario.mostrar_inventario()

# Simulación de compra
print("\nProceso de Compra:")
tienda.comprar_prenda("Camisa de Hombre", 2)
tienda.comprar_prenda("Falda de Mujer", 1)
tienda.comprar_prenda("Vestido de Mujer", 5)
