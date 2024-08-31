# Ansible Playbook Guide

Ansible Playbooks are YAML files that define a series of tasks to automate server configuration, deployment, and management. This guide provides instructions on how to run a playbook and includes examples to help you get started.

## Running an Ansible Playbook

To execute an Ansible Playbook, use the following command:

```bash
ansible-playbook <playbook.yaml> -i <inventory-file.ini>
```

- **`<playbook.yaml>`**: Path to your playbook file.
- **`<inventory-file.ini>`**: Path to your inventory file (can be in INI or YAML format).

## Example Playbooks

### 1. Simple APT Cache Update

This playbook updates the APT package cache on all specified hosts.

```yaml
- name: Update APT Cache Playbook
  hosts: all           # Run on all hosts defined in the inventory
  become: yes          # Use sudo for elevated privileges
  tasks:
    - name: Update apt-cache
      ansible.builtin.apt:
        update_cache: yes
```

### 2. Update APT Cache and Install Nginx

This playbook updates the APT cache and installs the Nginx web server on all specified hosts.

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

This playbook installs Nginx and copies a custom configuration file from the Ansible server to the target hosts.

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

This playbook demonstrates a full Nginx deployment: updating the APT cache, installing Nginx, copying a configuration file, and restarting the Nginx service to apply the changes.

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

## Key Components Explained

- **`hosts: all`**: Specifies that the playbook should run on all hosts listed in the inventory file.
- **`become: yes`**: Ensures tasks requiring elevated privileges (sudo) are executed as the root user.
- **Tasks**:
  - **`Update apt-cache`**: Uses the APT module to update the package cache.
  - **`Install Nginx`**: Installs the Nginx web server.
  - **`Copy Configuration File`**: Copies a custom configuration file to the appropriate directory on the target hosts.
  - **`Restart Nginx`**: Restarts the Nginx service to apply the new configuration.

## Running the Playbooks

Save the desired playbook as a YAML file (e.g., `deploy_nginx.yaml`), and run it using:

```bash
ansible-playbook deploy_nginx.yaml -i inventory.ini
```

Ensure that your inventory file (`inventory.ini`) includes all necessary hosts and connection details.

## Additional Examples

### Show Debug Message

Use the `debug` module to display a message during playbook execution:

```yaml
- name: Show Debug Message
  ansible.builtin.debug:
    msg: "Test Message"
```

### Use a Shell Command

Run a shell command and capture the output:

```yaml
- name: Execute Shell Command
  ansible.builtin.shell:
    cmd: echo "Hello, Ansible!"
  register: shell_output # Register the command output as a variable

- name: Display Shell Output
  ansible.builtin.debug:
    msg: "Output is: {{ shell_output.stdout }}" # Display the command output
```

### Playbook with Conditional Statements

This playbook demonstrates the use of conditional statements to check if a file exists and take action based on the result:

```yaml
- name: Check if File Exists
  ansible.builtin.shell:
    cmd: ls /path/to/file
  register: file_output
  ignore_errors: yes

- name: File Exists
  ansible.builtin.debug:
    msg: "File exists"
  when: file_output.rc == 0

- name: File Does Not Exist
  ansible.builtin.debug:
    msg: "File does not exist"
  when: file_output.rc != 0
```

### Check File Existence Using the `stat` Module

You can also check if a file exists using the `stat` module, which is more reliable and provides more information:

```yaml
- name: Check if File Exists
  ansible.builtin.stat:
    path: /path/to/file
  register: file_stat

- name: File Exists
  ansible.builtin.debug:
    msg: "File exists"
  when: file_stat.stat.exists

- name: File Does Not Exist
  ansible.builtin.debug:
    msg: "File does not exist"
  when: not file_stat.stat.exists
```

### Standalone Nginx Installation

This playbook installs Nginx on both Debian-based and RedHat-based systems by detecting the operating system family:

```yaml
- name: Install Nginx
  hosts: all
  become: yes
  tasks:
    - name: Install on Debian-based systems
      ansible.builtin.apt:
        name: nginx
        state: present
      when: ansible_facts['os_family'] == "Debian"

    - name: Install on RedHat-based systems
      ansible.builtin.yum:
        name: nginx
        state: present
      when: ansible_facts['os_family'] == "RedHat"
```

