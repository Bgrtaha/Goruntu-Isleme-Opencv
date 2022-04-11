import cv2
import pytesseract

path = "C:\\Users\\Buğra\\OneDrive\\Resimler\\elazig.jpeg"
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread(path)

text = pytesseract.image_to_string(img)
print(text)

cv2.imshow("img",img)
cv2.waitkey(0)

