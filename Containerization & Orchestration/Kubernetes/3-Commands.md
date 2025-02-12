Below is an improved version of your Kubernetes Command Reference. This revision enhances clarity, fixes typos, organizes related commands into logical sections, and standardizes formatting for readability.

---

# Kubernetes Command Reference

This document provides a concise reference for common `kubectl` commands used to manage Kubernetes clusters. Whether you’re managing nodes, namespaces, pods, deployments, or autoscaling, the examples below will help you perform everyday tasks with ease.

---

## Table of Contents

- [Kubernetes Command Reference](#kubernetes-command-reference)
  - [Table of Contents](#table-of-contents)
  - [General Commands](#general-commands)
  - [Node Management](#node-management)
    - [Listing Nodes](#listing-nodes)
    - [Labeling Nodes](#labeling-nodes)
    - [Node Maintenance (Cordon/Drain)](#node-maintenance-cordondrain)
  - [Namespace Management](#namespace-management)
  - [Pod Management](#pod-management)
    - [Listing Pods](#listing-pods)
    - [Running a Pod](#running-a-pod)
    - [Deleting a Pod](#deleting-a-pod)
  - [API Resources and Documentation](#api-resources-and-documentation)
  - [Logs and Pod Information](#logs-and-pod-information)
  - [Applying YAML Files](#applying-yaml-files)
  - [Viewing Cluster Resources](#viewing-cluster-resources)
  - [ReplicaSet and Deployment Management](#replicaset-and-deployment-management)
    - [Scaling and Rollouts](#scaling-and-rollouts)
    - [Autoscaling](#autoscaling)
  - [Additional Information](#additional-information)

---

## General Commands

- **List API Resources**

  Display all available API resources along with their short names:

  ```bash
  kubectl api-resources
  ```

---

## Node Management

### Listing Nodes

- **Show All Nodes**

  ```bash
  kubectl get nodes
  ```

### Labeling Nodes

- **Set a Custom Label on a Node**

  ```bash
  kubectl label node <node-name> kubernetes.io/<label-key>=<label-value>
  ```

  > **Note:** Replace `<node-name>`, `<label-key>`, and `<label-value>` with your desired values.

### Node Maintenance (Cordon/Drain)

- **Cordon a Node**  
  Prevent new pods from being scheduled on the node.

  ```bash
  kubectl cordon <node-name>
  ```

- **Uncordon a Node**  
  Mark the node as schedulable again.

  ```bash
  kubectl uncordon <node-name>
  ```

- **Drain a Node**  
  Evict all pods from the node (excluding those managed by DaemonSets).

  ```bash
  kubectl drain <node-name> --ignore-daemonsets --delete-local-data
  ```

  > **Warning:** Draining a node will evict running pods. Ensure this action is planned to avoid service disruption.

---

## Namespace Management

- **List All Namespaces**

  ```bash
  kubectl get namespaces
  # Or use the shorthand:
  kubectl get ns
  ```

- **Create a New Namespace**

  ```bash
  kubectl create namespace <namespace-name>
  ```

---

## Pod Management

### Listing Pods

- **List Pods in the Default Namespace**

  ```bash
  kubectl get pods
  ```

- **List Pods with Detailed Information (Wide Output)**

  ```bash
  kubectl get pods -o wide
  ```

- **List Pods in a Specific Namespace**

  ```bash
  kubectl get pods -o wide -n <namespace-name>
  ```

### Running a Pod

> **Note:** While `kubectl run` is a versatile command, note that in recent Kubernetes versions it is primarily used for running single pods (not deployments). For more complex configurations, consider using YAML manifests.

- **Basic Example:**

  ```bash
  kubectl run <pod-name> --image=<image-name> --port=<port-number> -n <namespace-name>
  ```

- **Advanced Example with Multiple Options:**

  ```bash
  kubectl run mypod --image=nginx --port=80 -n mynamespace \
    --env="ENV_VAR_NAME=VALUE" --command -- nginx -g "daemon off;" \
    --restart=Always --dry-run=client \
    --labels="app=myapp,env=prod" \
    --limits=cpu=100m,memory=256Mi --requests=cpu=50m,memory=128Mi
  ```

  **Common Options Explained:**

  - `--image`: Container image to use.
  - `--port`: Port exposed by the container.
  - `-n` or `--namespace`: Namespace in which to run the pod.
  - `--env`: Set environment variables.
  - `--command`: Treat the following arguments as the command to run.
  - `--restart`: Pod restart policy (`Always`, `OnFailure`, or `Never`).
  - `--labels`: Assign labels to the pod.
  - `--dry-run`: Validate the command without creating the pod.
  - `--limits` and `--requests`: Define resource limits and requests for the container.

### Deleting a Pod

- **Delete a Pod in a Specific Namespace**

  ```bash
  kubectl delete pod <pod-name> -n <namespace-name>
  ```

---

## API Resources and Documentation

- **Get Detailed Documentation for an API Resource**

  ```bash
  kubectl explain <api-resource-name>
  ```

  *Example:*

  ```bash
  kubectl explain pod
  ```

---

## Logs and Pod Information

- **Stream Logs for a Running Pod**

  ```bash
  kubectl logs -f -n <namespace-name> <pod-name>
  ```

- **Get Detailed Information About a Pod**

  ```bash
  kubectl describe pod <pod-name> -n <namespace-name>
  ```

---

## Applying YAML Files

- **Apply a Configuration from a YAML File**

  Apply a YAML configuration to a specific namespace:

  ```bash
  kubectl apply -f <yaml-file> -n <namespace-name>
  ```

---

## Viewing Cluster Resources

- **Display All Resources in a Namespace**

  ```bash
  kubectl get all -n <namespace-name>
  ```

- **Display ReplicaSets, Pods, and Deployments in a Specific Namespace**

  ```bash
  kubectl get rs,pods,deployments -n <namespace-name>
  ```

---

## ReplicaSet and Deployment Management

### Scaling and Rollouts

- **Scale a ReplicaSet**

  ```bash
  kubectl scale rs <replicaset-name> --replicas=<count> -n <namespace-name>
  ```

- **View Rollout History of a Deployment**

  ```bash
  kubectl rollout history deployment <deployment-name> -n <namespace-name>
  ```

- **View Details of a Specific Revision**

  ```bash
  kubectl rollout history deployment <deployment-name> -n <namespace-name> --revision=<number>
  ```

- **Roll Back a Deployment to a Specific Revision**

  ```bash
  kubectl rollout undo deployment <deployment-name> -n <namespace-name> --to-revision=<number>
  ```

### Autoscaling

- **Autoscale a Deployment**

  Automatically scale a deployment based on CPU utilization:

  ```bash
  kubectl autoscale deployment <deployment-name> -n <namespace-name> --cpu-percent=<target-cpu-percentage> --min=<min-pods> --max=<max-pods>
  ```

- **View Horizontal Pod Autoscalers (HPA)**

  ```bash
  kubectl get hpa -n <namespace-name>
  ```

---

## Additional Information

- **Static Manifest Files**

  Any YAML files placed in `/etc/kubernetes/manifests/` are automatically loaded when the kubelet starts (for example, after a server reboot).
