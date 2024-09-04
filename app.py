import sys
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import cv2

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from lane_detector import detect_lanes
from config import Config

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling file upload and processing
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))

    if file:
        # Save the uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Process the uploaded image using lane detection
        image = cv2.imread(filepath)
        lane_image, edges_path, masked_edges_path, output_image_path = detect_lanes(image, file.filename)

        print("Edges Image Path: ", edges_path)  # Debugging
        print("Masked Edges Image Path: ", masked_edges_path)  # Debugging
        print("Output Image Path: ", output_image_path)  # Debugging

        # Make sure to only pass the filename (not the full path) to url_for
        return render_template('result.html', 
                               edges_img=os.path.basename(edges_path), 
                               masked_edges_img=os.path.basename(masked_edges_path), 
                               output_img=os.path.basename(output_image_path))

# Route to serve the uploaded and processed files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
