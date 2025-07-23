class NodoHuffman:
    '''
    Estos son los nodos de los arboles de huffman, que contienen, un caracter, su frequencia,
    el nodo a su izquierda y el nodo a su derecha
    '''
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.izquierda = None
        self.derecha = None


    def __lt__(self, otro):
        '''
        esta funcion permite que se puedan comparar dos nodos utilizando los simbolos de < y >,
        utilizando sus frecuencias
        '''
        return self.freq < otro.freq


