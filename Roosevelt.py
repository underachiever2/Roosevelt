import os
from flask import Flask, request, jsonify, render_template
import shutil

# Set up Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_text_form')
def generate_text_form():
    return render_template('generate_text_form.html')

@app.route('/generate_text', methods=['POST'])
def generate_text():
    prompt = request.form.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    # Example of generating text using OpenAI (API key must be set as environment variable)
    # Here, we simply return the prompt for demonstration
    return jsonify({'response': f'Generated text for prompt: {prompt}'})

@app.route('/create_image_form')
def create_image_form():
    return render_template('create_image_form.html')

@app.route('/create_image', methods=['POST'])
def create_image():
    color = request.form.get('color', 'blue')
    width = int(request.form.get('width', 100))
    height = int(request.form.get('height', 100))

    # Example of creating an image (PIL must be installed)
    image = Image.new('RGB', (width, height), color=color)
    image_path = 'image.png'
    image.save(image_path)

    return jsonify({'message': f'Image created with color {color} and size ({width}, {height})', 'path': image_path})

@app.route('/clone_files_form')
def clone_files_form():
    return render_template('clone_files_form.html')

@app.route('/clone_files', methods=['POST'])
def clone_files():
    source_dir = request.form.get('source_dir')
    dest_dir = request.form.get('dest_dir')
    
    if not source_dir or not dest_dir:
        return jsonify({'error': 'Source or destination directory not provided'}), 400

    try:
        shutil.copytree(source_dir, dest_dir)
        return jsonify({'message': f'Files cloned from {source_dir} to {dest_dir}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/automate_task', methods=['GET'])
def automate_task():
    return jsonify({'message': 'Automate task functionality is currently not implemented.'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
