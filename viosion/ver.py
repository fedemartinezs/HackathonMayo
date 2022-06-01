#Librerias usadas
import cv2
from cv2 import boundingRect 

def rastrear():
    pass
#Instanciar objeto de rastreo
seguidor = Rastreador()

#Lectura del video(capture)
cap = cv2.VideoCapture('../avenida3.mp4')

#Elegimos el metodo de BackgroundSubstractor
detection = cv2.createBackgroundSubtractorMOG2(history=20000,varThreshold=100,detectShadows=False)

while True:
    ret,frame = cap.read()

    #definimos una resolucion para la ectura del video
    frame= cv2.resize(frame(1280,720))

    zona = frame[200:500, 400:900]

    mascara= deteccion.apply(zona)
    
    _,mascara = cv2.threshold(mascara,254,255, cv2.THRESH_BINARY)

    contornos,_ =cv2.findContours(mascara,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detecciones =[]

    for cont in contornos:

        area = cv2.contourArea(cont)

        if area > 1000:
            x,y,ancho,alto = cv2
            boundingRect(cont)
            cv2.rectangle(zona,(x,y),(x+ancho,y+alto), (0,255,0),2)

            direcciones.append([x,y,ancho,alto])


    info_id = seguidor.rastreo(detecciones)

    for inf in info_id:
        x, y, ancho, alto, id =inf
        cv2.putText(zona, "Movil"+str(id), (x,y -15),cv2.FONT_HERSHEY_PLAIN,1(0,255,0),2)