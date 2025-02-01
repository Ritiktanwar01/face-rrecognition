import cv2
import numpy as np
import face_recognition
import os


path = 'Images'

image_list = []

classNames = []

myList = os.listdir(path)



for cl in myList:
    curImg = cv2.imread(f"{path}/{cl}")
    image_list.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

def find_encodings(images):
    encode_list = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encoded_img = face_recognition.face_encodings(img)[0]
        encode_list.append(encoded_img)


    return encode_list


encode_list_known = find_encodings(image_list)
print("encoding complete")


cap = cv2.VideoCapture(1)


while True:
    success, img = cap.read()
    img_small = cv2.resize(img,(0,0),None,0.25,0.25)
    img_small = cv2.cvtColor(img_small,cv2.COLOR_BGR2RGB)
    faces_current_frame = face_recognition.face_locations(img_small)
    encoding_current_frame_cam = face_recognition.face_encodings(img_small,faces_current_frame)

    for encodeFace,faceLoc in zip(encoding_current_frame_cam,faces_current_frame):
        matches = face_recognition.compare_faces(encode_list_known,encodeFace)
        faceDis = face_recognition.face_distance(encode_list_known,encodeFace)
        print(faceDis)