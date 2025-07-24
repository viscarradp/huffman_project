# Laboratorio de Codificación de Huffman

[cite_start]Este repositorio contiene el notebook interactivo para el **Trabajo de investigación aplicada** de la materia **Estructuras de Datos y Algoritmos**[cite: 6]. El proyecto se centra en la implementación, aplicación y análisis de rendimiento del algoritmo de compresión sin pérdida de Huffman.

[cite_start]El objetivo es demostrar la aplicación de estructuras de datos y algoritmos en la resolución de problemas complejos, en este caso, la compresión de datos[cite: 12].

---

##  sadržaj del Notebook

El notebook `experimentos_huffman.ipynb` está dividido en tres secciones principales que guían al lector desde la implementación base hasta el análisis de resultados.

### 1. Motor de Compresión y Análisis
En esta primera parte, se definen todas las funciones esenciales que componen nuestro compresor en Python. Aquí se encuentra la lógica para:
* Leer archivos y calcular la frecuencia de caracteres.
* Construir el árbol de Huffman y generar los códigos binarios.
* Comprimir y analizar los resultados (tamaño original, tamaño comprimido, ratio de compresión).
* Generar visualizaciones para el análisis de rendimiento.

### 2. Aplicaciones Prácticas
Se demuestra el uso del algoritmo en tres casos de uso distintos para probar su versatilidad:
* **Aplicación 1: Compresión de Texto Literario:** Se comprime un extracto del libro "Don Quijote de la Mancha" para mostrar el funcionamiento del algoritmo en lenguaje natural.
* **Aplicación 2: Compresión de Código Fuente:** Se utiliza el propio código del compresor como archivo de entrada para analizar cómo se comporta Huffman con la sintaxis de un lenguaje de programación.
* **Aplicación 3: Compresión de Secuencias de ADN:** Se comprime una secuencia de ADN (`A`, `C`, `G`, `T`) para demostrar la increíble eficiencia del algoritmo en escenarios con un alfabeto muy reducido.

### 3. Experimentos y Análisis de Rendimiento
Finalmente, se somete el algoritmo a dos pruebas cuantitativas para evaluar su eficiencia:
* **Experimento 1 - Pruebas en 3 Escenarios:** Se compara el ratio de compresión en tres tipos de archivos del mismo tamaño: texto normal, texto altamente repetitivo y texto con caracteres aleatorios.
* **Experimento 2 - Escalabilidad del Algoritmo:** Se analiza cómo escala la compresión al procesar archivos de tamaños crecientes (1 KB a 100 KB), observando la relación entre el tamaño original y el comprimido.

---

## Cómo Ejecutar el Notebook

Para explorar este proyecto, sigue estos pasos:

### Prerrequisitos
Asegúrate de tener Python y las siguientes librerías instaladas:
```bash
pip install jupyter pandas matplotlib numpy
