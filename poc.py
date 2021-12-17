import cv2
import pytesseract

image = cv2.imread('cedula_frontal.jpeg')
# image = cv2.imread('cedula_frontal_02.jpeg')
# image = cv2.imread('cedula_frontal_gris.jpg')
# image = cv2.imread('cedula_frontal_invertida.jpg')



# image = cv2.imread('cedula_dorsal.png')


# Pasar a grises
# image = cv2.imread('cedula_frontal.jpeg', 0)
# cv2.imwrite('cedula_frontal_gris.jpg',image)


# Invertir colores
# image = cv2.bitwise_not(image)
# cv2.imwrite('cedula_frontal_invertida.jpg',image)

# Binarización
th, image = cv2.threshold(image, 128, 256, cv2.THRESH_TOZERO)

text_spa = pytesseract.image_to_string(image, lang='spa')
print('==================================')
print('Texto SPA:', text_spa)

text_eng = pytesseract.image_to_string(image)
print('==================================')
print('Texto ENG (default):', text_eng)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()