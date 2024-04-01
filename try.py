import cv2
import numpy as np

# Define the dimensions of the blank image
width, height = 800, 600
channels = 3  # RGB image

# Create a blank image
blank_image = np.zeros((height, width, channels), dtype=np.uint8)

# Divide the image into a 3x3 grid
num_rows = 3
num_cols = 3
section_width = width // num_cols
section_height = height // num_rows

# Define different colors for each section
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
          (255, 255, 0), (255, 0, 255), (0, 255, 255),
          (128, 0, 0), (0, 128, 0), (0, 0, 128)]

# Draw a colored rectangle in each section
for i, color in enumerate(colors):
    row = i // num_cols
    col = i % num_cols
    top_left = (col * section_width, row * section_height)
    bottom_right = ((col + 1) * section_width, (row + 1) * section_height)
    cv2.rectangle(blank_image, top_left, bottom_right, color, -1)

# Display the image with colored sections
cv2.imshow('Image with Colored Sections', blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the image
cv2.imwrite('path/to/save/colored_sections.png', blank_image)
