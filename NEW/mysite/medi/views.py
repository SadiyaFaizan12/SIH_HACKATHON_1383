
from django.shortcuts import render
from django.http import HttpResponse
import cv2
import face_recognition
import requests
import numpy as np



# Create your views here.

def index(request):
    
    return render(request,'index.html')
def f2(request):
    return render(request,'frame2.html')
def f3(request):
    return render(request,'frame3.html')
def f4(request):
    return render(request,'frame4.html')
def f5(request):
    return render(request,'frame5.html')
def f6(request):
    return render(request,'frame6.html')
def f7(request):
    return render (request,'frame7.html')
def f8(request):
    return render (request,'frame8.html')
def f10(request):
    return render(request,'frame10.html')
def f11(request):
    return render(request,'frame-11.html')
def flast(request):
    return render(request,'last-frame.html')
def facerec(request):
    

    # Load known faces
    known_face_encodings = []
    known_face_names = []

    # Add your known faces here
    # known_face_encodings.append(encoding_of_person_1)
    # known_face_names.append("Person 1")

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []

    url = "YOUR_CCTV_CAMERA_URL_HERE"

    # Capture video stream from the CCTV camera
    cap = cv2.VideoCapture(url)

    while True:
        # Read a frame
        ret, frame = cap.read()

        # Resize frame to speed up face recognition
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (OpenCV) to RGB color (face_recognition)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Find all face locations and face encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Compare each face found in the frame with the known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # Display the resulting frame
        cv2.imshow('CCTV Face Recognition', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video stream and close all windows
    cap.release()
    cv2.destroyAllWindows()






    