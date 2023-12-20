#Deploy Docker Containers with Docker Compose:

import subprocess

def deploy_docker_compose(compose_file):
    subprocess.run(f"docker-compose -f {compose_file} up -d", shell=True)

def stop_docker_compose(compose_file):
    subprocess.run(f"docker-compose -f {compose_file} down", shell=True)

# Example usage:
deploy_docker_compose(compose_file='docker-compose.yml')
