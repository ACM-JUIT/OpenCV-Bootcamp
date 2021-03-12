import os
import cv2
import numpy as np
from PIL import Image

# Initializing recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Function to get image data with corresponding


def getImagesWithID(path):

    # Create a list of the paths of each image - Eg. [dataset\User.1.12.jpg, dataset\User.1.13.jpg...]
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

    # Creeating empty lists for face data and ids
    faces = []
    ids = []

    # Looping through each path in ImagePaths
    for imagePath in imagePaths:

        # Converting to readable data
        face = Image.open(imagePath).convert('L')

        # Converting each face data to numpy array
        face_np = np.array(face)

        # Extracting id of each face
        id = int(os.path.split(imagePath)[-1].split('.')[1])

        # Appending Numpy data to faces list
        faces.append(face_np)
        # Appending id of corresponding face
        ids.append(id)

        cv2.imshow('Training', face_np)
        cv2.waitKey(10)

    return ids, faces


DATASET_PATH = 'dataset'
ids, faces = getImagesWithID(DATASET_PATH)
print(faces)

# Training our Recognizer
recognizer.train(faces, np.array(ids))

# Save the trained network
recognizer.save('trainedData.yml')

cv2.destroyAllWindows()
