import cv2
import numpy as np

def apply_gaussian_blur(image, kernel_size):
    return cv2.GaussianBlur(image, kernel_size, 0)

def apply_canny(image, low_threshold, high_threshold):
    return cv2.Canny(image, low_threshold, high_threshold)

def region_of_interest(image):
    height, width = image.shape[:2]
    mask = np.zeros_like(image)

    # Defining a triangular region of interest for rural lanes
    polygon = np.array([[
        (int(0.1 * width), height),
        (int(0.9 * width), height),
        (int(0.5 * width), int(0.5 * height))
    ]], np.int32)
    
    cv2.fillPoly(mask, polygon, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def draw_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 5)
    return line_image
