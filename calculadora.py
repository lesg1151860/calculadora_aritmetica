def suma(a, b):
  """
  Función para sumar dos números.

  Parámetros:
    a (float): Primer número.
    b (float): Segundo número.

  Retorno:
    float: La suma de a y b.
  """
  return a + b

def resta(a, b):
  """
  Función para restar dos números.

  Parámetros:
    a (float): Primer número.
    b (float): Segundo número.

  Retorno:
    float: La resta de a y b.
  """
  return a - b

def multiplicacion(a, b):
  """
  Función para multiplicar dos números.

  Parámetros:
    a (float): Primer número.
    b (float): Segundo número.

  Retorno:
    float: La multiplicación de a y b.
  """
  return a * b

def division(a, b):
  """
  Función para dividir dos números.

  Parámetros:
    a (float): Primer número.
    b (float): Segundo número.

  Retorno:
    float: La división de a y b.
  """
  if b == 0:
    print("ADVERTENCIA : No es posible dividir por cero :C).")
    return None
  return a / b

def main():
  """
  Función principal que ejecuta la calculadora.
  """
  while True:
    # Mostrar menú de opciones
    print("Calculadora Aritmética LESG")
    print("Opción 1 => Suma")
    print("Opción 2 => Resta")
    print("Opción 3 => Multiplicación")
    print("Opción 4 => División")
    print("Opción 5 => Salir")

    # Solicitar opción al usuario
    opcion = int(input("Por favor seleccione una opción: "))

    # Validar opción y realizar la operación
    if opcion == 1:
      a = float(input("Por favor ingrese el primer número: "))
      b = float(input("Por favor ingrese el segundo número: "))
      resultado = suma(a, b)
      print(f"La suma de {a} y {b} es: {resultado}")
    elif opcion == 2:
      a = float(input("Por favor ingrese el primer número: "))
      b = float(input("Por favor ingrese el segundo número: "))
      resultado = resta(a, b)
      print(f"La resta de {a} y {b} es: {resultado}")
    elif opcion == 3:
      a = float(input("Por favor ingrese el primer número: "))
      b = float(input("Por favor ingrese el segundo número: "))
      resultado = multiplicacion(a, b)
      print(f"La multiplicación de {a} y {b} es: {resultado}")
    elif opcion == 4:
      a = float(input("Ingrese el primer número: "))
      b = float(input("Ingrese el segundo número: "))
      resultado = division(a, b)
      if resultado is not None:
        print(f"La división de {a} y {b} es: {resultado}")
    elif opcion == 5:
      print("¡Nos vemos en una próxima :) !")
      break
    else:
      print("Opción no válida. Por favor intente de nuevo.")

if __name__ == "__main__":
  main()
