from attendence import attendence_system
import os
import cv2
import time


def Register_Face():
    cap = cv2.VideoCapture(1)
    Student_name = str(input("Enter Student name : "))
    print("please dont shake while taking picture the picture will be clicked in 8 next seconds try to look straight into your webcam \n and also please try to be close to the camera so that system could fetch your face then press 'C' key to capture")
    time.sleep(8)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Webcam', frame)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.imwrite(os.path.join('Images', f'{Student_name}.jpg'), frame)
            print("Success")
            break

    cap.release()
    cv2.destroyAllWindows()



def main():
    print("Press 1 and then 'enter key' to register a student face id \n Press 2 to start marking attendence for today")
    user_input = int(input("Enter your choice : "))


    if (user_input == 1):
        Register_Face()
    elif (user_input == 2) :
        print("activating attendence system")
        attendence_system()
    else:
        print("Wrong Choice")


while True:
    main()