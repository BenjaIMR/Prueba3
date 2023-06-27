import Medina_Benjamin_PGY_1121_P3_008D as fn
import time
import os

while True:
      os.system("cls")
      print("""\tBienvenido a Mascotas Segura\n
      1. Grabar
      2. Buscar
      3. Retirarse
      4. Salir\n""")
      
      
      opcion = fn.validar_opcion() 
      if opcion ==1:
         rut = fn.validar_rut()
         nombre = fn.validar_nombre()
         mascota = fn.validar_nom_mascota()
         cantidad = fn.validar_cantidad()
         print("REGISTRADO CORRECTAMENTE!")
         time.sleep(3)


      elif opcion ==2:
         rut = validar_rut()
         if validar_rut in lista_ruts:
            break
         habitacion = validar_habitacion()
         numero = int(input("Ingrese el número de habitacion"))

      elif opcion ==3:
         pass
      else:
         print("Gracias por su visita a Mascota Segura")
        