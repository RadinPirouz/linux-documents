## Docker Cheat Sheet

### Docker Data Directory
- **State Less:** Don't save your data like Nginx.
- **State Full:** Save your data.
  - `/var/lib/docker/` ==> Docker data directory

### Docker Commands

#### Login to Docker Hub
```bash
docker login
```

#### Pull Docker Image
```bash
docker pull <repo-addr>
```

#### Show Pulled Images
```bash
docker images
```

#### Run Docker Container
```bash
docker run <options> <image>
```
- **Options**:
  - `-it`: Run interactively and allocate a pseudo-TTY.
  - `-dit`: Run in detached mode with interactive TTY.

#### Go to Container Shell
```bash
docker exec -it <container name> bash
```

#### Remove Docker Container
```bash
docker rm <container name or ID>
```

#### Stop Docker Container
```bash
docker stop <container name or ID>
```

#### Stop and Remove Docker Container
```bash
docker rm -f <container name or ID>
```

#### List Docker Containers
```bash
docker ps -aq
```

#### List Exited Docker Containers
```bash
docker ps -aq -f status=exited
```

#### Remove Exited Docker Containers
```bash
docker rm $(docker ps -aq -f status=exited)
```

#### Remove All Stopped Containers
```bash
docker container prune
```

#### Container Configuration and Files
- `/var/lib/docker/containers/` ==> Container config and file directory

#### Get Container Information
```bash
docker inspect <container name or ID>
```

#### Get Container IP Address
```bash
docker inspect --format '{{ .NetworkSettings.IPAddress }}' <container name>
```

#### Copy Files Between Local and Container
```bash
docker cp <file_on_local> <container-name>:/<location>
docker cp <container-name>:/<location> <local_location>
```

#### Monitor Docker Container Statistics
```bash
docker stats
```

#### Run Container with Restart Policy
```bash
docker run -dit --name server --restart=always ubuntu
```

#### Create Custom Docker Image
```bash
docker commit <containername> <newname>
```

#### Save Docker Image to External File
```bash
docker save -o <file-location-and-name> <image-name>
```

#### Remove Docker Image
```bash
docker rmi -f <image-id>
```

#### Load Docker Image from File
```bash
docker load -i <file-location>
```
