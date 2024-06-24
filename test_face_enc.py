import face_recognition

# Dictionary that holds encodings and names of known faces
known_faces = {}

# Load the image of the person we want to recognize
image_path = "known_faces/este_2.png"


image = face_recognition.load_image_file(image_path)
encoding = face_recognition.face_encodings(image)[0]

# Add the encoding to the dictionary
known_faces["Este"] = encoding

# Test the encoding on a new image
unknown_image_path = "known_faces/este_2.png"
unknown_image = face_recognition.load_image_file(unknown_image_path)
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare the unknown face with the known faces
results = face_recognition.compare_faces(list(known_faces.values()), unknown_encoding)

# Print the results
for name, result in zip(known_faces.keys(), results):
    if result:
        print(f"The unknown face is: {name}")
    else:
        print("The unknown face is not recognized")
