# Kubernetes YAML Files

This document provides explanations and details for various Kubernetes YAML configurations, describing how different Kubernetes objects such as Namespaces, Pods, and other specifications are defined and utilized. The examples cover creating namespaces, deploying pods, setting resource limits, and using node selectors.

## Namespace Definition

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: my-ns
```

- **apiVersion**: Specifies the version of the Kubernetes API.
- **kind**: Defines the type of Kubernetes object, here it's a `Namespace`.
- **metadata**: Contains data that helps uniquely identify the object, including a `name`.

This YAML file creates a namespace named `my-ns` which isolates a group of resources within Kubernetes.

## Pod Definitions

### Nginx Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  namespace: my-ns
  name: nginx-pod
  labels:
    app: app1
    zone: staging
    version: v1.0.1
    app.kubernetes.io/product: nginx-pod
spec:
  containers:
    - name: naginx-container
      image: nginx:latest
      ports:
        - containerPort: 80
```

- **metadata.namespace**: Specifies the namespace the pod belongs to (`my-ns`).
- **metadata.name**: The name of the pod (`nginx-pod`).
- **metadata.labels**: Key-value pairs for organizing and selecting resources.
- **spec.containers**: Specifies the containers within the pod. Each container has:
  - **name**: Container name.
  - **image**: The Docker image to run (`nginx:latest`).
  - **ports**: List of ports to expose from the container (`containerPort: 80`).

This file defines a pod named `nginx-pod` running the latest Nginx container in the `my-ns` namespace.

### Test Pod 1

```yaml
apiVersion: v1
kind: Pod
metadata:
  namespace: my-ns
  name: testpod1
spec:
  containers:
    - name: c00
      image: ubuntu
      command: ["/bin/bash", "-c", "while true; do echo Hello-Coder; sleep 5 ; done"]
    - name: c01
      image: ubuntu
      command: ["/bin/bash", "-c", "while true; do echo Hello-Programmer; sleep 5 ; done"]
```

- **spec.containers.command**: Overrides the default command for the container, in this case, running a looped bash script that prints a message every 5 seconds.

This defines a pod named `testpod1` with two Ubuntu containers in the `my-ns` namespace, each running a different command.

## Pod with Resource Requests and Limits

```yaml
apiVersion: v1
kind: Pod
metadata:
  namespace: my-ns
  name: testpod1
spec:
  containers:
    - name: c00
      image: ubuntu
      command:
        - /bin/bash
        - -c
        - while true; do echo Hello-Coder; sleep 5 ; done
    - name: c01
      image: ubuntu
      command:
        - /bin/bash
        - -c
        - while true; do echo Hello-Programmer; sleep 5 ; done
      resources:
        limits:
          memory: "128Mi"
          cpu: "500m"
        requests:
          memory: "64Mi"
          cpu: "250m"
```

- **resources.limits**: Specifies the maximum amount of resources a container can use.
- **resources.requests**: Specifies the amount of resources a container is guaranteed.

This pod configuration defines resource limits and requests for the containers to ensure they do not exceed specific memory and CPU usage.

## Pod with NodeSelector

```yaml
apiVersion: v1
kind: Pod
metadata:
  namespace: my-ns
  name: testpod3
spec:
  containers:
    - name: c00
      image: ubuntu
      command:
        - /bin/bash
        - -c
        - while true; do echo Hello-Coder; sleep 5 ; done
    - name: c01
      image: ubuntu
      command:
        - /bin/bash
        - -c
        - while true; do echo Hello-Programmer; sleep 5 ; done
      resources:
        limits:
          memory: "128Mi"
          cpu: "500m"
        requests:
          memory: "64Mi"
          cpu: "250m"
  nodeSelector:
    kubernetes.io/hostname: k8s2
    kubernetes.io/disk: ssd
```

- **nodeSelector**: Ensures the pod is scheduled on nodes with the specified labels (`kubernetes.io/hostname: k8s2` and `kubernetes.io/disk: ssd`).

This configuration places the pod on specific nodes that match the given labels.

## Simple Pod Templates

### Basic Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp
  labels:
    name: myapp
spec:
  containers:
  - name: myapp
    image: <Image>
    resources:
      limits:
        memory: "128Mi"
        cpu: "500m"
    ports:
      - containerPort: <Port>
```

This is a template for a basic pod named `myapp` with configurable image and port settings.

### Nginx Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  labels:
    app: MyApp
spec:
  containers:
  - name: my-container
    image: nginx:latest
    ports:
    - containerPort: 80
```

This defines a pod named `my-pod` running an Nginx container exposing port 80.

## Useful Kubernetes Commands

### View Pod Details

```bash
kubectl get pod -n my-ns <pod-name> -o yaml
```

This command retrieves and displays the YAML configuration of the pod `testpod1` in the namespace `my-ns`.

### Label a Node

```bash
kubectl label node <node-name> kubernetes.io/<var-name>=<var-value>
kubectl get nodes --show-labels
```
