# Docker Commands and Concepts

## Docker Concepts

- **Stateless**: Do not save your data (like Nginx).
- **Stateful**: Save your data.

## Docker Data Directory

- `/var/lib/docker/`: Docker data directory.
- `/var/lib/docker/containers/`: Container configuration and file directory.
- `/var/lib/docker/volumes`: Directory where docker volumes are saved.

## Docker Installtion (Ubuntu)
```bash
apt update && apt install ca-certificates curl && install -m 0755 -d /etc/apt/keyrings && curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc && chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
apt update && apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



## Docker CLI Commands

### Authentication

- `docker login`: Login to Docker Hub with CLI.

### Image Management

- `docker pull <repo-addr>`: Pull a Docker image.
- `docker images`: Show pulled images.
- `docker rmi -f <image-id>`: Remove an image.
- `docker save -o <file-location-and-name> <image-name>`: Save image as an external file.
- `docker load -i <file-location>`: Import a Docker image.

### Container Management

- `docker run <options> <img-name>`: Run a Docker container.
  - `docker run`: Run Docker (after run exited).
  - `docker run -it`: Run and give bash to me.
  - `docker run -dit`: Run and give bash to me and run in the background.
- `docker exec -it <container-name>`: Go to container shell.
- `docker rm <container-name>`: Remove Docker container.
- `docker stop <container-name>`: Stop Docker container.
- `docker rm -f <container-name>`: Stop and remove Docker container.
- `docker ps -aq`: Give all Docker container IDs.
- `docker ps -aq -f status=exited`: Give all Docker container IDs with exited status.
- `docker container prune`: Remove all stopped containers.
- `docker commit <container-name> <new-name>`: Make a custom Docker image.
- `docker inspect <container-name>`: Get all data about container information.
- `docker inspect --format '{{ .NetworkSettings.IPAddress }}' <container-name>`: Get IP of the container.
- `docker cp <file_on_local> <container-name>:/<location>`: Copy from local to container.
- `docker cp <container-name>:/<location> <local-location>`: Copy from container to local.
- `docker stats`: Monitor Docker stats.
- `docker run -dit --name server --restart=always ubuntu`: Run container again after restarting the service or main server.
- `docker build -t <appname>:<appver> <location-of-docker-file>`: Build Docker image from a Dockerfile.

### Volume Management

- `docker volume ls`: List all volumes.
- `docker volume create <name-of-volume>`: Create a volume for Docker.
- `docker volume inspect <vol-name>`: Give information about the volume.
- `docker run -dit --name <container-name> -v <volume-name>:<location-in-container> <img-name>`: Run Docker image and save target location data in volume.

### Network Management

- `docker network ls`: List all Docker networks.
- `docker network create <network-name>`: Create a Docker network.
- `docker network create --subnet <ip>/<subnet> --gateway <gateway-ip> --driver=<network-type> <net-name>`: Create network with custom settings.
- `docker run -dit --name <container-name> --network <network-name> <img-name>`: Run a container and connect it to a custom network.
- `docker network connect <network-name> <container-name>`: Connect a container to a custom network.
- `docker network disconnect <network-name> <container-name>`: Disconnect a network from a container.
