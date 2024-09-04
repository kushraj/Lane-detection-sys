# Configuration settings for the project

class Config:
    # Input file paths
    IMAGE_PATH = 'static/uploads/'
    VIDEO_PATH = 'static/uploads/'

    # Output file paths
    OUTPUT_IMAGE_PATH = 'static/uploads/'
    OUTPUT_VIDEO_PATH = 'static/uploads/'

    # Other configuration options
    GAUSSIAN_BLUR_KERNEL = (5, 5)
    CANNY_LOW_THRESHOLD = 50
    CANNY_HIGH_THRESHOLD = 150
    HOUGH_THRESHOLD = 30
    HOUGH_MIN_LINE_LENGTH = 50
    HOUGH_MAX_LINE_GAP = 20
