import cv2
import face_recognition
import os
import time

# Ensure the unknown_faces directory exists
if not os.path.exists('unknown_faces'):
    os.makedirs('unknown_faces')


# Test camera, make sure video never stops until user presses "q"
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    if not ret:
        print("Failed to capture image from camera. Exiting...")
        break

    cv2.imshow("Video", frame)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)

    if face_locations:
        # If faces are found, save the frame to the unknown_faces directory
        face_filename = f"unknown_faces/face_{len(face_locations)}_{cv2.getTickCount()}.jpg"
        cv2.imwrite(face_filename, frame)
        print(f"Face detected. Image saved to {face_filename}")
        time.sleep(2)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()