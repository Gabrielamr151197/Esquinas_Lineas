import numpy as np
from cv2 import cv2

img = cv2.imread('img/iglesia_san_jeronimo.jpg')

cv2.imshow('imagen', img)

#convertimos la imagen en escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#lo convertimos en tipo float32
gray =np.float32(gray)
                            
dst = cv2.cornerHarris(gray, #la imagen en escala de grises y de tipo float32
                        2, # blockSize - Es el tamaño del vecindario considerado para la detección de esquinas.
                        3, # ksize – Parámetro de apertura del derivado Sobel utilizado
                        0.04) #k – parámetro libre en la formula de Harris.

dst = cv2.dilate(dst, None)
                              #color rojo
img[dst > 0.01 * dst.max()] = [0,0,255]

cv2.imshow('Harris', img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

