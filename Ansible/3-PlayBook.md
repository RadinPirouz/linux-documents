

# Ansible Playbook Guide

Ansible Playbooks are YAML files that define a series of tasks to automate server configuration, deployment, and management. This guide provides instructions on how to run a playbook and includes several examples to help you get started.

## Running an Ansible Playbook

To execute an Ansible Playbook, use the following command:

```bash
ansible-playbook <playbook.yaml> -i <inventory-file.ini>
```

- **`<playbook.yaml>`**: The path to your playbook file.
- **`<inventory-file.ini>`**: The path to your inventory file (can be in INI or YAML format).

## Example Playbooks

### 1. Simple APT Cache Update

This example demonstrates a basic playbook that updates the APT package cache on all specified hosts.

```yaml
- name: Update APT Cache Playbook
  hosts: all           # Specifies that the playbook runs on all hosts defined in the inventory
  become: yes          # Use sudo to execute tasks with elevated privileges
  tasks:
    - name: Update apt-cache
      ansible.builtin.apt:
        update_cache: yes
```

### 2. Update APT Cache and Install Nginx

This playbook not only updates the APT cache but also installs the Nginx web server on all specified hosts.

```yaml
- name: Install Nginx and Update APT Cache
  hosts: all           # Run on all hosts defined in the inventory
  become: yes          # Use sudo for elevated privileges
  tasks:
    - name: Update apt-cache and install Nginx
      ansible.builtin.apt:
        name: nginx
        state: present
        update_cache: yes
```

### 3. Install Nginx and Copy Configuration File

In addition to installing Nginx, this playbook copies a custom Nginx configuration file from the Ansible server to the target hosts.

```yaml
- name: Install Nginx and Copy Configuration
  hosts: all           # Run on all hosts defined in the inventory
  become: yes          # Use sudo for elevated privileges
  tasks:
    - name: Update apt-cache and install Nginx
      ansible.builtin.apt:
        name: nginx
        state: present
        update_cache: yes
        
    - name: Copy Nginx configuration file
      ansible.builtin.copy:
        src: /root/ansible/nginx.conf
        dest: /etc/nginx/nginx.conf
```

### 4. Full Nginx Deployment: Install, Configure, and Restart

This playbook provides a complete example of deploying Nginx: updating the APT cache, installing Nginx, copying the configuration file, and restarting the Nginx service to apply the changes.

```yaml
- name: Full Nginx Deployment
  hosts: all           # Run on all hosts defined in the inventory
  become: yes          # Use sudo for elevated privileges
  tasks:
    - name: Update apt-cache and install Nginx
      ansible.builtin.apt:
        name: nginx
        state: present
        update_cache: yes
        
    - name: Copy Nginx configuration file
      ansible.builtin.copy:
        src: /root/ansible/nginx.conf
        dest: /etc/nginx/nginx.conf
        
    - name: Restart Nginx service
      ansible.builtin.service:
        name: nginx
        state: restarted
```

### Explanation of Key Components

- **`hosts: all`**: This indicates that the playbook should be executed on all hosts listed in the inventory file.
- **`become: yes`**: Ensures that tasks requiring elevated privileges (sudo) are executed as the root user.
- **Tasks**:
  - **`Update apt-cache`**: Uses the APT module to update the package cache.
  - **`Install Nginx`**: Installs the Nginx web server.
  - **`Copy Configuration File`**: Copies a custom configuration file to the appropriate directory on the target hosts.
  - **`Restart Nginx`**: Restarts the Nginx service to apply the new configuration.

### Running the Playbooks

Save the desired playbook as a YAML file (e.g., `deploy_nginx.yaml`), and then run it using:

```bash
ansible-playbook deploy_nginx.yaml -i inventory.ini
```

Make sure your inventory file (`inventory.ini`) includes all necessary hosts and connection details.
