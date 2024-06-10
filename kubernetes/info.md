# Kubernetes (Kuber) Documentation

## Control Plane (CP)
- **CP (Control Plane)**: The central management entity of the Kubernetes cluster.
- By default, the manager in Kubernetes does not directly handle any containers.

## Kubernetes Manager Components
- **Control Manager**
- **Scheduler**
- **API Server**
- **etcd (Database)**
- **Kubelet**

## Kubernetes Worker Components
- **Kube Proxy**
- **Kubelet**

## Data Flow
- **Kube Proxy** and **Kubelet** communicate with the Kubernetes Manager for data handling.

## Administration Tools
- **kubeadm**: Used for administration commands.
- **kubectl**: Used to manage nodes and services.

---

## Kubernetes Setup

### Step 1: Write Default Config
1. Generate the default containerd configuration.
   ```bash
   containerd config default > /etc/containerd/config.toml
   ```

### Step 2: Modify Config
1. Change `systemd_cgroup` to `true`.
   ```bash
   vim /etc/containerd/config.toml
   ```
2. Restart the containerd service.
   ```bash
   systemctl restart containerd
   ```

### Step 3: Load Required Modules
1. Load necessary kernel modules.
   ```bash
   modprobe br_netfilter overlay
   lsmod | grep overlay  # To verify the overlay module is loaded
   ```
2. Add the modules to load at boot.
   ```bash
   vim /etc/modules-load.d/modules.conf
   ```
   Add the following lines:
   ```
   br_netfilter
   overlay
   ```

### Step 4: Enable IPv4 Forwarding
1. Update Config File
   ```bash
    sed -i 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/' /etc/sysctl.conf && sysctl -p
   ```


### Step 5: Install Required Packages
1. Install necessary packages.
   ```bash
   sudo apt install ca-certificates curl apt-transport-https conntrack -y
   ```

### Step 6: Install Kubernetes Components
1. Add Kubernetes keyring.
   ```bash
   curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
   ```
2. Add Kubernetes to the sources list.
   ```bash
   echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
   ```
3. Update package list and install Kubernetes components.
   ```bash
   sudo apt-get update
   sudo apt-get install -y kubelet kubeadm kubectl
   ```
4. Hold the package versions.
   ```bash
   sudo apt-mark hold kubelet kubeadm kubectl
   ```
5. Enable and start kubelet.
   ```bash
   sudo systemctl enable --now kubelet
   ```

### Step 7: Setup Network Protocol
1. Initialize the Kubernetes cluster.
   ```bash
   kubeadm init --apiserver-advertise-address <ip-interface> --pod-network-cidr 10.244.0.0/16
   ```
2. Apply the Flannel CNI plugin for network management.
   ```bash
   kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
   ```
3. Configure kubectl for the current user.
   ```bash
   mkdir -p $HOME/.kube
   sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
   sudo chown $(id -u):$(id -g) $HOME/.kube/config
   ```

### Step 8: Generate Join Command
1. Generate the command to join worker nodes to the cluster.
   ```bash
   kubeadm token create --print-join-command
   ```

This command will print out a token and the complete command to be used on worker nodes to join them to the cluster.
