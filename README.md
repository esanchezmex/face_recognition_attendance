# Face Recognition for Attendance

Attendnace methods at IE are below par in terms of comfort and UX for both the teacher and the students. This projects aims to simplify the process. 

The way this project works is the teacher runs the program, which will open a camera (using cv2 library in python) and each student shows their face to the camera as they enter the class. The program will detect each face (using the face_recognition library in python) and add it to the attendance list which will print out for the professor to see. 

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation

### Steps

From your terminal, use the following commands:

1. Clone the repository:

> `git clone https://github.com/esanchezmez/your-repo-face_recognition_attendance.git`

3. Navigate to the repo
   
> `cd face_recognition_attendance`

5. Install Dependencies
   
> `pip3 install -r requirments.txt`

## Usage

1. The first step is to collect the initial fotos of the students. Once these have been collected, create a direcotry called `known_faces` using the following command prompt:
> `mkdir known_faces`

and add the fotos to the new directory.
3. Once the fotos are in the correct directory, in the main.py script go to the end of the file where the main block is located. Uncomment the code to encode the initial faces
4. Once you have the initial faces encoded, comment again the line to encode initial faces, and make sure only the `main()` function is uncommented.
5. Run the script.

### To add a new face

In order to add a new face to the encodings list follow these steps:

1. Collect the foto of the new student and add it to the known_faces directory
2. Go to the bottom of the script to the main block.
3. Un-comment the `add_new_face()` function
4. For arguments, input the file name of the foto as a string. Only the file name without a path, but make sure to inlcude the extension
   > i.e. "new_face.jpeg"
6. Comment out the `main()` function
7. Run the script
8. Once you have the new face encoded, comment again the function to encode a new face, and make sure only the `main()` function is uncommented.

The script is ready to recognize the new person. 


### To delete a face

In order to delete a face follow these steps:

1. Go to the bottom of the script to the main block.
2. Un-comment the `del_face()` function
3. For arguments, input the name of the person whos face will be deleted as a stirng. Only the name without a path and without the file extension
  > i.e. "old_face"
4. Comment out the `main()` function
5. Run the script
6. Once you have the face deleted, comment again the function, and make sure only the `main()` function is uncommented.


## Features

### Continuous Camera

The camera is continoulsy recording and identifyin faces, meaning that the teacher does not have to take any fotos neither of each student or the class as a whole. 

### Delete screenshots immediatly after creating list

Since the camera is taking screenshots to recognize and match the faces to the recorded encodings, students fotos will be temporarily saved in a directory called unknown_faces. For privacy conerncs, these images will be deleted as soon as the attendance list is created. 



