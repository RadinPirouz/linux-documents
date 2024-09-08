# Ansible Playbook Guide

Ansible Playbooks are YAML files that automate server configuration, deployment, and management tasks. This guide provides instructions on running a playbook, explains key components, and includes examples to help you get started.

## Table of Contents
- [Ansible Playbook Guide](#ansible-playbook-guide)
  - [Table of Contents](#table-of-contents)
  - [Running an Ansible Playbook](#running-an-ansible-playbook)
    - [Example](#example)
  - [Key Concepts](#key-concepts)
  - [Example Playbooks](#example-playbooks)
    - [1. Simple APT Cache Update](#1-simple-apt-cache-update)
    - [2. Update APT Cache and Install Nginx](#2-update-apt-cache-and-install-nginx)
    - [3. Install Nginx and Copy Configuration File](#3-install-nginx-and-copy-configuration-file)
    - [4. Full Nginx Deployment: Install, Configure, and Restart](#4-full-nginx-deployment-install-configure-and-restart)
    - [Show Debug Message](#show-debug-message)
    - [Use a Shell Command](#use-a-shell-command)
    - [Playbook with Conditional Statements](#playbook-with-conditional-statements)
    - [Check File Existence Using the `stat` Module](#check-file-existence-using-the-stat-module)
    - [Standalone Nginx Installation](#standalone-nginx-installation)
    - [Create a User](#create-a-user)
    - [Install Multiple Packages](#install-multiple-packages)
      - [Using a Loop:](#using-a-loop)
      - [Using a List:](#using-a-list)
    - [Create Multiple Users](#create-multiple-users)
    - [Import Playbook Files](#import-playbook-files)

---

## Running an Ansible Playbook

To execute an Ansible Playbook, use the following command:

```bash
ansible-playbook <playbook.yaml> -i <inventory-file.ini>
```

- **`<playbook.yaml>`**: Path to your playbook file.
- **`<inventory-file.ini>`**: Path to your inventory file (can be in INI or YAML format).

### Example

```bash
ansible-playbook deploy_nginx.yaml -i inventory.ini
```

This command runs the `deploy_nginx.yaml` playbook on the hosts defined in `inventory.ini`.

## Key Concepts

- **`hosts: all`**: Defines the target hosts from the inventory on which the playbook should run.
- **`become: yes`**: Ensures tasks requiring elevated privileges (sudo) are executed as the root user.
- **Handlers**: Special tasks that are triggered by other tasks using the `notify` directive.
- **Variables**: Dynamic values that can be reused across tasks and playbooks, enhancing flexibility and maintainability.

---

## Example Playbooks

### 1. Simple APT Cache Update

This playbook updates the APT package cache on all specified hosts.

```yaml
- name: Update APT Cache
  hosts: all
  become: yes
  tasks:
    - name: Update apt-cache
      ansible.builtin.apt:
        update_cache: yes
```

### 2. Update APT Cache and Install Nginx

This playbook updates the APT cache and installs the Nginx web server.

```yaml
- name: Install Nginx and Update APT Cache
  hosts: all
  become: yes
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
  hosts: all
  become: yes
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

This playbook demonstrates a complete Nginx deployment.

```yaml
- name: Full Nginx Deployment
  hosts: all
  become: yes
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
      notify: Restart Nginx

  handlers:
    - name: Restart Nginx
      ansible.builtin.service:
        name: nginx
        state: restarted
```

### Show Debug Message

Use the `debug` module to display a message during playbook execution. This is useful for testing or providing feedback within your playbooks.

```yaml
- name: Show Debug Message
  hosts: all
  tasks:
    - name: Display debug message
      ansible.builtin.debug:
        msg: "Test Message"
```

### Use a Shell Command

Run a shell command and capture the output for further use within the playbook.

```yaml
- name: Execute Shell Command
  hosts: all
  tasks:
    - name: Run a shell command
      ansible.builtin.shell:
        cmd: echo "Hello, Ansible!"
      register: shell_output

    - name: Display Shell Output
      ansible.builtin.debug:
        msg: "Output is: {{ shell_output.stdout }}"
```

### Playbook with Conditional Statements

This playbook demonstrates the use of conditional statements to check if a file exists and take action based on the result.

```yaml
- name: Check if File Exists
  hosts: all
  tasks:
    - name: Check if file exists
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

A more reliable method to check if a file exists using the `stat` module.

```yaml
- name: Check if File Exists
  hosts: all
  tasks:
    - name: Check if file exists
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

This playbook installs Nginx on both Debian-based and RedHat-based systems by detecting the operating system family.

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

### Create a User

This playbook checks if a user exists and creates the user if it does not.

```yaml
- name: Manage User Account
  hosts: all
  become: yes
  tasks:
    - name: Check if user exists
      ansible.builtin.command:
        cmd: id new_user
      register: user_data
      ignore_errors: yes

    - name: Create user
      ansible.builtin.user:
        name: new_user
        state: present
      when: user_data.rc != 0
```

### Install Multiple Packages

These examples show how to install multiple packages using either a loop or a list.

#### Using a Loop:

```yaml
- name: Install Multiple Packages with Loop
  hosts: all
  become: yes
  tasks:
    - name: Install packages
      ansible.builtin.apt:
        name: "{{ item }}"
        state: present
      loop:
        - vim
        - git
        - nginx
```

#### Using a List:

```yaml
- name: Install Multiple Packages as a List
  hosts: all
  become: yes
  tasks:
    - name: Install packages
      ansible.builtin.apt:
        name: ["vim", "nginx", "git"]
        state: present
```

### Create Multiple Users

This playbook creates multiple users with different groups.

```yaml
- name: Create Multiple Users
  hosts: all
  become: yes
  tasks:
    - name: Create users
      ansible.builtin.user:
        name: "{{ item.name }}"
        group: "{{ item.group }}"
        state: "{{ item.state }}"
      loop:
        - { name: "radin", state: "present", group: "sudo" }
        - { name: "test", state: "present", group: "

dev" }
        - { name: "test2", state: "present", group: "test_unit" }
```

### Import Playbook Files

This allows you to split your playbooks into smaller, manageable files and include them as needed.

```yaml
- name: Nginx Setup
  import_playbook: nginx.yaml

- name: User Creation
  import_playbook: users.yaml
```

