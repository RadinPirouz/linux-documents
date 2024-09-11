# Docker Commands Guide

## Docker Data Directory

- **`/var/lib/docker/`**: The main Docker data directory.
- **`/var/lib/docker/containers/`**: Directory containing container configurations and files.
- **`/var/lib/docker/volumes/`**: Directory where Docker volumes are stored.

## Installing Docker on Ubuntu

To install Docker on Ubuntu, run the following commands:

```bash
# Update the package list and install required packages
sudo apt update && sudo apt install -y ca-certificates curl 

# Create a directory for Docker's GPG key and download it
sudo install -m 0755 -d /etc/apt/keyrings 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc 
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add Docker's official repository to Apt sources
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update the package list and install Docker
sudo apt update && sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## Docker CLI Commands

### Authentication

```bash
docker login
```

### Image Management

```bash
docker pull <repo-addr>                     # Pull a Docker image from a repository
docker images                               # List all Docker images on your system
docker rmi -f <image-id>                    # Force remove a Docker image
docker save -o <file-location-and-name> <image-name>  # Save a Docker image as a file
docker load -i <file-location>              # Load a Docker image from a file
```

### Container Management

```bash
docker run <options> <img-name>             # Run a Docker container with specified options
docker run                                  # Run a Docker container
docker run -it                              # Run a container in interactive mode with a terminal
docker run -dit                             # Run a container in detached mode with a terminal
docker exec -it <container-name>            # Access the shell of a running container
docker stop <container-name>                # Stop a running Docker container
docker rm <container-name>                  # Remove a stopped Docker container
docker rm -f <container-name>               # Forcefully stop and remove a Docker container
docker ps -aq                               # List the IDs of all containers (running and stopped)
docker ps -aq -f status=exited              # List the IDs of all exited containers
docker container prune                      # Remove all stopped containers
docker commit <container-name> <new-name>   # Create a new image from a container’s changes
docker inspect <container-name>             # Display detailed information about a container
docker inspect --format '{{ .NetworkSettings.IPAddress }}' <container-name>  # Get the IP address of a container
docker cp <file_on_local> <container-name>:/<location>  # Copy a file from the local system to a container
docker cp <container-name>:/<location> <local-location>  # Copy a file from a container to the local system
docker stats                                # Display a live stream of container resource usage statistics
docker run -dit --name server --restart=always ubuntu  # Run a container that automatically restarts on server or service restarts
docker build -t <appname>:<appver> <location-of-dockerfile>  # Build a Docker image from a Dockerfile
```

### Volume Management

```bash
docker volume ls                            # List all Docker volumes
docker volume create <name-of-volume>       # Create a new Docker volume
docker volume inspect <vol-name>            # Display detailed information about a volume
docker run -dit --name <container-name> -v <volume-name>:<location-in-container> <img-name>  # Run a container with a mounted volume
```

### Network Management

```bash
docker network ls                           # List all Docker networks
docker network create <network-name>        # Create a new Docker network
docker network create --subnet <ip>/<subnet> --gateway <gateway-ip> --driver=<network-type> <net-name>  # Create network with custom settings
docker run -dit --name <container-name> --network <network-name> <img-name>  # Run a container and connect it to a specified network
docker network connect <network-name> <container-name>  # Connect an existing container to a network
docker network disconnect <network-name> <container-name>  # Disconnect a container from a network
```