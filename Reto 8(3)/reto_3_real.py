import json
from funciones import *        
if __name__ == "__main__": 
   print("bienvenido a tu futuro restaurante")
   ceo = Manager(input("ingresa tu nombre: "), float(input("ingresa el capital inicial para el negocio (es recomendable tener al menos 600000)")))
   print("este es su menu")
   # se muestar un menu por defecto
   print(ceo.ver_menu())
   if (input("¿desea añadir mas productos? (si/no): ")) == "si":
      nu = float(input("¿cuantos productos desea añadir?: "))
      #añadir productos tiene su respectivo costo
      ceo.añadir_productos(nu)
   final_menu = ceo.menu
   print("ahora es necesario contratar empleados")
   ceo.contratar() #contratar empleados cuesta dinero, para que funcion es necesario al menos tener un mesero y un cajero 
   trabajadores = ceo.empleados
   print("tus trabajadores son: ")
   for i in trabajadores:
      print(i)
   print("ahora empezemos a trabajar")
   comensales = random.randint(1,10) #una cantidad aleatoria de comensales para cada mesero
   flag = 0
   ordenes_tomadas = []
   medios_de_pago = []
   for i in trabajadores:
         if isinstance(i,mesero):
             while flag < comensales:
               ran_num = random.randint(0,100)
               if ran_num < 50:
                  medio_comensal_random = Efectivo(random.randint(10000,1000000))
               elif ran_num >= 50:
                  medio_comensal_random = Tarjeta(random.randint(10000, 1000000), random.randbytes(7))
               print(f"comensal {flag + 1}")
               i.añadir_orden(final_menu[0],final_menu[1],final_menu[2],final_menu[3],final_menu[4])
               #las ordenes añadidas seran almacenadas en una cola
               flag = flag +1
               ordenes_tomadas.append(i)
               medios_de_pago.append(medio_comensal_random)
               #las colas seran añadidas a una lista
         if isinstance(i, cajero):
            cont = 0
            if ordenes_tomadas == []:
               print(f"por el momento no hay cuentas que {i._nombre} pueda hacer")
               trabajadores.append(i)
               pass  
            else:
               # el cajero ira encargandose de las ordenes y realizando el cobro respectivo
               for j in ordenes_tomadas: 
                  ganacia = i.cuentas(j,medios_de_pago[cont])
                  cont=cont +1 
                  ceo.balance = ceo.balance + ganacia