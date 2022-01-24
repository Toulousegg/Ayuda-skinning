from PIL import Image
import os
import pathlib 
import cv2
from numpy import delete

#Esto es una ejemplo de dirección
#Nota: Si el programa no funciona probablemente sea por la dirección, cambiala a la dirección donde tengas guardado el archivo para que funcione porque
# las direcciones que yo puse son las de mi pc y no necesariamente van a ser las misma en tu pc, antes de que digas que no sirve verifica eso xd
<<<<<<< HEAD
direccion = 'C:/Users/EQUIPO/Desktop/Proyectos/Ayuda-skinning/Images'
files = os.listdir(direccion)
direccion_guardado = 'C:/Users/EQUIPO/Desktop/Proyectos/Ayuda-skinning/Redimensionadas'
=======
direccion = 'D:/proyectos/Python/ayuda skinning/Images'
files = os.listdir(direccion)
direccion_guardado = 'D:/proyectos/Python/ayuda skinning/Redimensionadas'
>>>>>>> 27937354a3bc6385f0af5202384a0baf72bab3d0
save_direct = os.listdir(direccion_guardado)
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
    imagen_to_resize = Image.open(os.path.join(direccion, files))
    ancho, alto = imagen_to_resize.size
    imagen_to_resizes = imagen_to_resize.resize((ancho//2, alto//2))

    if imagen_to_resizes.endswith('.png'):
        name = os.path.join (os.path.abspath (direccion), files) #esto obtiene el nombre original de la imagen
        rename = os.path.join (os.path.abspath (direccion), 'Prueba_' + files) #Renombrar de acuerdo a sus necesidades, puede cambiar 'E_' + img al nombre que desee
        rename_completed = os.rename (name, rename) #Rename, sobrescribe el nombre original

<<<<<<< HEAD
    else:
        continue

    if '@2x' in name:
            del_2x = name
            del_2x_name = os.path.abspath (direccion)
            del_2x_rename = os.path.join(del_2x_name, del_2x_name - '@2x')

    #if i >= 20: #quiero que el programa tenga un limite de 20 archivos máximo para redimensionar
        #break

    if i == 10:
        break

    imagen_to_resizes.save (f'Redimensionada_{i}.png')
=======
    if '@2x' not in files:
        break
>>>>>>> 27937354a3bc6385f0af5202384a0baf72bab3d0
