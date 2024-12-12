
---

# Containerd and Kubernetes Installation Guide

## 1. Disable Swap
Turn off swap and disable it permanently.

```bash
swapoff -a
sed -i '/swap/d' /etc/fstab
```
## 2. Enable Required Kernel Modules
Create a configuration file to load necessary kernel modules and load them temporarily.
```bash
echo -e "overlay\nbr_netfilter" | sudo tee /etc/modules-load.d/containerd.conf
sudo modprobe overlay
sudo modprobe br_netfilter
```
## 3. Enable IPv4 Forwarding
Enable IPv4 forwarding in the sysctl configuration and apply the changes.
```bash
sed -i 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/' /etc/sysctl.conf
sysctl -p
```
## 4. Configure Containerd
Generate the default configuration for Containerd and modify it to use systemd as the cgroup driver.
```bash
containerd config default | sudo tee /etc/containerd/config.toml
sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml
```

## 5. Install Kubernetes
Add the Kubernetes package repository and install the required packages.
```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```
## 6. Enable kubelet
Enable and start the kubelet service.
```bash
sudo systemctl enable --now kubelet
```
## 7. Initialize the Kubernetes Cluster
Initialize the Kubernetes control plane with the specified parameters.
```bash
sudo kubeadm init --control-plane-endpoint 192.168.2.100 --apiserver-advertise-address 192.168.2.100 --pod-network-cidr 10.244.0.0/16 | tee kuber-install.log
```
## 8. Create Control Plane Join Command
Create the control plane join command and save it for later use.
```bash
sudo kubeadm init phase upload-certs --upload-certs

Copy the output certificate key and run the following command, replacing <CERTIFICATE_KEY> with the copied key.

sudo kubeadm token create --certificate-key <CERTIFICATE_KEY> --print-join-command | tee cp-command.txt
```
## 9. Join Control Plane and Worker Nodes
Use the command from cp-command.txt on your control plane nodes to join them. Additionally, get the join command for worker nodes from kuber-install.log and run it on each worker node.

---

This revised guide provides clear, step-by-step instructions, making it easier to follow and ensuring all necessary actions are covered.