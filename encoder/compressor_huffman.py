import heapq
from collections import Counter
from encoder.nodo_huffman import NodoHuffman

class CompresorHuffman():
    def construir_arbol_huffman(self, frecuencias):
        '''
        Se uitiliza la librería heapq para convertir un diccionario de todas 
        los caracteres y sus frecuenciass en un arbol en el que el nodo con la menor frecuencia es la raíz
        '''
        heap = [NodoHuffman(char, freq) for char, freq in frecuencias.items()]
        
        heapq.heapify(heap)
        #Mientras queda más de un nodo
        while len(heap) > 1:

        #Los dos nodos con menores frecuencias se vuelven hijos del nodo actual

            izquierda = heapq.heappop(heap)
            derecha = heapq.heappop(heap)

            '''
            Estos nodos se unen de forma que sea un nodo sin caracter, ya que no es una hoja; 
            la frecuencia siendo la suma de las frecuencias de sus nodos hijos y los punteros hacia sus nodos hijos
            '''
            nodo = NodoHuffman(freq=izquierda.freq + derecha.freq)
            nodo.izquierda = izquierda
            nodo.derecha = derecha

            
            #se regresa este nodo al heap
            
            heapq.heappush(heap, nodo)

        
        #Regresa la raíz una vez sea el unico nodo que queda
        return heap[0]

    def generar_codigos(self, NodoHuffman, prefix="", codigos={}):
        #Esta es la condicion para terminar la recursión
        if NodoHuffman is None:
            return

        #Si esta en un nodo hoja, el codigo para ese caracter es su prefijo
        if NodoHuffman.char is not None:
            codigos[NodoHuffman.char] = prefix

        #Recursion para los hijos izquierda y derecha añadiendo 0 al prefijo en el lado izquierdo y 1 en el lado derecho
        self.generar_codigos(NodoHuffman.izquierda, prefix + "0", codigos)
        self.generar_codigos(NodoHuffman.derecha, prefix + "1", codigos)
        
        #Se regresa un diccionario con los caracteres como llaves y sus codigos como valores
        return codigos

    def compresion_huffman(self, text):
        #Se utiliza counter de la librería collections para regresar un diccionario con todos los caracteres y sus frecuencias
        frecuencias = Counter(text)
        
        #Se construye un arbol huffman utilizando esas frecuencias
        raiz = self.construir_arbol_huffman(frecuencias)
        
        #Se generan los codigos en binario para esas frecuencias
        codigos = self.generar_codigos(raiz)
        
        #Cada caracter del texto se convierte en su codigo
        texto_comprimido = ''.join(codigos[char] for char in text)
        
        #Se regresa el texto comprimido, la raiz del arbol y los codigos de los caracteres
        return texto_comprimido, raiz

    def descompresion_huffman(self, texto_comprimido, raiz):
        #El resultado se guarda como una lista vacía
        resultado = []
        
        #Se comienza a descomprimir desde la raíz
        nodo = raiz

        #Por cada 0 o 1 dentro del texto
        for bit in texto_comprimido:
            #Si es un 0, se analiza el nodo izquierdo, si es un 1, del derecho
            if bit == '0':
                nodo = nodo.izquierda
            else:
                nodo = nodo.derecha

            #Al encontrar un nodo hoja, se añade el caracter
            if nodo.char is not None:
                resultado.append(nodo.char)
                
            #El nodo regresa a ser la raíz para volver a emprezar
                nodo = raiz  
        #Se regresa la lista del resultado unido con un string vacío para obtener el texto original
        return ''.join(resultado)