#@markdown We implemented some functions to visualize the face landmark detection results. <br/> Run the following cell to activate the functions.
import cv2
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import matplotlib.pyplot as plt
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

import numpy as np
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


IMAGE_FILENAMES = ['k.png']
# Create the options that will be used for FaceStylizer
base_options = python.BaseOptions(model_asset_path='face_stylizer_color_sketch.task')
options = vision.FaceStylizerOptions(base_options=base_options)

# Create the face stylizer
with vision.FaceStylizer.create_from_options(options) as stylizer:

  # Loop through demo image(s)
  for image_file_name in IMAGE_FILENAMES:

    # Create the MediaPipe image file that will be stylized
    image = mp.Image.create_from_file(image_file_name)
    # Retrieve the stylized image
    stylized_image = stylizer.stylize(image)

    # Show the stylized image
    rgb_stylized_image = cv2.cvtColor(stylized_image.numpy_view(), cv2.COLOR_BGR2RGB)
    cv2.imshow('My Image', rgb_stylized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()