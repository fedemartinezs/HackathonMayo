#creador para logica de contador de autos
# @creador: Fede

#librerias usadas
import cv2

seguidor= Raestrador()


#lectura del video
cv2.VideoCapture('../avenida3.mp4')

#Elegimos el metodo de BackgroundSubstraction
deteccion = cv2.createBackgroundSubtractorMOG2(history=2000, varThreshold=100, detectShadows=False)

while True:
    ret, frame = cap.read()

#definimos una resolucion para la lectura del video
    frame=cv2.resize(frame, (1280,720))

#seleccionamos la zona de interes (coordenadas)
    zona = frame[200:500, 400:900]

#Creamos una mascara a partir de la zona de interes
    mascara=deteccion.apply(zona)

#Definimos el rango de escala de grises (desde 0 hasta 255) en la que detectaremos los movimientos
    _, mascara=cv2.threshold(src=mascara, thresh=254, maxval=255, TresholdingTechnique=cv2.THRESH_BINARY)

#Extraemos las posiciones de los contornos para pintarlos.
    contornos,_= cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Lista para guardar las coordenadas de los contornos
    detecciones=[]

#Dibujamos todos los contornos en frame (matriz), con un color y grosor.
    for cont in contornos:
    #Calculamos el area del contorno
        area=cv2.contourArea(cont)
        if area > 1000:
        #Dibujamos los areas que superen los 1000px
            x, y, ancho, alto = cv2.boundingRect(cont)
            cv2.rectangle(zona, (x,y), (x+ancho, y+ alto), (0,255,0), 2)
            #guardar las coordenadas de los escaneos
            detecciones.append([x,y,ancho,alto])

    #Realizamos el seguimiento
    info_id=seguidor.rastreo(detecciones)
    