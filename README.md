# Reto_8_POO
----------------------------------
### Ejercicio: cree una clase iterable para los items del restaurante de tal forma que al realizar la orden esta sea recorrida
```python
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
```
### Explicacion:
- Dentro de la clase definimos el index de la lista que contiene los productos ademas del index actual
- Por medio del metodo __iter__ creamos el iterador a partir del iterable
- Por medio de __next__ definimos el como la lista es recorrida 
``` python
 def añadir_producto(ltest, lend): #secuencia para elegir la comida
         for idx, producto in enumerate(iterable_ordenes(ltest)):
            print(f"{idx+1}. {producto._nombre} - {producto._precio}")
         d = int(input("indique el numero que desea pedir: "))
         lend.append(ltest[d-1])
         return d
```
### Explicacion:
- Dentro del metodo añadir producto  usamos el built-in enumerate en el iterable aplicado en la lista de ordenes para entregar por medio de un print cada item junto con su numero asociado que el usuario tendra que ingresar