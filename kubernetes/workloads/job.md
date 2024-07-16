
#### 1. Simple Job

This Job is configured to run a single container that prints "hello world" to the console.

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: myjob
  namespace: my-ns
spec:
  template:
    spec:
      containers:
      - name: myjob
        image: alpine
        command:
        - echo
        - "hello world"
      restartPolicy: Never
```
- `apiVersion: batch/v1`: Specifies the API version.
- `kind: Job`: Defines the object as a Job.
- `metadata`: Provides metadata for the Job.
  - `name`: The name of the Job (`myjob`).
  - `namespace`: The namespace where the Job will be created (`my-ns`).
- `spec`: Describes the desired state.
  - `template`: The pod template used by the Job.
    - `spec`: Describes the pod specification.
      - `containers`: Defines the containers within the pod.
        - `name`: The name of the container (`myjob`).
        - `image`: The container image (`alpine`).
        - `command`: The command to run in the container (`echo "hello world"`).
      - `restartPolicy`: Specifies the restart policy for the pod (`Never`).

#### 2. Job with Error and Retries

This Job attempts to list a non-existent directory (`/chert`) and will try to complete the task up to 6 times due to the error.

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: myjob
  namespace: my-ns
spec:
  backoffLimit: 6
  template:
    spec:
      containers:
      - name: myjob
        image: alpine
        command:
        - ls
        - "/chert"
      restartPolicy: Never
```
- `apiVersion: batch/v1`: Specifies the API version.
- `kind: Job`: Defines the object as a Job.
- `metadata`: Provides metadata for the Job.
  - `name`: The name of the Job (`myjob`).
  - `namespace`: The namespace where the Job will be created (`my-ns`).
- `spec`: Describes the desired state.
  - `backoffLimit`: The number of retries before the Job is considered failed (6).
  - `template`: The pod template used by the Job.
    - `spec`: Describes the pod specification.
      - `containers`: Defines the containers within the pod.
        - `name`: The name of the container (`myjob`).
        - `image`: The container image (`alpine`).
        - `command`: The command to run in the container (`ls /chert`).
      - `restartPolicy`: Specifies the restart policy for the pod (`Never`).

This guide provides a detailed explanation of Kubernetes Job YAML files. Jobs are designed to run a task to completion, and they can retry in case of failures. Each Job configuration includes specifications for containers, commands, and restart policies, with the option to set a retry limit for handling errors.