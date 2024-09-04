import cv2
import numpy as np
from src.utils import apply_gaussian_blur, apply_canny, region_of_interest, draw_lines
from src.config import Config
import os

def detect_lanes(image, filename):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blur_gray = apply_gaussian_blur(gray, Config.GAUSSIAN_BLUR_KERNEL)

    # Apply Canny edge detection
    edges = apply_canny(blur_gray, Config.CANNY_LOW_THRESHOLD, Config.CANNY_HIGH_THRESHOLD)
    
    # Save the edge-detected image
    edges_path = os.path.join(Config.OUTPUT_IMAGE_PATH, 'edges_' + filename)
    cv2.imwrite(edges_path, edges)

    # Define region of interest
    masked_edges = region_of_interest(edges)

    # Save the masked edge-detected image
    masked_edges_path = os.path.join(Config.OUTPUT_IMAGE_PATH, 'masked_edges_' + filename)
    cv2.imwrite(masked_edges_path, masked_edges)

    # Apply Hough Line Transform to detect lines
    lines = cv2.HoughLinesP(
        masked_edges,
        rho=1,
        theta=np.pi / 180,
        threshold=Config.HOUGH_THRESHOLD,
        minLineLength=Config.HOUGH_MIN_LINE_LENGTH,
        maxLineGap=Config.HOUGH_MAX_LINE_GAP
    )

    # Draw the lines on the original image
    line_image = draw_lines(image, lines)
    
    # Combine the original image with the line image
    output_image = cv2.addWeighted(image, 0.8, line_image, 1, 0)
    
    # Save the final output image
    output_image_path = os.path.join(Config.OUTPUT_IMAGE_PATH, 'output_' + filename)
    cv2.imwrite(output_image_path, output_image)
    
    return output_image, edges_path, masked_edges_path, output_image_path
