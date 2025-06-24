
## Node Management

### Listing Nodes

- **Show All Nodes**

  ```bash
  kubectl get nodes
  ```


  ```bash
    kubectl get nodes --show-lables
  ```

### Node Maintenance (Cordon/Drain)

- **Cordon a Node**  
  Prevent new pods from being scheduled on the node.

  ```bash
  kubectl cordon <node-name>
  ```

- **Uncordon a Node**  
  Mark the node as schedulable again.

  ```bash
  kubectl uncordon <node-name>
  ```

- **Drain a Node**  
  Evict all pods from the node (excluding those managed by DaemonSets).

  ```bash
  kubectl drain <node-name> --ignore-daemonsets --delete-local-data
  ```

  > **Warning:** Draining a node will evict running pods. Ensure that you plan this action to avoid service disruption.


---

