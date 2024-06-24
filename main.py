import os
import cv2
import time
import face_recognition
import json

def encode_initial_faces() -> None:
    if not os.path.exists('known_faces.json'):
        with open('known_faces.json', 'w') as file:
            file.write('{}')
    with open('known_faces.json') as file:
        known_faces = json.load(file)

    known_faces_dir = os.path.join(os.path.dirname(__file__), 'known_faces')

    for file in os.listdir(known_faces_dir):
        file_path = os.path.join(known_faces_dir, file)
        image = face_recognition.load_image_file(file_path)
        encoding = face_recognition.face_encodings(image)[0]
        known_faces[os.path.splitext(file)[0]] = encoding.tolist()
    
    with open('known_faces.json', 'w') as file:
        json.dump(known_faces, file)


def add_new_face(face_file_name) -> None:
    '''
    Adds a new face to the known_faces.json file.

    Args:
        face_file_name (str): The name of the file containing the face to be added. WITH FILE EXTENSION
    '''
    known_faces_dir = os.path.join(os.path.dirname(__file__), 'known_faces')
    new_face_path = os.path.join(known_faces_dir, face_file_name)
    with open('known_faces.json') as file:
        known_faces = json.load(file)
    image = face_recognition.load_image_file(new_face_path)
    encoding = face_recognition.face_encodings(image)[0]
    known_faces[os.path.splitext(face_file_name)[0]] = encoding.tolist()

    with open('known_faces.json', 'w') as file:
        json.dump(known_faces, file)

def del_face(face_name) -> None:
    '''
    Deletes a face from the known_faces.json file.

    Args:
        face_name (str): The name of the face to be deleted. NO FILE EXTENSION.
    '''
    with open('known_faces.json') as file:
        known_faces = json.load(file)
    known_faces.pop(face_name)

    with open('known_faces.json', 'w') as file:
        json.dump(known_faces, file)

def start_rec() -> None:
    video_capture = cv2.VideoCapture(0)
    last_save_time = time.time()
    save_interval = 2

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print(f"{ret = }")
            break

        cv2.imshow("", frame)

        rgb_frame = frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_frame)

        current_time = time.time()
        if face_locations and (current_time - last_save_time) > save_interval:
            face_filename = f"unknown_faces/face_{len(face_locations)}_{cv2.getTickCount()}.jpg"
            cv2.imwrite(face_filename, frame)
            print(f"Face detected. Image saved to {face_filename}")
            last_save_time = current_time
        else:
            time.sleep(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


def create_list() -> list[str]:
    attendance_list = []

    unknown_faces_dir = os.path.join(os.path.dirname(__file__), 'unknown_faces')

    for file in os.listdir(unknown_faces_dir):
        file_path = os.path.join(unknown_faces_dir, file)
        image = face_recognition.load_image_file(file_path)
        encoding = face_recognition.face_encodings(image)
        if not encoding:
            print(f"No face found in {file}")
            continue
        unknown_encoding = encoding[0]

        with open('known_faces.json') as file:
            known_faces = json.load(file)
        for name, face_encoding in known_faces.items():
            results = face_recognition.compare_faces([face_encoding], unknown_encoding)
            if results[0]:
                attendance_list.append(name)
                break
    return(set(attendance_list))

def del_fotos() -> None:
    if os.path.exists('unknown_faces'):
        for file in os.listdir('unknown_faces'):
            os.remove(f'unknown_faces/{file}')
        os.rmdir('unknown_faces')


def main() -> None:
    if not os.path.exists('unknown_faces'):
        os.makedirs('unknown_faces')
    start_rec()
    attendance_list = create_list()
    print(f"Attendance: {attendance_list}")
    del_fotos()



if __name__ == "__main__":
    # Uncomment the following line to encode the initial faces
    # encode_initial_faces()

    # Uncomment the following line to add a new face
    # add_new_face("este.jpg")

    # Uncomment the following line to delete a face
    # del_face("este_1")

    main()

    
