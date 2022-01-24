#CREO QUE ESTO SIRVE PARA OBTENER LA DIRECCIÓN DEL USUARIO AUTOMATICAMENTE SIN NECESIDAD DE ESTAR CAMBIANDO LA DIRECCIÓN DESDE EL CODE

import os
 
ROOT_DIR = os.path.abspath("../")
img_path = os.path.join(ROOT_DIR, "Ayuda-skinning/Images")
imglist = os.listdir(img_path)
#print(filelist)
i = 0
for img in imglist:
    i+=1
    if img.endswith('.jpg'):
        print(i)
        src = os.path.join (os.path.abspath (img_path), img) #El nombre original de la imagen
        dst = os.path.join (os.path.abspath (img_path), 'E_' + img) # Renombrar de acuerdo a sus necesidades, puede cambiar 'E_' + img al nombre que desee
        os.rename (src, dst) #Rename, sobrescribe el nombre original