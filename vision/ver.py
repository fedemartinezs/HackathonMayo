#creador para logica de contador de autos

#librerias usadas
import cv2
from cv2 import THRESH_BINARY
from cv2 import threshold
import datetime

# librerias locales
from rastreador import Rastreador

# Instanciar el objeto de rastreo

seguidor = Rastreador()

# lectura el video (capture)
cap = cv2.VideoCapture('avenida3.mp4')
print(cap)

#lectura del video
cv2.VideoCapture('../avenida3.mp4')

#Elegimos el metodo de BackgroundSubstraction
deteccion = cv2.createBackgroundSubtractorMOG2(history=2000, varThreshold=100, detectShadows=False)

while True:
    ret, frame = cap.read()

    # definimos una resolucion para la lectura del video
    frame = cv2.resize(frame, (1280, 720))

    # seleccionamos la zona de interes (coordenadas de la matriz)
    zona = frame[200:500, 400:900]

    # Creamos mascara en la zona de deteccion
    mascara = deteccion.apply(zona)

    # Definimos el rango de escala de grises (desde 0 hasta 255) en la que detectaremos los movimientos
    _, mascara = cv2.threshold(src=mascara, thresh=254, maxval=255, type=cv2.THRESH_BINARY)

    # extramos las posiciones de los contornos para despues pintarlos
    # contornos, _ = cv2.findContours(image=mascara, mode=cv2.RETR_TREE, contours=cv2.CHAIN_APPROX_SIMPLE)
    contornos, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Lista para guardar las coordenadas de los contornos
    detecciones = []

    # Dibujamos todos los contornos en frame (matriz), con un color y un grosor
    for cont in contornos:

        # calculamos el area del contorno
        area = cv2.contourArea(cont)
        
        # Dibujamos los areas que superen los 1000 px
        if area > 1000:
            # escaneo de la zona a ser dibujada. Obtenemos sus coordenadas
            x, y, ancho, alto = cv2.boundingRect(cont)

            # Dibujamos el contorno
            cv2.rectangle(zona, (x, y), (x+ancho, y+alto), (0, 255, 0), 2)

            # guardar las coordenadas de los escaneos
            detecciones.append([x, y, ancho, alto])

    # Realizamos el seguimiento
    info_id, cont = seguidor.rastreo(detecciones)

    

    for inf in info_id:
        x, y, ancho, alto, id = inf
        # colocamos el id (numero de objeto) arriba del objeto detectado
        cv2.putText(zona, "Movil "+str(id), (x, y - 15),cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
        # dibujamos el rectangulo
        cv2.rectangle(zona, (x, y), (x + ancho, y + alto), (0, 255, 0), 3)
        

    # print("Coordenas X-Y-W-H-ID :",info_id)  # muestra las coordenas x,y,ancho,alto y el id
    #guardamos los datos obtenidos en un archivo del tipo csv
    
    
    cv2.imshow('Zona de Interes', zona)
    cv2.imshow('Carretera', frame)
    cv2.imshow('Mascara', mascara)

    key = cv2.waitKey(5)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()

with open('datos.txt','a') as myfile:
    #data = myfile.read()
    myfile.seek(0)
    myfile.write(str(cont) +","+f"{datetime.date.today():%d-%m-%Y}")
    myfile.write("\n")
    myfile.truncate()