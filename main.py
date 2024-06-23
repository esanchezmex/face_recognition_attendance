import os
import cv2
import time
import face_recognition


def start_rec():
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print(f"{ret = }")
            break

        cv2.imshow("Video", frame)

        rgb_frame = frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_frame)

        if not face_locations:
            time.sleep(1)
        face_filename = f"unknown_faces/face_{len(face_locations)}_{cv2.getTickCount()}.jpg"
        cv2.imwrite(face_filename, frame)
        print(f"Face detected. Image saved to {face_filename}")
        time.sleep(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


def create_list():
    pass



def main():
    if not os.path.exists('unknown_faces'):
        os.makedirs('unknown_faces')

    start_rec()



if __name__ == "__main__":
    main()

    
