# Docker Commands Guide

## Docker Data Directory
Docker stores its files, such as images, containers, and volumes, in specific directories. These are essential for Docker's operation.

- **`/var/lib/docker/`**: This is Docker's primary data directory where all data related to Docker is stored.
- **`/var/lib/docker/containers/`**: Contains the configurations and files for individual Docker containers.
- **`/var/lib/docker/volumes/`**: Stores the data for Docker volumes, which allow persistent data storage outside of containers.

---

## Installing Docker on Ubuntu

Here’s a step-by-step explanation of the commands used to install Docker on Ubuntu.

```bash
# Update the package list and install required packages
sudo apt update && sudo apt install -y ca-certificates curl
```
- **`sudo apt update`**: Updates the local package list to ensure you're downloading the latest versions.
- **`sudo apt install -y ca-certificates curl`**: Installs essential packages like `ca-certificates` and `curl` for secure communication and downloading files.

```bash
# Create a directory for Docker's GPG key and download it
sudo install -m 0755 -d /etc/apt/keyrings 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc 
sudo chmod a+r /etc/apt/keyrings/docker.asc
```
- **`install -m 0755 -d /etc/apt/keyrings`**: Creates the directory `/etc/apt/keyrings` with the correct permissions for storing GPG keys.
- **`curl -fsSL <url> -o <file>`**: Downloads Docker’s GPG key securely and stores it as `docker.asc`.
- **`chmod a+r`**: Gives read permission to all users for the GPG key file.

```bash
# Add Docker's official repository to Apt sources
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
- **`dpkg --print-architecture`**: Determines the system's architecture (e.g., `amd64`).
- **`os-release`**: Fetches the OS version to ensure the correct Docker version is downloaded for your system.

```bash
# Update the package list and install Docker
sudo apt update && sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
- **`docker-ce`**: Installs Docker Community Edition.
- **`docker-ce-cli`**: Installs the Docker command-line interface.
- **`containerd.io`**: Installs Containerd, a container runtime used by Docker.
- **`docker-buildx-plugin`**: Installs Docker Buildx, an advanced image builder.
- **`docker-compose-plugin`**: Installs Docker Compose, which helps manage multi-container applications.

---

## Docker CLI Commands

### Authentication

```bash
docker login
```
- **`docker login`**: Authenticates your Docker CLI with Docker Hub or a private registry by prompting for credentials.

---

### Image Management
Image management commands help you interact with Docker images: downloading, saving, loading, and removing images.

```bash
docker pull <repo-addr>
```
- **`docker pull <repo-addr>`**: Downloads a Docker image from the specified repository (e.g., Docker Hub).

```bash
docker images
```
- **`docker images`**: Lists all Docker images stored on your system.

```bash
docker rmi -f <image-id>
```
- **`docker rmi -f <image-id>`**: Forcefully removes a Docker image from your system. Use caution as this will permanently delete the image.

```bash
docker save -o <file-location-and-name> <image-name>
```
- **`docker save -o <file-location> <image-name>`**: Saves a Docker image as a tar archive file. Useful for transferring images.

```bash
docker load -i <file-location>
```
- **`docker load -i <file-location>`**: Loads a Docker image from a tar archive file.

---

### Container Management
These commands allow you to create, run, manage, and remove containers.

```bash
docker run <options> <img-name>
```
- **`docker run <img-name>`**: Runs a Docker container based on the specified image. Add options for more customization.

```bash
docker run -it
```
- **`docker run -it`**: Runs a container in interactive mode with a terminal.

```bash
docker run -dit
```
- **`docker run -dit`**: Runs a container in detached mode with a terminal, meaning it runs in the background.

```bash
docker exec -it <container-name>
```
- **`docker exec -it <container-name>`**: Opens an interactive terminal inside a running container.

```bash
docker stop <container-name>
```
- **`docker stop <container-name>`**: Stops a running container gracefully.

```bash
docker rm <container-name>
```
- **`docker rm <container-name>`**: Removes a stopped container.

```bash
docker rm -f <container-name>
```
- **`docker rm -f <container-name>`**: Forcefully stops and removes a running container.

```bash
docker ps -aq
```
- **`docker ps -aq`**: Lists all container IDs, both running and stopped.

```bash
docker ps -aq -f status=exited
```
- **`docker ps -aq -f status=exited`**: Lists the container IDs of all stopped (exited) containers.

```bash
docker container prune
```
- **`docker container prune`**: Removes all stopped containers.

```bash
docker commit <container-name> <new-image-name>
```
- **`docker commit <container-name> <new-image-name>`**: Creates a new Docker image from an existing container.

```bash
docker inspect <container-name>
```
- **`docker inspect <container-name>`**: Displays detailed information about a container’s configuration and state.

```bash
docker inspect --format '{{ .NetworkSettings.IPAddress }}' <container-name>
```
- **`docker inspect --format '{{ .NetworkSettings.IPAddress }}' <container-name>`**: Retrieves the IP address of a specific container.

```bash
docker cp <file_on_local> <container-name>:/<location>
```
- **`docker cp <file_on_local> <container-name>:/<location>`**: Copies a file from your local system to a Docker container.

```bash
docker cp <container-name>:/<location> <local-location>
```
- **`docker cp <container-name>:/<location> <local-location>`**: Copies a file from a Docker container to your local system.

```bash
docker stats
```
- **`docker stats`**: Displays a live stream of resource usage statistics for all running containers.

```bash
docker build -t <app-name>:<app-ver> <path-to-dockerfile>
```
- **`docker build -t <app-name>:<app-ver> <path-to-dockerfile>`**: Builds a Docker image from a Dockerfile located at the specified path.

---

### Volume Management
Docker volumes are used to persist data between container restarts. These commands manage those volumes.

```bash
docker volume ls
```
- **`docker volume ls`**: Lists all Docker volumes available on your system.

```bash
docker volume create <volume-name>
```
- **`docker volume create <volume-name>`**: Creates a new volume with the specified name.

```bash
docker volume inspect <volume-name>
```
- **`docker volume inspect <volume-name>`**: Displays detailed information about the specified volume.

```bash
docker run -dit --name <container-name> -v <volume-name>:<container-location> <image-name>
```
- **`docker run -v <volume-name>:<container-location>`**: Runs a container and mounts the specified volume at the given location inside the container.

---

### Network Management
These commands help manage Docker networks, enabling containers to communicate with each other.

```bash
docker network ls
```
- **`docker network ls`**: Lists all Docker networks on your system.

```bash
docker network create <network-name>
```
- **`docker network create <network-name>`**: Creates a new Docker network.

```bash
docker network create --subnet <ip>/<subnet> --gateway <gateway-ip> --driver=<network-type> <network-name>
```
- **`docker network create --subnet <ip>/<subnet> --gateway <gateway-ip> --driver=<network-type> <network-name>`**: Creates a custom Docker network with specified settings (subnet, gateway, and driver).

```bash
docker run -dit --name <container-name> --network <network-name> <image-name>
```
- **`docker run --network <network-name>`**: Runs a container and connects it to the specified network.

```bash
docker network connect <network-name> <container-name>
```
- **`docker network connect <network-name> <container

-name>`**: Connects an existing container to the specified network.

```bash
docker network disconnect <network-name> <container-name>
```
- **`docker network disconnect <network-name> <container-name>`**: Disconnects the specified container from the network.
