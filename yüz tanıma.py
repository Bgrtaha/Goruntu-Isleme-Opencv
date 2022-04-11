import numpy as np
import cv2
import face_recognition
import tkinter as tk
from tkinter import filedialog

def UploadAction(event=None):
    global filename
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

def print_filename():
    print(filename)

root = tk.Tk()
button = tk.Button(root, text='UPLOAD A FACE ', command=UploadAction)
button.pack()
root.mainloop()


print_filename()

taha_yüz = face_recognition.load_image_file(filename)
taha_enc = face_recognition.face_encodings(taha_yüz)[0]

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    yüz_konum = face_recognition.face_locations(frame)
    face_encoding = face_recognition.face_encodings(frame,yüz_konum)

    for face in face_encoding:
        sonuc = face_recognition.compare_faces([taha_enc],face)
        print(sonuc)

    cv2.imshow("1",frame)
    if cv2.waitKey(30) & 0xff == ord("k"):
        break
cap.release()
cv2.destroyAllWindows()