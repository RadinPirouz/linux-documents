### YAML File Breakdown

#### 1. Node Exporter DaemonSet

This DaemonSet is configured to run a Node Exporter container on each node in the `my-ns` namespace.

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-exporter
  namespace: my-ns
  labels:
    app: example
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: node-exporter
      app.kubernetes.io/env: development
      app.kubernetes.io/part-of: monitoring
  template:
    metadata:
      labels:
        app.kubernetes.io/name: node-exporter
        app.kubernetes.io/env: development
        app.kubernetes.io/part-of: monitoring
    spec:
      containers:
      - name: node-exporter
        image: prom/node-exporter
```
- `apiVersion: apps/v1`: Specifies the API version.
- `kind: DaemonSet`: Defines the object as a DaemonSet.
- `metadata`: Provides metadata for the DaemonSet.
  - `name`: The name of the DaemonSet (`node-exporter`).
  - `namespace`: The namespace where the DaemonSet will be created (`my-ns`).
  - `labels`: Key-value pairs to categorize the DaemonSet (`app: example`).
- `spec`: Describes the desired state.
  - `selector`: Identifies the pods managed by this DaemonSet.
    - `matchLabels`: Matches pods with specified labels.
      - `app.kubernetes.io/name`: `node-exporter`
      - `app.kubernetes.io/env`: `development`
      - `app.kubernetes.io/part-of`: `monitoring`
  - `template`: The pod template used by the DaemonSet.
    - `metadata`: Metadata for the pod template.
      - `labels`: Labels applied to the pods.
        - `app.kubernetes.io/name`: `node-exporter`
        - `app.kubernetes.io/env`: `development`
        - `app.kubernetes.io/part-of`: `monitoring`
    - `spec`: Describes the pod specification.
      - `containers`: Defines the containers within the pod.
        - `name`: The name of the container (`node-exporter`).
        - `image`: The container image (`prom/node-exporter`).

#### 2. Example DaemonSet

This DaemonSet is configured to run an example container on each node.

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: example-daemonset
  labels:
    app: example
spec:
  selector:
    matchLabels:
      app: example
  template:
    metadata:
      labels:
        app: example
    spec:
      containers:
      - name: example-container
        image: nginx
```
- `apiVersion: apps/v1`: Specifies the API version.
- `kind: DaemonSet`: Defines the object as a DaemonSet.
- `metadata`: Provides metadata for the DaemonSet.
  - `name`: The name of the DaemonSet (`example-daemonset`).
  - `labels`: Key-value pairs to categorize the DaemonSet (`app: example`).
- `spec`: Describes the desired state.
  - `selector`: Identifies the pods managed by this DaemonSet.
    - `matchLabels`: Matches pods with the label `app: example`.
  - `template`: The pod template used by the DaemonSet.
    - `metadata`: Metadata for the pod template.
      - `labels`: Labels applied to the pods (`app: example`).
    - `spec`: Describes the pod specification.
      - `containers`: Defines the containers within the pod.
        - `name`: The name of the container (`example-container`).
        - `image`: The container image (`nginx`).
