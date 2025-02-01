import cv2
import numpy as np
import face_recognition
import os



elon_image = face_recognition.load_image_file("Images/elon-musk-192956355-3x4_0.jpg")
elon_rgb = cv2.cvtColor(elon_image,cv2.COLOR_BGR2RGB)

elon_image_test = face_recognition.load_image_file("Images/zackma-test.jpg")
elon_rgb_test = cv2.cvtColor(elon_image,cv2.COLOR_BGR2RGB)

face_loc = face_recognition.face_locations(elon_image)[0]
encode_face_elon = face_recognition.face_encodings(elon_image)[0]
encode_face_elon_test = face_recognition.face_encodings(elon_image_test)[0]
cv2.rectangle(elon_image,(face_loc[3],face_loc[0],face_loc[1],face_loc[2],),(255,0,255),2)

result = face_recognition.compare_faces([encode_face_elon],encode_face_elon_test)
distance = face_recognition.face_distance([encode_face_elon],encode_face_elon_test)
print(result,distance)

cv2.putText(elon_image_test,f'{result} {round(distance[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.imshow('elon musk',elon_image)
cv2.imshow('elon test',elon_image_test)



cv2.waitKey(0)
