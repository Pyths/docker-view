from flask import Flask
from flask import jsonify
from shell_docker import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#check app running
@app.route('/')
def get_index():
    return "Docker View App is alive!"

#get image list from terminal
@app.route('/images')
def get_docker_images():
    return get_docker_images_json()

#get container list from terminal
@app.route('/containers')
def get_docker_containers():
    return get_docker_containers_json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8065')