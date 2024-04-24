
# Ansible Module Usage

Ansible modules are standalone scripts that can be used within Ansible to perform various tasks on managed nodes. Here are some examples of using Ansible modules:

## Basic Module Execution

To execute a module against all hosts in your inventory file:

```bash
ansible -m <module> all -i <inventory_file>
```

Example:

```bash
ansible -m ping all -i server.ini
```

## Module Execution with Arguments

You can pass arguments to modules using the `-a` flag:

```bash
ansible -m <module> -a <arguments> -i <inventory_file> <group_of_servers>
```

Examples:

```bash
ansible -m command -a "uptime" -i server.ini all
ansible -m command -a "uname -a" -i server.ini all
```

## Running Commands as sudo

If the command requires root privileges, you can use the `--become` or `-b` flag:

```bash
ansible -m <module> -a "<command>" --become -i <inventory_file> <group_of_servers>
```

Example:

```bash
ansible -m command -a "sudo reboot" -i server.ini all
```

## More Examples

Here are some additional examples demonstrating Ansible module usage:

- Gathering facts from all hosts:

```bash
ansible -m setup all -i server.ini
```

- Copying a file to all hosts:

```bash
ansible -m copy -a "src=/path/to/src/file dest=/path/to/destination/" -i server.ini all
```

- Installing a package using apt module:

```bash
ansible -m apt -a "name=<package_name> state=present" -i server.ini all
```

- Restarting a service:

```bash
ansible -m service -a "name=<service_name> state=restarted" -i server.ini all
```

