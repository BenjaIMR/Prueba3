import os
import numpy

lista_nombres = []
lista_ruts = []

Guarderia_mascota = numpy.zeros((2,6)int)

while True:
   print("""\tBienvenido a Mascotas Segura\n
   1. Grabar
   2. Buscar
   3. Retirarse
   4. Salir""")

   def validar_opcion():
     try:
       opcion = int(input("Ingrese opción: "))
       if opcion in (1,2,3,4):
        return opcion
       else:
           print("ERROR! OPCION NO VALIDA")  
     except:
        print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO")

   def validar_rut():
      try: 
       rut = int(input("Ingrese Rut(sin puntos ni dígito verificador): "))
       if rut>= 7 and rut<=8:
          return rut
       else:
          print("ERROR! DEBE CONTENER ENTRE 7 Y 8 DIGITOS")
      except:
         print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO")    