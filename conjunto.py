''' Crear la clase conjunto '''
import sys
import os
current = os.path.dirname(os.path.realpath(__file__)) 
parent = os.path.dirname(current)                      
sys.path.append(parent)

from collections import OrderedDict

class Conjunto():
    elementos = []

    def __init__(self, *elemento):
        lista = list(elemento)
        self.elementos = list(OrderedDict.fromkeys(lista))
            
   
    def agregar(self,elemento):
        if elemento not in self.elementos:
            self.elementos.append(elemento)

    def remover(self,elemento):
       self.elementos.remove(elemento)

    def union(self, conjunto):
        salida = self

        for x in conjunto.elementos:
            if x not in salida.elementos:
                salida.agregar(x)
        
        return salida
   
    def interseccion(self,conjunto):
        salida = Conjunto()
       
        for x in conjunto.elementos:
            if x in self.elementos:
                salida.agregar(x)
                
        return salida

    def diferencia(self, conjunto):
        salida = Conjunto()

        for x in self.elementos:
            if x not in conjunto.elementos:
                salida.agregar(x)
        return salida

    def diferencia_simetrica(self, conjunto):
        salida = Conjunto()

        for x in self.elementos:
            if x not in conjunto.elementos:
                salida.agregar(x)
        for x in conjunto.elementos:
            if x not in self.elementos:
                salida.agregar(x)
        return salida

    def producto_cartesiano(self, conjunto):
        salida = Conjunto()

        for x in self.elementos:
            for y in conjunto.elementos:
                salida.agregar((x,y))
        
        return salida

    def  __len__(self):
        return len(self.elementos)

    def __eq__(self, other):
        if len(self) == len(other):
           if self.elementos == other.elementos:
             return True
        else: return False

    def __repr__(self):
       return 'Conjunto' + str(tuple(self.elementos))


