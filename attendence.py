import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime,timezone,timedelta


path = 'Images'

image_list = []

classNames = []

myList = os.listdir(path)



def getDateTime():
    tz = timezone(timedelta(hours=5,minutes=30))
    now = datetime.now(tz)
    date = now.strftime("%d")
    month = now.strftime("%m")
    year = now.strftime("%Y")
    hour = now.strftime("%I")
    minute = now.strftime("%M")
    am_pm = now.strftime("%p").upper()

    month_dict = {
        "01":"Jan",
        "02":"Feb",
        "03":"Mar",
        "04":"Apr",
        "05":"May",
        "06":"Jun",
        "07":"Jul",
        "08":"Aug",
        "09":"Sep",
        "10":"Oct",
        "11":"Nov",
        "12":"Dec"
    }

    month_name = month_dict.get(month, "Invalid month")

    formated_date_Time  = f"{date}--{month_name.upper()}-{year} {hour}:{minute} {am_pm}"
    return formated_date_Time


def mark_attendence(name):
    with open('attendence.csv','r+') as f:
        my_data_List = f.readlines()
        name_List = []
        for line in my_data_List:
            entry = line.split(",")
            name_List.append(entry[0])
        if name not in name_List:
            date_String = getDateTime()
            f.write(f'\n{name},{date_String}')

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




cap = cv2.VideoCapture(0)

def attendence_system ():
    while True:
        success, img = cap.read()
        img_small = cv2.resize(img,(0,0),None,0.25,0.25)
        img_small = cv2.cvtColor(img_small,cv2.COLOR_BGR2RGB)
        faces_current_frame = face_recognition.face_locations(img_small)
        encoding_current_frame_cam = face_recognition.face_encodings(img_small,faces_current_frame)

        for encodeFace,faceLoc in zip(encoding_current_frame_cam,faces_current_frame):
            matches = face_recognition.compare_faces(encode_list_known,encodeFace)
            faceDis = face_recognition.face_distance(encode_list_known,encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)


            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                mark_attendence(name)
                y1,x2,y2,x1 = faceLoc
                y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        cv2.imshow('webcam',img)
        cv2.waitKey(1)