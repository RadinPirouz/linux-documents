# **Docker Commands Guide**

## **1. Docker Data Directory**
Docker stores its critical files like images, containers, and volumes in specific directories. These are essential for Docker's operation.

- **`/var/lib/docker/`**: The main directory where Docker stores all its data.
- **`/var/lib/docker/containers/`**: Contains configuration files for individual containers.
- **`/var/lib/docker/volumes/`**: Stores data for Docker volumes, enabling persistent storage beyond container lifetimes.

---

## **2. Installing Docker on Ubuntu**

Follow these steps to install Docker on Ubuntu.

### **Step 1: Update package list and install required packages**
```bash
sudo apt update && sudo apt install -y ca-certificates curl
```
- **`sudo apt update`**: Refreshes the local package list to ensure you download the latest versions.
- **`sudo apt install -y ca-certificates curl`**: Installs essential tools like `ca-certificates` and `curl` for secure downloads.

### **Step 2: Add Docker’s GPG key**
```bash
sudo install -m 0755 -d /etc/apt/keyrings 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc 
sudo chmod a+r /etc/apt/keyrings/docker.asc
```
- **`install -m 0755 -d /etc/apt/keyrings`**: Creates the `/etc/apt/keyrings` directory with the appropriate permissions.
- **`curl -fsSL <url> -o <file>`**: Downloads Docker’s GPG key securely.
- **`chmod a+r`**: Ensures the GPG key file is readable by all users.

### **Step 3: Add Docker’s official repository**
```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
- This command adds Docker's official repository to your Apt sources list.

### **Step 4: Install Docker**
```bash
sudo apt update && sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
- **`docker-ce`**: Installs Docker Community Edition.
- **`docker-ce-cli`**: The Docker command-line interface.
- **`containerd.io`**: Container runtime.
- **`docker-buildx-plugin`**: Advanced build functionality.
- **`docker-compose-plugin`**: Tool for managing multi-container applications.

---

## **3. Docker CLI Commands**

### **3.1 Authentication**
```bash
docker login
```
- **`docker login`**: Prompts for credentials to log in to Docker Hub or a private registry.

### **3.2 Image Management**
```bash
docker pull <repo-addr>
```
- **`docker pull <repo-addr>`**: Downloads an image from the specified repository.

```bash
docker images
```
- **`docker images`**: Lists all images on your system.

```bash
docker rmi -f <image-id>
```
- **`docker rmi -f <image-id>`**: Forcefully removes the specified image.

```bash
docker save -o <file-location-and-name> <image-name>
```
- **`docker save -o <file-location>`**: Saves an image as a `.tar` file.

```bash
docker load -i <file-location>
```
- **`docker load -i <file-location>`**: Loads an image from a `.tar` file.

---

### **3.3 Container Management**

```bash
docker run <options> <img-name>
```
- **`docker run <img-name>`**: Runs a container from the specified image.

```bash
docker run -it nginx
```
- **`docker run -it`**: Runs a container interactively with a terminal.

```bash
docker run -dit nginx
```
- **`docker run -dit`**: Runs a container in detached mode (background).

```bash
docker run -dit --restart=always nginx
```

```bash
docker run -dit --restart=always nginx
```

```bash
docker run -dit --name <container-name> nginx
```
- Creates a named container.

```bash
docker run -dit --hostname=<hostname-sv> nginx
```
- Assigns a hostname to the container.

```bash
docker run -dit -e var1=data --name <container-name> --hostname=<hostname-sv> nginx
```
- Sets environment variables and runs a container with a custom name and hostname.

```bash
docker run -dit -p <sv_port>:<container_port>  nginx
```
- Maps a host port to a container port.

```bash
docker run -dit -p <sv_port_from>-<sv_port_to>:<container_port_from>-<container_port_to>  nginx
```
- Maps a range of ports between host and container.

```bash
docker run -dit -p 127.0.0.1:<sv_port_from>-<sv_port_to>:<container_port_from>-<container_port_to>  nginx
```
- Binds container ports to specific IP addresses on the host.

```bash
docker logs -f
```
- **`docker logs -f`**: Streams logs of a container in real-time.


```bash
docker events
```


```bash
docker exec -it <container-name>
```
- **`docker exec -it <container-name>`**: Opens an interactive terminal inside a running container.

```bash
docker stop <container-name>
```
- **`docker stop <container-name>`**: Stops a running container.

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
- **`docker ps -aq`**: Lists all container IDs, including stopped ones.

```bash
docker ps -aq -f status=exited
```
- **`docker ps -aq -f status=exited`**: Lists only the stopped container IDs.

```bash
docker container prune
```
- **`docker container prune`**: Removes all stopped containers.

```bash
docker commit <container-name> <new-image-name>
```
- **`docker commit <container-name> <new-image-name>`**: Creates a new image from a running or stopped container.

```bash
docker inspect <container-name>
```
- **`docker inspect <container-name>`**: Displays detailed information about a container.

```bash
docker inspect --format '{{ .NetworkSettings.IPAddress }}' <container-name>
```
- **`docker inspect --format '{{ .NetworkSettings.IPAddress }}' <container-name>`**: Retrieves the container's IP address.

```bash
docker cp <file_on_local> <container-name>:/<location>
```
`-A` : use for archive mode (keep permmision and )
- **`docker cp <file_on_local> <container-name>:/<location>`**: Copies files from local machine to the container.

```bash
docker cp <container-name>:/<location> <local-location>
```
- **`docker cp <container-name>:/<location> <local-location>`**: Copies files from the container to the local machine.

```bash
docker stats
```
- **`docker stats`**: Displays a real-time stream of resource usage for all running containers.

```bash
docker build -t <app-name>:<app-ver> <path-to-dockerfile>
```
- **`docker build -t <app-name>:<app-ver> <path-to-dockerfile>`**: Builds a Docker image using a Dockerfile.

---

## **4. Volume Management**

```bash
docker volume ls
```
- **`docker volume ls`**: Lists all Docker volumes.

```bash
docker volume create <volume-name>
```
- **`docker volume create <volume-name>`**: Creates a new volume.

```bash
docker volume inspect <volume-name>
```
- **`docker volume inspect <volume-name>`**: Shows detailed information about a volume.

```bash
docker run -dit --name <container-name> -v <volume-name>:<container-location> <image-name>
```
- **`docker run -v <volume-name>:<container-location>`**: Attaches a volume to a container.

---

## **5. Network Management**

```bash
docker network ls
```
- **`docker network ls`**: Lists all Docker networks.

```bash
docker network create <network-name>
```
- **`docker network create <network-name>`**: Creates a new Docker network.

```bash
docker network create --subnet <ip>/<subnet> --gateway <gateway-ip> --driver=<network-type> <network-name>
```
- **`docker network create --subnet <ip>/<subnet> --gateway <gateway-ip> --driver=<network-type> <network-name>`**: Creates a custom network with specified settings.

```bash
docker run -dit --name <container-name> --network <network-name> <image-name>
```
- **`docker run --network <network-name>`**: Runs a container on a specified network.

```bash
docker network connect <network-name> <container-name>
```


- **`docker network connect <network-name> <container-name>`**: Connects an existing container to a network.

```bash
docker network inspect <network-name>
```
- **`docker network inspect <network-name>`**: Displays detailed information about a network.

```bash
docker network disconnect <network-name> <container-name>
```
- **`docker network disconnect <network-name> <container-name>`**: Disconnects a container from a network.

