from PIL import Image
import os
import pathlib 
import cv2
from numpy import delete
from tqdm.auto import tqdm

#Esto es una ejemplo de dirección
#Nota: Si el programa no funciona probablemente sea por la dirección, cambiala a la dirección donde tengas guardado el archivo para que funcione porque
# las direcciones que yo puse son las de mi pc y no necesariamente van a ser las misma en tu pc, antes de que digas que no sirve verifica eso xd
direccion = 'C:/Users/EQUIPO/Desktop/Proyectos/Ayuda-skinning/Images'
files = os.listdir(direccion)

direccion_guardado = 'C:/Users/EQUIPO/Desktop/Proyectos/Ayuda-skinning/Redimensionadas'
save_direct = os.listdir(direccion_guardado)

caracteres = '@2x'
images_para_redimensionar = int(input('¿Cuantas imagenes quieres redimensionar?: '))
i = 0

#Nota de lo que aprendí: los bucles sirven para realizar una tarea una y otra vez hasta que se le diga que pare por una condición (las condiciones
#pueden ser tanto 'BREAK' como 'CONTINUE', el break termina por completo el bucle, el continue solo ignora tal cosa, puede ser un bucle While o bucle for
#las dos son muy parecidas y sinceramente no conozco que diferencias tendrán entre ellas.#

for files in files:
    i+=1
    #el os.path.join es una función para interactuar con el sistema operativo (SO), esta incluido modulos de utilidad por defecto de Python y proporciona
    #una forma portable de utilizar el sistema operativo, así puedes hacer que tu código corra tanto en MAC, Linux y Windows sin problemas, el módulo 'os.path' 
    #es un submódulo del módulo OS en Python que se utiliza para la manipulación de nombres de rutas comunes, en otras palabras se usa para interactuar con las
    #direcciones de nuestros archivos (o por lo menos eso es lo que entendí), el 'os.path.join' une uno o más componentes de una dirección (supongo) de forma
    #inteligente, Este método concadena varios componentes de ruta con exactamente un separador de directorio ('/') en Windows ('\') en Unix/Linuxdespués de 
    #cada parte no vacía, excepto el último componente de ruta. Se usa siempre que quieras usar las direcciones de los archivos.
    
    #redimensionamiento...
    imagen_to_resize = Image.open(os.path.join(direccion, files))
    ancho, alto = imagen_to_resize.size
    imagen_to_resizes = imagen_to_resize.resize((ancho//2, alto//2))
    
    #cambio de nombre...
    name = str(imagen_to_resizes)
    rename = name.replace(caracteres, ' ')

    #guardado
    imagen_to_resizes.save (f'{rename}.png', 'w')

    if i == images_para_redimensionar:
        break

    if '@2x' not in files:
        break

    #for i in tqdm(range(images_para_redimensionar)): #esto es una barra de carga
        #print(' ', end='\r')