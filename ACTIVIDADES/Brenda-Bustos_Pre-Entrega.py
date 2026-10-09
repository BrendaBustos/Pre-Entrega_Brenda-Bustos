# Ejercicio 1: presentar un producto
# Escribí un programa que:
# 1. Pida el nombre de un producto.
# 2. Pida su categoría.
# 3. Pida su precio.
# 4. Muestre una ficha como esta:
# Producto: Cuaderno
# Categoría: Librería
# Precio: $2500

productos = []

while True:
    print("\n--- MENÚ DE PRODUCTOS ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Elegí una opción: ").strip()

    # 1. AGREGAR
    if opcion == "1":
        nombre = input("Nombre: ").strip()
        categoria = input("Categoría: ").strip()
        precio_texto = input("Precio (número entero): $").strip()

        if nombre == "" or categoria == "" or precio_texto == "":
            print("Error: no puede haber datos vacíos")
            continue

        if not precio_texto.isdigit():
            print("Error: el precio debe contener solo números")
            continue

        precio = int(precio_texto)

        if precio <= 0:
            print("Error: el precio debe ser mayor que cero")
            continue

        print(f"\nProducto: {nombre} | Categoría: {categoria} | Precio: ${precio}")
        confirma = input("¿Confirmás agregar este producto? (si/no): ").strip().lower()

        if confirma == "si":
            producto = [nombre, categoria, precio]
            productos.append(producto)
            print("Producto agregado")
        else:
            print("Se canceló la carga")

    # 2. MOSTRAR
    elif opcion == "2":
            if len(productos) == 0:
                print("No hay productos cargados")
            else:
                print("\n--- PRODUCTOS ---")
    
                for i in range(len(productos)):
                    producto = productos[i]
                    print(
                        f"{i + 1}. Nombre: {producto[0]} | "
                        f"Categoría: {producto[1]} | "
                        f"Precio: ${producto[2]}"
                    )

    # 3. BUSCAR
    elif opcion == "3":
            buscado = input("Nombre a buscar: ").strip().lower()
    
            if buscado == "":
                print("Error: ingresá un nombre para buscar")
                continue
    
            encontrado = False
    
            for producto in productos:
                if buscado in producto[0].lower():
                    print(
                        f"Nombre: {producto[0]} | "
                        f"Categoría: {producto[1]} | "
                        f"Precio: ${producto[2]}"
                    )
                    encontrado = True
    
            if not encontrado:
                print("No se encontraron productos")

    # 4. ELIMINAR
    elif opcion == "4":
        if len(productos) == 0:
            print("No hay productos para eliminar")
            continue

        print("\n--- PRODUCTOS ---")
        for i in range(len(productos)):
            producto = productos[i]
            print(f"{i + 1}. {producto[0]}")

        numero_texto = input("Número del producto a eliminar: ").strip()

        if not numero_texto.isdigit():
            print("Error: ingresá un número")
            continue

        numero = int(numero_texto)

        if numero < 1 or numero > len(productos):
            print("Error: número fuera de la lista")
            continue

        nombre_elegido = productos[numero - 1][0]
        confirma = input(
            f"¿Confirmás eliminar '{nombre_elegido}'? (si/no): "
        ).strip().lower()

        if confirma == "si":
            productos.pop(numero - 1)
            print("Producto eliminado")
        else:
            print("Eliminación cancelada")

    # 5. SALIR
    elif opcion == "5":
        confirma = input("¿Confirmás que querés salir? (si/no): ").strip().lower()

        if confirma == "si":
            print("Fin del programa")
            break
        else:
            print("Seguís en el programa")

    else:
        print("Opción inválida")