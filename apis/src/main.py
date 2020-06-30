from flask import Flask
from flask import jsonify


app = Flask(__name__)

#check app running
@app.route('/')
def get_index():
    return "Docker View App is alive!"

#get image list from terminal
@app.route('/images')
def get_docker_images():
    return "List of images"

#get container list from terminal
@app.route('/containers')
def get_docker_containers():
    return "List of containers"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8065')