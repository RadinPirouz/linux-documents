
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

> **Note:** The `kubectl run` command is best suited for running single pods. For more complex deployments, consider using YAML manifests.


```bash
kubectl run <pod-name> --image=<image-name>
```

```bash
kubectl run <pod-name> --image=<image-name> -n <namespace>
```


```bash
kubectl delete pod <pod-name> -n <namespace-name>
```


```bash
kubectl delete pod <pod-name> -n <namespace-name> --force
```


```bash
kubectl delete pod <pod-name> -n <namespace-name> --force --grace-period 0
```

```bash
kubectl edit pod -n <namepsace> <podname>
```
Pod Can not been edit (not editable)


```bash
kubectl exec -it -n <namespace> <podname> -- <command or shell>
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  namespace: dev
  name: pod-1
  labels:
    label1: test
    label2: test2
    app.kubernetes.io/label3: test3
    app.kubernetes.io/label4: test4
spec:
  containers:
    - name: nginx-server
      image: nginx
    
    - name: nginx-exporter
      image: nginx-exporter

    - name: ubuntu-c0
      image: ubuntu
      command: ["/bin/bash","-c","while true; do echo hello-world; sleep 5; done"]
      resources:
        limits:
          memory: "256Mi"
          cpu: "250m"
        requests:
          memory: "128Mi"
          cpu: "125m"
  nodeSelector:
    hostname: k3s
    app.kubernetes.io/disk: ssd
```

