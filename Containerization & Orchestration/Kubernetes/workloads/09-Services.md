# 🔗 Services in Kubernetes (SVC)

A **Service** in Kubernetes provides a stable networking interface to access a set of pods. It allows for decoupling between client applications and the underlying pods by using DNS names and selectors.

---

## 🌐 Service Basics

### 📌 Service Flow
```

Service ➡️ Endpoint ➡️ Pods

````

- Services abstract access to a group of pods.
- Services automatically get a DNS name in the cluster.
- They use selectors to route traffic to matching pods.

---

## 🧭 Service Types

1. **ClusterIP** (default)  
   - Accessible only within the cluster.

2. **NodePort**  
   - Exposes the service on a static port on each node.

3. **LoadBalancer**  
   - Provisions an external IP via a cloud provider to expose the service.

---

## 🧪 Useful Commands

### 🔍 Get Endpoints
```bash
kubectl get ep -n <namespace>
````

### 📄 Get Services

```bash
kubectl get svc -n <namespace>
```

---

## 🧾 Example Service Manifest

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
  namespace: ns
  labels:
    app: web-server
spec:
  type: ClusterIP  # Options: ClusterIP, NodePort, LoadBalancer
  selector:
    app: nginx
  ports:
    - name: http  # Port name is optional but useful
      port: 80  # Service port
      targetPort: 8080  # Container port
```

> 🔍 **Note:** The `selector` must match pod labels for the service to route traffic correctly.
> 🧠 **Tip:** Use `kubectl describe svc <svc-name>` to troubleshoot or verify service-to-pod connectivity.
> 🌐 Services are resolved by DNS using the format: `<service-name>.<namespace>.svc.cluster.local`.

