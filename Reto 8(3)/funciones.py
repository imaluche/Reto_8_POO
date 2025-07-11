import json
import random
from collections import namedtuple
from queue import Queue
# clases de empleados, medios de pago y productos
class producto:
 def __init__(self, nombre, precio): #lo mas elemental
    self._nombre = nombre
    self._precio = precio
    self._tipo = "producto"
 def get_nombre(self):
    return self._nombre
 def get_precio(self):
    return self._precio
 def get_tipo(self):
    return self._tipo
 def __str__(self):
    return f"{self._nombre} - {self._precio} ({self._tipo})"
 
class sopas(producto): #las sopas son un producto
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self._tipo = "sopa"
    def __str__(self):
       return f"{self._nombre} - {self._precio} ({self._tipo})"
class ensaladas(producto): #las ensaladas son un producto
    def __init__(self, nombre, precio, p:bool=False): #indiciador de poder llevar vinagreta
        super().__init__(nombre, precio)
        self._tipo = "ensalada"
        self.p = p
    def vinagreta(self, b:bool = False):
       if (self.p == False):
          print("esa ensalada no lleva vinagreta")
       if (b == False):
         print("sin vinagreta")
       if (b == True) and (self.p == True):
         print("con vinagreta")
         self._precio= self._precio + 50
    def __str__(self):
      return f"{self._nombre} - {self._precio} ({self._tipo})"
class bebidas(producto): #las bebidas son un producto
    def __init__(self, nombre, precio, jugo:bool = False):
        self.jugo = jugo
        super().__init__(nombre, precio)
        self._tipo = "bebida"
    def azucar(self, b:bool = False):
               if self.jugo == True:
                  if b == False:
                     print("sin azucar")
                  else:
                     self._precio = self._precio + 50
               else:
                  print("esa bebida no lleva azucar")
    def hielo(self, b:bool = False):
       if b == False:
         print("sin hielo")
       else:
         self._precio = self._precio+50
    def __str__(self):
      return f"{self._nombre} - {self._precio} ({self._tipo})"
class platocentral(producto): #los platos centrales son un producto
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self._tipo = "plato central"
    def __str__(self):
      return f"{self._nombre} - {self._precio} ({self._tipo})"
class postres(producto): #los postres son un producto
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self._tipo = "postre"
    def __str__(self):
      return f"{self._nombre} - {self._precio} ({self._tipo})"
#clases de personas que manejan el restaurante
class Manager:
   def __init__(self, nombre: str = "N/A", balance: float = 0.0, empleados: list =[]):
      self.nombre = nombre
      self.balance = balance
      lectura = (open("menu.json", "r"))
      self.jsonmenu = json.load(lectura)
      lectura.close()
      self.menu = convertidor(self.jsonmenu)
      self.empleados = empleados
   def cobro(self,valor):
      self.balance = self.balance - valor
      if self.balance < 0:
         print(f"te quedaste en negativo y el negocio quebro :c")
         exit()
   def ver_menu(self):
      print("Menu de tu restaurante:")
      for i in self.menu:
         for j in i:
            print(f"{j.get_nombre()} - {j.get_precio()} ({j.get_tipo()})")
   def añadir_productos(self, n : int):
      ip = 0
      while ip < n:
         print(f"que producto deseas añadir a tu restaurante?")
         x = int(input(f"1 para sopas, 2 para ensaladas, 3 para bebidas, 4 para platos principales, 5 para postres: "))
         name = input(f"¿que nombre tiene el plato que deseas añadir?")
         precio = float(input(f"¿que precio se le asignara al plato?"))
         if x == 1:
            self.jsonmenu["sopas"].append({"nombre": name, "precio": precio})
         elif x == 2:
            y = input("¿la ensalada lleva vinagreta? (si/no)")
            vinagreta_bool = True if y == "si" else False
            self.jsonmenu["ensaladas"].append({"nombre": name, "precio": precio, "vinagreta": vinagreta_bool})
         elif x == 3:
            y = input("¿la bebida es un jugo? (si/no)")
            jugo_bool = True if y == "si" else False
            self.jsonmenu["bebidas"].append({"nombre": name, "precio": precio, "jugo": jugo_bool, "azucar": False, "hielo": False})
         elif x == 4:
            self.jsonmenu["platos_centrales"].append({"nombre": name, "precio": precio})
         elif x == 5:
            self.jsonmenu["postres"].append({"nombre": name, "precio": precio})
         else:
            print("Opción inválida, intenta de nuevo")
            continue
         ip += 1
      
      # Actualizar el menú de objetos
      self.menu = convertidor(self.jsonmenu)
      
      # Guardar cambios en el archivo JSON
      archivo = open("menu.json", "w")
      json.dump(self.jsonmenu, archivo, indent=2)
      archivo.close()
      print("Productos añadidos exitosamente al menú!")
   def contratar(self):
      num = int(input(f"¿cuantos empleados contrataras?"))
      i = 0
      if num == 0:
         print(f"no puedes contratar 0 empleados")
         self.contratar()
      while i < num:
         tipo = input(f"¿que tipo de empleado deseas contratar? (mesero/cajero)")
         print(f"has puesto un aviso de trabajo..")
         print(f"despues de {random.randint(1,365)} dias llego alguien" )
         nombre = input(f"¿como se llama tu empleado?")
         cobro = random.randint(0,100000)
         print(f"despues de negociar inicialmente {nombre} acepto un pago de {cobro}")
         self.cobro(cobro)
         if tipo == "mesero":
            mes = mesero(nombre)
         elif tipo == "cajero":
            mes = cajero(nombre)
         else: 
            
            raise ValueError("ese cargo no es valido")      
         self.empleados.append(mes)
         i = i + 1


class mesero:
   def __init__(self, nombre: str = "N/A", ordenes: "Queue" = Queue(maxsize=10)):
      self._nombre = nombre
      self._ordenes = ordenes
   def get_ordenes(self):
      return self._ordenes
   def añadir_orden(self, ls:list,le:list,lb:list,lp:list,lps:list):      
      def añadir_producto(ltest, lend): #secuencia para elegir la comida
         for idx, producto in enumerate(iterable_ordenes(ltest)):
            print(f"{idx+1}. {producto._nombre} - {producto._precio}")
         d = int(input("indique el numero que desea pedir: "))
         lend.append(ltest[d-1])
         return d
      lf = []
      flag = True
      print(f"bienvenido")
      while flag == True:
        print(f"que desea pedir? (1 para sopas, 2 para ensaladas, 3 para bebidas, 4 para plato central, 5 para postres)")
        opcion = int(input("opcion: "))
        if opcion == 1: 
           print("que sopa desea pedir? (en caso de pedirse ccon un plato central se recibira un descuneto unico del 5%)")
           añadir_producto(ls,lf)
        if opcion == 2: 
           print("que ensalada desea pedir? (en caso de pedirse con un plato central y una bebida se recibira un descuento unico del 5%)")
           q = añadir_producto(le,lf)
           c = (input("desea vinagreta? (si/no)"))
           if c == "si":
              le[q-1].vinagreta(b=True)
        if opcion == 3:
           print("que bebida desea pedir? (en caso de pedirse con un plato central y unna ensalada se aplicara un descuento unico del 5%)")
           q = añadir_producto(lb,lf)
           c = (input("desea hielo? (si/no)"))
           if c == "si":
              lb[q-1].hielo(b = True)
           if lb[q-1].jugo == True:
               c= (input("desea azucar? (si/no)"))
               if c == "si":
                  lb[q-1].azucar(True)
        if opcion == 4:
           print("que plato central desea pedir? (en caso de pedirse con una ensalada u una bebida o con una sopa se aplicara un descuento unico del 5%)")
           añadir_producto(lp,lf)
        if opcion == 5:
           print("que postre desea pedir?")
           añadir_producto(lps,lf)
        f=input("desea pedir algo mas? (si/no)")
        if f == "no":
           flag = False
      self._ordenes.put(lf) 
   def __str__(self):
      return f"Mesero: {self._nombre}"
# clases de medios de pago
class Mediodepago:
   def __init__(self, disponible: float):
      self._efectivodisponible = disponible
      self._mensaje= 0
   def pagar(self, total):
      if total <= self._efectivodisponible:
         self._efectivodisponible = self._efectivodisponible - total
         print("su pago fue realizado con exito" + str(self._mensaje))
      else:
         print("no tiene suficiente dinero para realizar la transaccion")
class Tarjeta(Mediodepago): #una tarjeta tiene como datos privados el numero,el saldo disponible y el codigo de seguridad
   def __init__(self, disponible: float, numero: str):
      super().__init__(disponible)
      self.__numero = numero
      self._mensaje = ", podra ver el saldo de su tarjeta en el recibo"
   def get_numero(self):
      return self.__numero
class Efectivo(Mediodepago): #el efectivo no tiene datos privados, mas sin embargo la cantidad de dinero que se tiene es privado
   def __init__(self, disponible: float):
      super().__init__(disponible)
      self._mensaje = ", acerquese a un cajero en caso de que su cambio no sea el aducuado"
   def get_efectivo_disponible(self):
      return self._efectivodisponible
class cajero:
   def __init__(self, nombre: str = "N/A"):
      self._nombre = nombre
   def cuentas(self, mesero: "mesero", medio: "Mediodepago"):
      ordenes = mesero.get_ordenes()
      if ordenes.empty():
         print("no hay ordenes para procesar")
         pass
      else:
         orden_actual = ordenes.get()
         cuenta = 0
         print(f"cuenta de {mesero._nombre}:")
         c = False
         e = False
         b = False
         s = False
         discount = False
         print(f"Gracias por su visita, sus compras fuerzon las siguientes:")
         for item in orden_actual:
            print(f"{item.get_nombre()} - {item.get_precio()}")
            cuenta += item.get_precio()
         for i in (orden_actual):
          if i.get_nombre() == "plato central":
             c = True
          if i.get_nombre() == "ensalada":
             e = True
          if i.get_nombre() == "bebida":
             b = True
          if i.get_nombre() == "sopa":
             s = True
         fl = (c and e and b) or (s and c)
         if  fl == True:
          print("debido a la compra del conjunto de 2 o mas de los tipos de productos seleccionados usted recibira un" \
           "descuento unico del 5% en su compra total")
          discount = True     #se aplican descuentos dependiendo de la compra de ciertos productos
         if discount == True:
          cuenta = cuenta - (cuenta*0.05)
          print("su descuento es del 5%")
         print(f"su total parcial es: {cuenta}")
         prop=input("desea dejar propina? (si/no)")
         if prop == "si":
            propina = int(input("indique el porcentaje de propina que desea dejar: "))
            cuenta = cuenta + (cuenta*propina/100)
            print(f"su total con propina es: {cuenta}")
         print(f"total a pagar: {cuenta}")
         medio.pagar(cuenta)
         return cuenta
   def __str__(self):
      return f"Cajero: {self._nombre}"
class iterable_ordenes:
    def __init__(self, lista):
        self._lista = lista
        self._index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._index >= len(self._lista):
            raise StopIteration
        item = self._lista[self._index]
        self._index += 1
        return item
#convertidor de json a objetos
def convertidor(json):
   ls = []
   le = []
   lb = []
   lp = []
   lpo = []
   for pro in json:
      if pro == "sopas":
         for item in json[pro]:
            r = sopas(item["nombre"],item["precio"])
            ls.append(r)
      if pro == "ensaladas":
         for item in json[pro]:
            r = ensaladas(item["nombre"], item["precio"], item["vinagreta"])
            le.append(r)
      if pro == "bebidas":
         for item in json[pro]:
            r = bebidas(item["nombre"], item["precio"], item["jugo"])
            lb.append(r)
      if pro == "platos_centrales":
         for item in json[pro]:
            r = platocentral(item["nombre"], item["precio"])
            lp.append(r)
      if pro == "postres":
         for item in json[pro]:
            r = postres(item["nombre"], item["precio"])
            lpo.append(r)
   return [ls, le, lb, lp, lpo]