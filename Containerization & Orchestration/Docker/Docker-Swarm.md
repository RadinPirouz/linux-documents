# Docker Swarm Documentation

## Manager Count

To ensure the cluster remains functional, the number of manager nodes must be more than 50%. If it falls below 51%, the cluster will become non-operational.

## Example: Setting Up Nginx

**Workflow:** API → Allocator → Dispatcher → Scheduler

## Commands

### Cluster Initialization and Management

- **Create Cluster**
  ```bash
  docker swarm init
  ```
  Initializes a new Docker Swarm cluster.

- **Join Cluster**
  ```bash
  docker swarm join
  ```
  Joins a node to an existing Docker Swarm cluster.

- **Create Cluster with Specific Interface**
  ```bash
  docker swarm init --advertise-addr <ip or interface name>
  ```
  Initializes a new Docker Swarm cluster, specifying the IP or interface name to advertise.

- **Leave Cluster**
  ```bash
  docker swarm leave
  ```
  Removes a node from the Docker Swarm cluster.

- **Unlock Locked Manager**
  ```bash
  docker swarm unlock
  ```
  Unlocks a locked manager node in the Docker Swarm cluster.

### Node Management

- **List Nodes**
  ```bash
  docker node ls
  ```
  Displays information about the nodes in the cluster.
  
  **Example Output:**
  ```bash
  docker node ls
  ```

  ```
  ID                            HOSTNAME   STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
  8yw8jrjeqczaci0qkuy060g09 *   docker-1   Ready     Active         Leader           24.0.5
  v4gvf7xenw0izmxgvhr6hb2rj     docker-2   Ready     Active                          24.0.5
  kd3ujmt1ey3pw6v9189fouxfa     docker-3   Ready     Active         Reachable        24.0.5
  tm1msy58ztcltt36rs1lb76p7     docker-3   Down      Active                          24.0.5
  ```

- **Remove Node**
  ```bash
  docker node rm <node-id>
  ```
  Removes a node from the cluster.
  
  **Example:**
  ```bash
  docker node rm tm1msy58ztcltt36rs1lb76p7
  ```

- **Promote Node to Manager**
  ```bash
  docker node promote <hostname or ID>
  ```
  Promotes a worker node to a manager node.
  
  **Example:**
  ```bash
  root@docker-1:~# docker node promote v4gvf7xenw0izmxgvhr6hb2rj
  Node v4gvf7xenw0izmxgvhr6hb2rj promoted to a manager in the swarm.
  ```

### Service Management

- **Show Task Status on Cluster**
  ```bash
  docker node ps
  ```
  Displays the status of tasks running on nodes in the cluster.

- **List Services**
  ```bash
  docker service ls
  ```
  Lists all services running in the cluster.

- **Create Service**
  ```bash
  docker service create --name <service-name> <image-name>
  ```
  Creates a new service with the specified name and image.

- **Scale Service**
  ```bash
  docker service scale <service-name>=<replica-count>
  ```
  Scales the number of replicas for a service.
  
  **Example:**
  ```bash
  docker service scale nginx=5
  ```
  Scales the `nginx` service to 5 replicas.

- **Inspect Service**
  ```bash
  docker service inspect <service-name>
  ```
  Displays detailed information about a service.

- **Create Service with Replicas and Environment Variables**
  ```bash
  docker service create --name <service-name> --replicas <replica-count> --env <env-variable> <image-name>
  ```
  Creates a new service with the specified name, number of replicas, and environment variables.
  
  **Example:**
  ```bash
  docker service create --name nginx --replicas 3 --env MY_ENV_VAR=value nginx
  ```
  Creates an `nginx` service with 3 replicas and an environment variable `MY_ENV_VAR` set to `value`.
