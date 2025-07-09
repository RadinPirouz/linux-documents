# 🧾 Kubernetes ConfigMap

## 📘 What is a ConfigMap?

A **ConfigMap** allows you to **store configuration data** in key-value pairs that can be:

* Mounted as files in a Pod
* Exposed as environment variables
* Consumed by Kubernetes workloads without hardcoding settings in container images

---

## ⚙️ Creating a ConfigMap from Files

Create a ConfigMap from one or more files:

```bash
kubectl -n <namespace> create configmap <configmap-name> --from-file=<file-or-directory>
```

### ✅ Examples

```bash
# Create from a single file
kubectl -n <ns> create configmap nginx-conf --from-file=./nginx.conf

# Create from multiple files
kubectl -n <ns> create configmap nginx-conf --from-file=./nginx.conf --from-file=./site.conf
```

---

## 📂 Viewing and Editing ConfigMaps

```bash
# List ConfigMaps in a namespace
kubectl get cm -n <namespace>

# Edit a ConfigMap
kubectl -n <namespace> edit configmap <configmap-name>
```

---

## 📄 ConfigMap YAML Example

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: game-demo
data:
  # Key-value style
  player_initial_lives: "3"
  ui_properties_file_name: "user-interface.properties"

  # Multi-line file-style entries
  game.properties: |
    enemy.types=aliens,monsters
    player.maximum-lives=5    
  user-interface.properties: |
    color.good=purple
    color.bad=yellow
    allow.textmode=true    
```

---

## 🚀 Deployment Example: Using ConfigMap as Volume

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-1
  namespace: dev
  labels:
    app.kubernetes.io/name: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: nginx
  template:
    metadata:
      labels:
        app.kubernetes.io/name: nginx
        os: linux
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
          volumeMounts:
            - name: configfile
              mountPath: /etc/nginx/nginx.conf
              subPath: nginx.conf  # Mount specific file from ConfigMap
      volumes:
        - name: configfile
          configMap:
            name: nginx-conf
```

