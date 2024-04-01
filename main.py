import cv2
import numpy as np

image = cv2.imread('./mario.jpg')

rows, cols, _ = image.shape
print("Rows: ", rows, "Cols: ", cols)

size = 1
multiplier = 5
section_width = size
section_height = size

num_rows = rows // section_height
num_cols = cols // section_width

print(num_rows, num_cols)

sections = []
for y in range(0, num_rows*section_height, section_height):
    for x in range(0, num_cols*section_width, section_width):
        section = image[y:y + section_height, x:x + section_width]
        sections.append(section)

def get_average_color(section):
    average_color = np.mean(section, axis=(0, 1)).astype(int)
    return tuple(average_color)

colors = [get_average_color(section) for section in sections]

# Display the original image with section boundaries
# for i, section in enumerate(sections):
#     x = (i % num_cols) * section_width
#     y = (i // num_cols) * section_height
#     cv2.rectangle(image, (x, y), (x + section_width, y + section_height), (0, 255, 0), 2)

cv2.imshow('Image with Colored Sections', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Create a blank image with correct dtype
section_width_length = int(size*multiplier)
blank_image = np.zeros((section_width_length * num_rows, section_width_length * num_cols, 3), np.uint8)

for i, color in enumerate(colors):
    row = i // num_cols
    col = i % num_cols
    top_left = (col * section_width_length, row * section_width_length)
    bottom_right = ((col + 1) * section_width_length, (row + 1) * section_width_length)
    blank_image[row * section_width_length:(row + 1) * section_width_length,
    col * section_width_length:(col + 1) * section_width_length] = color
    # print(i, color, type(color))

cv2.imwrite('mario_reduced2.jpg', blank_image)

cv2.imshow('Image with Colored Sections', blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()