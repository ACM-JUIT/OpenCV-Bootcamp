# Face Recognition with OpenCV and Python

## Dependencies

- Python (3.x or above)
- OpenCV (3.x or above) [pip install opencv]
- OpenCV Contrib [pip install opencv-contrib-python]

## Face Detection Method

`Haarcascade Classifier - Frontal Face Default`

## Face Recognition Method

`LBPH Recognizer Algorithm`

### Workflow / Project Pipeline

1. createData.py
   Accepts user ID, extracts face ROI (Region of Interest) from camera feed using haarcascades, and saves 60 photos corresponding to user in the dataset folder.

2. trainData.py
   Used "LBPH Recognizer" to train and create a weights file (.yml) for the users whose face data is stored in the dataset folder.

3. recognizeData.py
   Loads the trained network / weights file, extracts ROI (face) from camera feed, preprocesses data and passed through loaded weights to receive id and confidence.

### Create Dataset -> Train our machine -> Recognize faces
