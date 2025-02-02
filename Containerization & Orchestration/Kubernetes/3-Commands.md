

# Kubernetes Command Reference

This document provides a reference for common `kubectl` commands used for managing Kubernetes clusters. Use the examples and explanations below to help manage nodes, namespaces, pods, deployments, and more.

## Table of Contents

- [Kubernetes Command Reference](#kubernetes-command-reference)
  - [Table of Contents](#table-of-contents)
  - [General Commands](#general-commands)
  - [Node Management](#node-management)
  - [Namespace Management](#namespace-management)
  - [Pod Management](#pod-management)
    - [Listing Pods](#listing-pods)
    - [Running a Pod](#running-a-pod)
    - [Deleting a Pod](#deleting-a-pod)
  - [API Resources and Documentation](#api-resources-and-documentation)
  - [Logs and Pod Information](#logs-and-pod-information)
  - [Applying YAML Files](#applying-yaml-files)
  - [Managing Nodes and Labels](#managing-nodes-and-labels)
  - [Viewing Cluster Resources](#viewing-cluster-resources)
  - [ReplicaSet and Deployment Management](#replicaset-and-deployment-management)
  - [Additional Information](#additional-information)

---

## General Commands

- **List API Resources**

  ```bash
  kubectl api-resources
  ```

---

## Node Management

- **Show all nodes**

  ```bash
  kubectl get node
  ```

- **Set a label on a node**

  ```bash
  kubectl label nodes <node-name> kubernetes.io/<label-key>=<label-value>
  ```

---

## Namespace Management

- **List all namespaces**

  ```bash
  kubectl get namespaces
  # or the abbreviated version:
  kubectl get ns
  ```

- **Create a custom namespace**

  ```bash
  kubectl create ns <namespace-name>
  ```

---

## Pod Management

### Listing Pods

- **List pods in the default namespace**

  ```bash
  kubectl get pod
  ```

- **List pods with detailed information (wide output) in the default namespace**

  ```bash
  kubectl get pod -o wide
  ```

- **List pods with detailed information in a specific namespace**

  ```bash
  kubectl get pod -o wide -n <namespace-name>
  ```

### Running a Pod

- **Run a new pod**

  Use the following command structure to run a pod with various options:

  ```bash
  kubectl run <pod-name> <switch> {
    --image=<image-name>,                # Container image to use
    --port=<port-number>,                # Port that the container exposes
    -n <namespace-name>,                 # Namespace in which to run the pod
    --env="KEY=VALUE",                   # Environment variables for the container
    --command,                           # Treat the following arguments as the command
    --replicas=<number>,                 # Number of pod replicas to create
    --labels="key=value,key2=value2",    # Labels to assign to the pod(s)
    --dry-run=client,                    # Print the object without creating it
    --restart=<Always|OnFailure|Never>,  # Pod restart policy
    --overrides='<json>',                # JSON override for the generated object
    --image-pull-policy=<policy>,        # Image pull policy (Always, IfNotPresent, Never)
    --limits=cpu=<cpu>,memory=<memory>,   # Resource limits for the container
    --requests=cpu=<cpu>,memory=<memory>  # Resource requests for the container
  }
  ```

  - **Example:**

    ```bash
    kubectl run mypod --image=nginx --port=80 -n mynamespace \
      --env="ENV_VAR_NAME=VALUE" --command -- nginx -g "daemon off;" \
      --replicas=3 --labels="app=myapp,env=prod" --dry-run=client \
      --restart=Always --overrides='{"spec": {"containers": [{"name": "nginx", "image": "nginx"}]}}' \
      --image-pull-policy=IfNotPresent --limits=cpu=100m,memory=256Mi \
      --requests=cpu=50m,memory=128Mi
    ```

### Deleting a Pod

- **Delete a pod in a custom namespace**

  ```bash
  kubectl delete pod -n <namespace-name> <pod-name>
  ```

---

## API Resources and Documentation

- **Get documentation for an API resource**

  ```bash
  kubectl explain <api-resource-name>
  ```

  - *Example:*

    ```bash
    kubectl explain pod
    ```

---

## Logs and Pod Information

- **Stream logs for a running pod**

  ```bash
  kubectl logs -f -n <namespace-name> <pod-name>
  ```

- **Get detailed state and log information for a pod**

  ```bash
  kubectl describe pod -n <namespace-name> <pod-name>
  ```

---

## Applying YAML Files

- **Apply configuration from a YAML file to a specific namespace**

  ```bash
  kubectl apply -f <yaml-file> -n <namespace-name>
  ```

---

## Managing Nodes and Labels

- **Label a node with a custom key-value pair**

  ```bash
  kubectl label nodes <node-name> kubernetes.io/<label-key>=<label-value>
  ```

---

## Viewing Cluster Resources

- **Display all resources loaded in a namespace**

  ```bash
  kubectl get all -n <namespace-name>
  ```

- **Display replica sets, pods, and deployments in a specific namespace**

  ```bash
  kubectl get rs,pod,deployment -n <namespace-name>
  ```

---

## ReplicaSet and Deployment Management

- **Scale a ReplicaSet**

  ```bash
  kubectl scale rs <replicaset-name> -n <namespace-name> --replicas=<count>
  ```

- **View rollout history of a deployment**

  ```bash
  kubectl rollout history deployment -n <namespace-name> <deployment-name>
  ```

- **View details of a specific revision in a deployment's rollout history**

  ```bash
  kubectl rollout history deployment -n <namespace-name> <deployment-name> --revision <number>
  ```

- **Roll back a deployment to a specific revision**

  ```bash
  kubectl rollout undo deployment -n <namespace-name> <deployment-name> --to-revision=<number>
  ```

  > **Note:** The command for rolling back to a specific revision is `kubectl rollout undo` rather than using `--to-revision` with `kubectl rollout history`.

---

## Additional Information

- **Static Manifest Files**

  All YAML files located under `/etc/kubernetes/manifests/` are automatically loaded after a server reboot.

---
