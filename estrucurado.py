nombre_estudiante = input("Ingrese su Nombre: ")
apellido_studiante = input("Ingrese su Apellido: ")
cedula = int(input("Ingrese su Número de cedula: "))
semestre = int(input("Ingese el numero del semestre que cursa\n Ej: '1' : "))
escrito = True
cancelar = True
numero_carrera = 0
while numero_carrera <= 0 or numero_carrera >= 4:
  numero_carrera = int(
    input(
      "--Eliga su carrera--\n 1:Derecho Constitucional\n 2:Ciencias de la computación\n 3:Diseño de moda\n\n"
    ))
materias_inscritas = []
materias_derecho = [
  "Teoría del Poder", "Teoría del Estado", "Teoría de la Constitución",
  "Teoría de los derechos humanos", "Fuentes del derecho constitucional",
  "División de poderes", "Control de constitucionalidad"
]
materias_diseno_moda = [
  "Historia de la Moda", "Dibujo de Moda", "Patronaje y Confección",
  "Tecnología Textil", "Diseño de Accesorios", "Tendencias de Moda",
  "Marketing y Comunicación en Moda"
]

materias_ciencias_computacion = [
  "Introducción a la Programación", "Estructuras de Datos", "Algoritmos",
  "Bases de Datos", "Inteligencia Artificial", "Redes de Computadoras",
  "Seguridad Informática"
]
materias_todas = [
  materias_derecho, materias_ciencias_computacion, materias_diseno_moda
]

salir = True

while salir:
  inscribir = int(
    input(
      "\nDigite '1' si quiere incribir sus materias\n\n Digite '0' si quiere cancelar alguna materia\n\n: "
    ))

  if inscribir == 1:
    while escrito:
      if numero_carrera == 1:
        print("Escribe tus materias de Derecho Constitucional\n")
      elif numero_carrera == 2:
        print("Escribe tus materias de Ciencias de la computación\n")
      elif numero_carrera == 3:
        print("Escribe tus materias de Diseño de moda\n")

      materia_seleccionada = materias_todas[numero_carrera - 1]
      for materia in materia_seleccionada:
        print((materia_seleccionada.index(materia)) + 1, ":", materia)

      materia_ins = int(input("Materia a Inscribir: "))
      materias_inscritas.append(materia_seleccionada[materia_ins - 1])
      materia_seleccionada.remove(materia_seleccionada[materia_ins - 1])
      print(f"\nTienes {len(materias_inscritas)}  materias inscritas")
      escrito = int(
        input(
          "\nDigite '1' si quiere seguir con la incripción de materias\n\n Digite '0' si quiere terminar aqui\n\n : "
        ))
  else:
    while cancelar:
      if len(materias_inscritas) == 0:
        print("No tienes materia disponibles para cancelar")
        cancelar = False
      else:
        for materia in materias_inscritas:
          print((materias_inscritas.index(materia)) + 1, ":", materia)
        materia_ins = int(input("Materia a Cancelar: "))
        materia_seleccionada.append(materias_inscritas[materia_ins - 1])
        materias_inscritas.remove(materias_inscritas[materia_ins - 1])
        cancelar = int(
          input(
            "\nDigite '1' si quiere seguir con la cancelación de materias\n\n Digite '0' si quiere terminar aqui\n\n : "
          ))
    cancelar = True
  salir = int(
    input(
      "\nDigite '1' para volver al menu principal\n\n Digite '0' para salir\n\n : "
    ))

print("--Tus materias incritas son: --")
for materia in materias_inscritas:
  print((materias_inscritas.index(materia)) + 1, ":", materia)
