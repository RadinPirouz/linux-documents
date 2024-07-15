#### 1. Deployment with Resource Limits and Horizontal Pod Autoscaler

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  namespace: my-ns
  labels:
    app.kubernetes.io/name: myapp
    app.kubernetes.io/env: development
spec:
  replicas: 5
  selector:
    matchLabels:
      app.kubernetes.io/name: myapp
      app.kubernetes.io/env: development
  template:
    metadata:
      labels:
        app.kubernetes.io/name: myapp
        app.kubernetes.io/env: development
    spec:
      containers:
      - name: nginx
        image: nginx # change image and apply again
        resources:
          limits:
            memory: "128Mi"
            cpu: "500m"
          requests:
            memory: "64Mi"
            cpu: "250m"
        ports:
        - containerPort: 80
```
- `apiVersion: apps/v1`: Specifies the API version.
- `kind: Deployment`: Defines the object as a Deployment.
- `metadata`: Provides metadata for the Deployment.
  - `name`: The name of the Deployment (`myapp`).
  - `namespace`: The namespace where the Deployment will be created (`my-ns`).
  - `labels`: Key-value pairs to categorize the Deployment.
- `spec`: Describes the desired state.
  - `replicas`: Number of pod replicas (5).
  - `selector`: Identifies the pods managed by this Deployment.
  - `template`: The pod template used by the Deployment.
    - `metadata`: Metadata for the pod template.
    - `spec`: Describes the pod specification.
      - `containers`: Defines the containers within the pod.
        - `name`: The name of the container (`nginx`).
        - `image`: The container image (`nginx`).
        - `resources`: Resource limits and requests.
          - `limits`: Maximum resources (`128Mi` memory, `500m` CPU).
          - `requests`: Minimum resources (`64Mi` memory, `250m` CPU).
        - `ports`: Container ports (80).


### 2. Deployment with Rolling Update Strategy

```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: my-name
  labels:
    name: my-name
spec:
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  template:
    metadata:
      labels:
        name: my-name
    spec:
      containers:
      - image: ipedrazas/docmock
        name: my-name
        resources:
          requests:
            cpu: "20m"
            memory: "55M"
        livenessProbe:
          httpGet:
            path: /_status/healthz
            port: 5000
          initialDelaySeconds: 90
          timeoutSeconds: 10
        readinessProbe:
          httpGet:
            path: /_status/healthz
            port: 5000
          initialDelaySeconds: 30
          timeoutSeconds: 10
        env:
        - name: ENVVARNAME
          value: ENVVARVALUE       
        ports:
        - containerPort: 5000
          name: my-name
        volumeMounts:
        - mountPath: /data
          name: data
      volumes:
        - name: data
          emptyDir: {}
      restartPolicy: Always
      imagePullPolicy: Always
```
- `apiVersion: extensions/v1beta1`: Specifies the API version.
- `kind: Deployment`: Defines the object as a Deployment.
- `metadata`: Provides metadata for the Deployment.
  - `name`: The name of the Deployment (`my-name`).
  - `labels`: Key-value pairs to categorize the Deployment.
- `spec`: Describes the desired state.
  - `strategy`: Rolling update strategy.
    - `rollingUpdate`: Defines the update strategy.
      - `maxSurge`: Maximum number of additional pods (1).
      - `maxUnavailable`: Maximum number of unavailable pods (1).
    - `type`: The type of update strategy (`RollingUpdate`).
  - `template`: The pod template used by the Deployment.
    - `metadata`: Metadata for the pod template.
    - `spec`: Describes the pod specification.
      - `containers`: Defines the containers within the pod.
        - `name`: The name of the container (`my-name`).
        - `image`: The container image (`ipedrazas/docmock`).
        - `resources`: Resource requests.
          - `requests`: Minimum resources (`20m` CPU, `55M` memory).
        - `livenessProbe`: Health check for the container.
          - `httpGet`: HTTP GET request for the probe.
            - `path`: The path to check (`/_status/healthz`).
            - `port`: The port to check (5000).
          - `initialDelaySeconds`: Initial delay before the probe starts (90 seconds).
          - `timeoutSeconds`: Timeout for the probe (10 seconds).
        - `readinessProbe`: Readiness check for the container.
          - `httpGet`: HTTP GET request for the probe.
            - `path`: The path to check (`/_status/healthz`).
            - `port`: The port to check (5000).
          - `initialDelaySeconds`: Initial delay before the probe starts (30 seconds).
          - `timeoutSeconds`: Timeout for the probe (10 seconds).
        - `env`: Environment variables for the container.
          - `name`: The name of the environment variable (`ENVVARNAME`).
          - `value`: The value of the environment variable (`ENVVARVALUE`).
        - `ports`: Container ports.
          - `containerPort`: The container port (5000).
          - `name`: The name of the port (`my-name`).
        - `volumeMounts`: Mounting volumes to the container.
          - `mountPath`: The path to mount the volume (`/data`).
          - `name`: The name of the volume (`data`).
      - `volumes`: Defines the volumes.
        - `name`: The name of the volume (`data`).
        - `emptyDir`: An empty directory volume.
      - `restartPolicy`: Restart policy for the container (`Always`).
      - `imagePullPolicy`: Image pull policy (`Always`).

