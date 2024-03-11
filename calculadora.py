def main():
  """
  Función principal que ejecuta la calculadora.
  """
  while True:
    # Mostrar menú de opciones
    print("Calculadora Arit´metica LESG")
    print("Opción 1 => Suma")
    print("Opción 2 => Resta")
    print("Opción 3 => Multiplicación")
    print("Opción 4 => División")
    print("Opción 5 => Salir")

    # Solicitar opción al usuario
    opcion = int(input("Seleccione una opción: "))

    # Validar opción y realizar la operación
    if opcion == 1:
      a = float(input("Ingrese el primer número: "))
      b = float(input("Ingrese el segundo número: "))
      resultado = suma(a, b)
      print(f"La suma de {a} y {b} es: {resultado}")
    elif opcion == 2:
      a = float(input("Ingrese el primer número: "))
      b = float(input("Ingrese el segundo número: "))
      resultado = resta(a, b)
      print(f"La resta de {a} y {b} es: {resultado}")
    elif opcion == 3:
      a = float(input("Ingrese el primer número: "))
      b = float(input("Ingrese el segundo número: "))
      resultado = multiplicacion(a, b)
      print(f"La multiplicación de {a} y {b} es: {resultado}")
    elif opcion == 4:
      a = float(input("Ingrese el primer número: "))
      b = float(input("Ingrese el segundo número: "))
      resultado = division(a, b)
      if resultado is not None:
        print(f"La división de {a} y {b} es: {resultado}")
    elif opcion == 5:
      print("¡Hasta luego!")
      break
    else:
      print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
  main()