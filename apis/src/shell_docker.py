import subprocess

def get_docker_images_json():
    # sh: sudo docker image ls --format '{{json .}},'
    docker_images = subprocess.check_output(['sudo', 'docker', 'image', 'ls', '--format', "{{json .}},"])
    docker_images = "[" + docker_images.decode('utf-8')[:-2] + "]"
    print("LOGS:" + docker_images)
    return docker_images

def get_docker_containers_json():
    # sh: sudo docker container ls --format '{{json .}},' -a 
    docker_containers = subprocess.check_output(['sudo', 'docker', 'container', 'ls',  '--format', "{{json .}},", '-a'])
    docker_containers = "[" + docker_containers.decode('utf-8')[:-2] + "]"
    print("LOGS:" + docker_containers)
    return docker_containers
