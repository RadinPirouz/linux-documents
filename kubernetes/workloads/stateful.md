
#### 1. Basic Redis StatefulSet

This StatefulSet is configured to run Redis instances in the `my-ns` namespace with 3 replicas.

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: redis
  namespace: my-ns
  labels:
    app.kubernetes.io/name: redis
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: redis
  template:
    metadata:
      labels:
        app.kubernetes.io/name: redis
    spec:
      containers:
      - name: redis
        image: redis
```
- `apiVersion: apps/v1`: Specifies the API version.
- `kind: StatefulSet`: Defines the object as a StatefulSet.
- `metadata`: Provides metadata for the StatefulSet.
  - `name`: The name of the StatefulSet (`redis`).
  - `namespace`: The namespace where the StatefulSet will be created (`my-ns`).
  - `labels`: Key-value pairs to categorize the StatefulSet.
- `spec`: Describes the desired state.
  - `replicas`: Number of pod replicas (3).
  - `selector`: Identifies the pods managed by this StatefulSet.
    - `matchLabels`: Matches pods with the label `app.kubernetes.io/name: redis`.
  - `template`: The pod template used by the StatefulSet.
    - `metadata`: Metadata for the pod template.
      - `labels`: Labels applied to the pods (`app.kubernetes.io/name: redis`).
    - `spec`: Describes the pod specification.
      - `containers`: Defines the containers within the pod.
        - `name`: The name of the container (`redis`).
        - `image`: The container image (`redis`).

#### 2. Redis StatefulSet with Volume

This StatefulSet is similar to the first one but includes persistent volume claims (PVCs) to ensure data persistence.

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: redis
  namespace: my-ns
  labels:
    app.kubernetes.io/name: redis
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: redis
  template:
    metadata:
      labels:
        app.kubernetes.io/name: redis
    spec:
      containers:
      - name: redis
        image: redis
        volumeMounts:
          - name: redis-data
            mountPath: /var/lib/redis
  volumeClaimTemplates:
    - metadata:
        name: redis-data
      spec:
        accessModes:
          - "ReadWriteOnce"
        resources:
          requests:
            storage: 1Gi
```
- `apiVersion: apps/v1`: Specifies the API version.
- `kind: StatefulSet`: Defines the object as a StatefulSet.
- `metadata`: Provides metadata for the StatefulSet.
  - `name`: The name of the StatefulSet (`redis`).
  - `namespace`: The namespace where the StatefulSet will be created (`my-ns`).
  - `labels`: Key-value pairs to categorize the StatefulSet.
- `spec`: Describes the desired state.
  - `replicas`: Number of pod replicas (3).
  - `selector`: Identifies the pods managed by this StatefulSet.
    - `matchLabels`: Matches pods with the label `app.kubernetes.io/name: redis`.
  - `template`: The pod template used by the StatefulSet.
    - `metadata`: Metadata for the pod template.
      - `labels`: Labels applied to the pods (`app.kubernetes.io/name: redis`).
    - `spec`: Describes the pod specification.
      - `containers`: Defines the containers within the pod.
        - `name`: The name of the container (`redis`).
        - `image`: The container image (`redis`).
        - `volumeMounts`: Mounts the specified volume to `/var/lib/redis`.
          - `name`: The name of the volume (`redis-data`).
          - `mountPath`: The path to mount the volume (`/var/lib/redis`).
  - `volumeClaimTemplates`: Defines the PVCs for the StatefulSet.
    - `metadata`: Metadata for the PVC.
      - `name`: The name of the PVC (`redis-data`).
    - `spec`: Describes the PVC specification.
      - `accessModes`: Access mode for the PVC (`ReadWriteOnce`).
      - `resources`: Resource requests for the PVC.
        - `requests`: Storage request (1Gi).

#### 3. Web StatefulSet with Volume

This StatefulSet runs NGINX instances with persistent storage.

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  selector:
    matchLabels:
      app: nginx # has to match .spec.template.metadata.labels
  serviceName: "nginx"
  replicas: 3 # by default is 1
  minReadySeconds: 10 # by default is 0
  template:
    metadata:
      labels:
        app: nginx # has to match .spec.selector.matchLabels
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: nginx
        image: registry.k8s.io/nginx-slim:0.8
        ports:
        - containerPort: 80
          name: web
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:
  - metadata:
      name: www
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: "my-storage-class"
      resources:
        requests:
          storage: 1Gi
```
- `apiVersion: apps/v1`: Specifies the API version.
- `kind: StatefulSet`: Defines the object as a StatefulSet.
- `metadata`: Provides metadata for the StatefulSet.
  - `name`: The name of the StatefulSet (`web`).
- `spec`: Describes the desired state.
  - `selector`: Identifies the pods managed by this StatefulSet.
    - `matchLabels`: Matches pods with the label `app: nginx`.
  - `serviceName`: The name of the service that governs this StatefulSet (`nginx`).
  - `replicas`: Number of pod replicas (3).
  - `minReadySeconds`: Minimum time for pods to be ready (10 seconds).
  - `template`: The pod template used by the StatefulSet.
    - `metadata`: Metadata for the pod template.
      - `labels`: Labels applied to the pods (`app: nginx`).
    - `spec`: Describes the pod specification.
      - `terminationGracePeriodSeconds`: Time for the pod to terminate gracefully (10 seconds).
      - `containers`: Defines the containers within the pod.
        - `name`: The name of the container (`nginx`).
        - `image`: The container image (`registry.k8s.io/nginx-slim:0.8`).
        - `ports`: Container ports.
          - `containerPort`: The container port (80).
          - `name`: The name of the port (`web`).
        - `volumeMounts`: Mounts the specified volume to `/usr/share/nginx/html`.
          - `name`: The name of the volume (`www`).
          - `mountPath`: The path to mount the volume (`/usr/share/nginx/html`).
  - `volumeClaimTemplates`: Defines the PVCs for the StatefulSet.
    - `metadata`: Metadata for the PVC.
      - `name`: The name of the PVC (`www`).
    - `spec`: Describes the PVC specification.
      - `accessModes`: Access mode for the PVC (`ReadWriteOnce`).
      - `storageClassName`: The storage class name (`my-storage-class`).
      - `resources`: Resource requests for the PVC.
        - `requests`: Storage request (1Gi).

