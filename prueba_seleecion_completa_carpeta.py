from PIL import Image
import os

direccion = 'C:/Users/Franklin Mogollón/Documents/Proyectos (Programing)/Ayuda-skinning/images de prueba'
files = os.listdir(direccion)

caracteres = '@2x'

i = 0

print('Escribe 0 para seleccionar todo')
images_para_redimensionar = int(input('¿Cuantas imagenes quieres redimensionar?: '))

if images_para_redimensionar == 0: #quiero que esto seleecione todos los elementos de una carpeta solo escribiendo 0 o *
    for seleccion_completa in files:
        print(f'Seleccionaste todos los elementos, será un total de imagenes para redimensionar')
        #elementos = (list(map(int, files))) #problema en esta linea, selecciona un elemento pero me dice que es un elemento invalido
        ints = []
        for elementos in seleccion_completa: #tengo que encontrar la forma de poner esto en un bucle ya sea for o while que se repita la operacióon y seleccione todos los elementos de la lista 
            todos_elementos = ints.append[int(elementos)]    
        #files[elementos][all]
        print (todos_elementos)

#redimensionamiento, proceso
for files in files:
    i+=1
    
    #redimensionamiento...
    imagen_to_resize = Image.open(os.path.join(direccion, files))
    ancho, alto = imagen_to_resize.size
    imagen_to_resizes = imagen_to_resize.resize((ancho//2, alto//2))
    
    #cambio de nombre...
    name = imagen_to_resize.filename
    rename = name.replace(caracteres, '')

    #guardado
    imagen_to_resizes.save (f'{rename}')

#notas: Si
##