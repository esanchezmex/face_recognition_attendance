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

> `git clone https://github.com/esanchezmex/face_recognition_attendance.git`

2. Navigate to the repo
   
> `cd face_recognition_attendance`

3. Create a new Virtual Environment (and activate it)

> `python3 -m venv .venv`
> `source .venv/bin/activate`

4. Install Dependencies
   
> `pip3 install -r requirments.txt`

## Usage

1. The first step is to collect the initial fotos of the students. Once these have been collected, create a directory called `known_faces` using the following command prompt:
> `mkdir known_faces`

2. Add the fotos to the new directory.
3. Once the fotos are in the correct directory, in the main.py script go to the end of the file where the main block is located. Uncomment the the function called `encode_initial_faces` and comment out the `main()` function
4. Once you have the initial faces encoded, comment again the line to encode initial faces, and make sure only the `main()` function is uncommented.
5. Run the script.

### To add a new face

In order to add a new face to the encodings list follow these steps:

1. Collect the foto of the new student and add it to the `known_faces` directory
2. Go to the bottom of the script to the main block.
3. Un-comment the `add_new_face()` function
4. For arguments, input the *file name* of the foto *as a **string***. Only the file name without the full path, but **make sure to inlcude the extension**
   > i.e. "new_face.jpeg"
6. Comment out the `main()` function
7. Run the script
8. Once you have the new face encoded, comment again the function to encode a new face, and make sure only the `main()` function is uncommented.

The script is ready to recognize the new person. 


### To delete a face

In order to delete a face follow these steps:

> **Important note**: The name of the students is saved as the name of the file of their foto, so if the foto used to encode the student "Juan Costuras" is called "juan_costuras.jpeg", his name will be stored as "juan_costuras" in the encodings JSON. Take note of these names. 

1. Go to the bottom of the script to the main block.
2. Un-comment the `del_face()` function
3. For arguments, input the *name of the person* whos face will be deleted *as a **stirng***. Only the name **without** a path and **without** the file extension. (view **Important Note** above)
  > i.e. "juan_costuras"
4. Comment out the `main()` function
5. Run the script
6. Once you have the face deleted, comment again the function, and make sure only the `main()` function is uncommented.

The record of this student (name and face encoding) has been deleted. The program will no longer recognize the student. 


## Features

### Continuous Camera

The camera is continoulsy recording and identifying faces, meaning that the teacher does not have to take any fotos of neither each student or the class as a whole. 

### One time setup

There is minimal setup required as only the initial faces have to be encoded once and then a comparison is easy. Make sure to have a good clear picture of the student to be initially encoded. Same applies for new students, as only a single foto is required to add them to the "databse".

### Delete screenshots immediatly after creating list

Since the camera is taking screenshots to recognize and match the faces to the recorded encodings, student fotos will be temporarily saved in a directory called unknown_faces. For privacy conerncs, these images will be deleted as soon as the attendance list is created. 



