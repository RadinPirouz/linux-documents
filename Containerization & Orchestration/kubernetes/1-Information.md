# Kubernetes (K8s) Documentation

## Overview  
**Kubernetes (K8s)** is an open-source container orchestration platform designed to automate the deployment, scaling, and operation of containerized applications.

---

## Control Plane (CP)  
The **Control Plane** is the core management component of a Kubernetes cluster. It makes global decisions about the cluster (e.g., scheduling), and it maintains the desired state of the cluster by managing workloads and directing communication within the system.  
> **Note:** By default, the Control Plane does not directly manage or run application containers.

### Key Components of the Control Plane:
- **API Server (`kube-apiserver`)**:  
  Exposes the Kubernetes API and serves as the entry point to the cluster. It handles communication between internal components and external clients.
  
- **Scheduler (`kube-scheduler`)**:  
  Assigns work (e.g., pods) to nodes based on resource availability and policies.

- **Controller Manager (`kube-controller-manager`)**:  
  Runs controllers that regulate the state of the cluster (e.g., Node Controller, Replication Controller, etc.).

- **etcd**:  
  A consistent, highly-available key-value store that stores all cluster data, configurations, and states. This is the "database" of Kubernetes.

---

## Worker Nodes  
Worker nodes are the machines where containerized applications run. Each worker node contains essential components for managing containers.

### Key Components of a Worker Node:
- **Kubelet**:  
  An agent that ensures containers are running as specified in their Pod definitions. It communicates with the Control Plane to receive and execute tasks.

- **Kube Proxy**:  
  Maintains network rules and handles routing for communication between services within the cluster and with external traffic.

---

## Data Flow  
- **Kubelet** and **Kube Proxy** on each worker node communicate with the **API Server** in the Control Plane for task execution and resource updates.
- The **Scheduler** assigns pods to nodes based on resource requirements, while the **Controller Manager** ensures that the cluster state remains consistent.

---

## Administration Tools  
- **`kubeadm`**:  
  A tool for bootstrapping Kubernetes clusters. It simplifies the setup and configuration of the Control Plane and worker nodes.

- **`kubectl`**:  
  The command-line interface (CLI) for interacting with the Kubernetes API. It is used to manage resources, deploy applications, and inspect cluster components.

---

## Kubernetes Version Compatibility  
### Kubernetes and Container Runtimes:
- **Kubernetes ≤ 1.23**:  
  Compatible with Docker as the default container runtime.
  
- **Kubernetes 1.24 to 1.25**:  
  Docker is not supported as a runtime. These versions require `containerd` or another Container Runtime Interface (CRI) implementation.
  
- **Kubernetes ≥ 1.25**:  
  Docker can be installed on the server but must be used indirectly through `containerd` or another CRI-compliant runtime. Docker itself is not a supported runtime.


