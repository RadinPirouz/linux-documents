# Docker Swarm Documentation

This guide covers key commands and workflows for managing a Docker Swarm cluster. It includes information on initializing the cluster, node management, service management, and best practices to ensure your cluster remains operational.

---

## Table of Contents

1. [Cluster Health & Manager Count](#cluster-health--manager-count)
2. [Example Workflow: Setting Up Nginx](#example-workflow-setting-up-nginx)
3. [Cluster Initialization and Management](#cluster-initialization-and-management)
4. [Node Management](#node-management)
5. [Service Management](#service-management)
6. [Join Tokens](#join-tokens)

---

## Cluster Health & Manager Count

To maintain a healthy and functional Docker Swarm cluster, **the number of manager nodes must exceed 50% of the total nodes**. If the manager nodes fall below 51% of the cluster, the system will lose quorum and become non-operational. Always monitor your manager count to ensure high availability.

---

## Example Workflow: Setting Up Nginx

When deploying services such as Nginx, the typical workflow in Docker Swarm is:

1. **API**: Handle incoming requests.
2. **Allocator**: Distribute workload to available nodes.
3. **Dispatcher**: Manage task assignments.
4. **Scheduler**: Ensure tasks run on the optimal nodes.

This workflow ensures that your service is efficiently distributed and scaled across the cluster.

---

## Cluster Initialization and Management

### Create Cluster

Initialize a new Docker Swarm cluster:
```bash
docker swarm init
```
This command sets up the current node as the manager of a new cluster.

### Create Cluster with a Specific Interface

Specify an IP address or interface name when initializing the cluster:
```bash
docker swarm init --advertise-addr <ip or interface name>
```
This ensures that the node advertises the correct network interface for other nodes to join.

### Join Cluster

Add a node to an existing Docker Swarm cluster:
```bash
docker swarm join
```

### Leave Cluster

Remove a node from the cluster:
```bash
docker swarm leave
```

### Unlock Locked Manager

Unlock a manager node that has been locked:
```bash
docker swarm unlock
```

---

## Node Management

### List Nodes

View the status and details of all nodes in your cluster:
```bash
docker node ls
```
**Example Output:**
```
ID                            HOSTNAME   STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
8yw8jrjeqczaci0qkuy060g09 *   docker-1   Ready     Active         Leader           24.0.5
v4gvf7xenw0izmxgvhr6hb2rj     docker-2   Ready     Active                          24.0.5
kd3ujmt1ey3pw6v9189fouxfa     docker-3   Ready     Active         Reachable        24.0.5
tm1msy58ztcltt36rs1lb76p7     docker-4   Down      Active                          24.0.5
```

### Remove Node

Remove a node from the cluster by specifying its ID:
```bash
docker node rm <node-id>
```
**Example:**
```bash
docker node rm tm1msy58ztcltt36rs1lb76p7
```

### Promote Node to Manager

Upgrade a worker node to a manager node:
```bash
docker node promote <hostname or ID>
```
**Example:**
```bash
docker node promote v4gvf7xenw0izmxgvhr6hb2rj
```
This command promotes the specified node, enabling it to participate in cluster management decisions.

---

## Service Management

### Show Task Status on Cluster

Display the status of tasks running on each node:
```bash
docker node ps
```

### List Services

List all services currently running in the cluster:
```bash
docker service ls
```

### Create Service

Create a new service with the specified name and Docker image:
```bash
docker service create --name <service-name> <image-name>
```

### Scale Service

Adjust the number of replicas for an existing service:
```bash
docker service scale <service-name>=<replica-count>
```
**Example:**
```bash
docker service scale nginx=5
```
This command scales the `nginx` service to 5 replicas.

### Inspect Service

View detailed information about a specific service:
```bash
docker service inspect <service-name>
```

### Create Service with Replicas and Environment Variables

Launch a new service with multiple replicas, environment variables, and port publishing:
```bash
docker service create --name <service-name> --replicas <replica-count> --env <env-variable> --publish <host-port>:<container-port> <image-name>
```
**Example:**
```bash
docker service create --name nginx --replicas 3 --env MY_ENV_VAR=value --publish 8080:80 nginx
```
This creates an `nginx` service with 3 replicas, sets the environment variable `MY_ENV_VAR` to `value`, and maps port 8080 on the host to port 80 in the container.

---

## Join Tokens

To securely add new nodes to the swarm, use the join tokens provided by Docker Swarm.

### Get Worker Join Token

Display the token required for a node to join as a worker:
```bash
docker swarm join-token worker
```

### Get Manager Join Token

Display the token required for a node to join as a manager:
```bash
docker swarm join-token manager
```
