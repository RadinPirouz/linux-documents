# Kubernetes

## `kubectl` Command Reference

### Get State of API Resources
```bash
kubectl api-resources
```

### Node Management
- **Show all nodes:**
  ```bash
  kubectl get node
  ```

### Namespace Management
- **List all namespaces:**
  ```bash
  kubectl get namespaces
  ```
  ```bash
  kubectl get ns
  ```
- **Create a custom namespace:**
  ```bash
  kubectl create ns <namespace-name>
  ```

### Pod Management
- **Get the list of pods in the default namespace:**
  ```bash
  kubectl get pod
  ```
- **Get the list of pods in the default namespace with full information:**
  ```bash
  kubectl get pod -o wide
  ```
- **Get the list of pods in a custom namespace with full information:**
  ```bash
  kubectl get pod -o wide -n <name-space>
  ```

### Running a Pod
- **Run a new pod:**
  ```bash
    kubectl run <pod-name> <switch> {
    --image=<image-name>,                # Specifies the container image to use
    --port=<portnumber>,                 # Specifies the port that the container exposes
    -n <namespace-name>,                 # Specifies the namespace
    --env="KEY=VALUE",                   # Sets environment variables in the container
    --command,                           # Treats the rest of the arguments as the command to run in the container
    --replicas=<number>,                 # Specifies the number of replicas for the deployment
    --labels="key=value,key2=value2",    # Adds labels to the pod(s)
    --dry-run=client,                    # Prints the object that would be sent, without creating it
    --restart=<Always|OnFailure|Never>,  # Determines the restart policy for the pod
    --overrides='<json>',                # Provides a JSON override for the generated object
    --image-pull-policy=<policy>,        # Specifies the image pull policy (Always, IfNotPresent, Never)
    --limits=cpu=<cpu>,memory=<memory>,  # Specifies resource limits for the container
    --requests=cpu=<cpu>,memory=<memory> # Specifies resource requests for the container
    }
  ```
  - *Example:*
    ```bash
      kubectl run mypod --image=nginx --port=80 -n mynamespace \
      --env="ENV_VAR_NAME=VALUE" --command -- nginx -g "daemon off;" \
      --replicas=3 --labels="app=myapp,env=prod" --dry-run=client \
      --restart=Always --overrides='{"spec": {"containers": [{"name": "nginx", "image": "nginx"}]}}' \
      --image-pull-policy=IfNotPresent --limits=cpu=100m,memory=256Mi \
      --requests=cpu=50m,memory=128Mi
    ```


### Deleting a Pod
- **Delete a pod in a custom namespace:**
  ```bash
  kubectl delete pod -n <namespace-name> <pod-name>
  ```

### API Resource Documentation
- **Get documentation of an API resource:**
  ```bash
  kubectl explain <api-resource-name>
  ```
  - *Example:*
    ```bash
    kubectl explain pod
    ```

### Logging and Pod Information
- **Get and follow logs of a pod (pod must be created and running):**
  ```bash
  kubectl logs -f -n <namespace-name> <podname>
  ```
- **Get logs and state information of a pod (works at any time):**
  ```bash
  kubectl describe pod -n <namespace-name> <podname>
  ```

### Apply Yaml File
```bash
kubectl apply -f <yaml-file> -n <namespace-name>
```