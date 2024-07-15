## Document: Kubernetes ReplicaSet YAML Explanation

### Overview
This document provides an explanation of a Kubernetes ReplicaSet YAML file and commands to manage the ReplicaSet. The YAML file defines the desired state for a ReplicaSet, which ensures a specified number of pod replicas are running at any given time.

### YAML File Breakdown

#### 1. Define the ReplicaSet
The YAML file begins with the `apiVersion`, `kind`, and `metadata` fields, which specify the API version, the type of Kubernetes object, and metadata about the object, respectively.

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: my-app
  namespace: my-ns
  labels:
    app.kubernetes.io/name: my-app
    app.kubernetes.io/env: development
```
- `apiVersion: apps/v1`: Specifies that this configuration uses the `apps/v1` API version.
- `kind: ReplicaSet`: Defines the object as a ReplicaSet.
- `metadata`: Provides metadata for the ReplicaSet, including:
  - `name`: The name of the ReplicaSet (`my-app`).
  - `namespace`: The namespace where the ReplicaSet will be created (`my-ns`).
  - `labels`: Key-value pairs to categorize the ReplicaSet (`app.kubernetes.io/name: my-app` and `app.kubernetes.io/env: development`).

#### 2. Define the Specification
The `spec` section describes the desired state of the ReplicaSet.

```yaml
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: my-app
  template:
    metadata:
      labels:
        app.kubernetes.io/name: my-app
    spec:
      containers:
      - name: nginx
        image: nginx
```
- `replicas: 3`: Specifies that three replicas of the pod should be running.
- `selector`: Defines how to identify the pods managed by this ReplicaSet.
  - `matchLabels`: Matches pods with the label `app.kubernetes.io/name: my-app`.
- `template`: Provides the pod template used by the ReplicaSet to create new pods.
  - `metadata`: Metadata for the pod template.
    - `labels`: Labels applied to the pods (`app.kubernetes.io/name: my-app`).
  - `spec`: Describes the pod specification.
    - `containers`: Defines the containers within the pod.
      - `name`: The name of the container (`nginx`).
      - `image`: The container image to use (`nginx`).


### Update the Container Image Version

To update the container image version, edit the YAML manifest and change the `image` field:
```yaml
containers:
- name: nginx
  image: nginx:1.25
```
Apply the updated manifest to update the pods with the new image version.

### Complete YAML File with Image Version Update

Here is the complete YAML file with the container image version updated to `nginx:1.25`:

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: my-app
  namespace: my-ns
  labels:
    app.kubernetes.io/name: my-app
    app.kubernetes.io/env: development
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: my-app
  template:
    metadata:
      labels:
        app.kubernetes.io/name: my-app
    spec:
      containers:
      - name: nginx
        image: nginx:1.25
```
