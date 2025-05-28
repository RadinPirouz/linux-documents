# Linux Runlevels Guide

This document outlines the standard runlevels for **Red Hat** and **Debian**-based systems. Runlevels are used by `init` systems to define different states or modes of operation for the system.

---

## 📊 Runlevels Overview

| Runlevel | Description                          | Red Hat      | Debian          |
| -------- | ------------------------------------ | ------------ | --------------- |
| 0        | Halt                                 | ✅ Supported  | ✅ Supported     |
| 1        | Single User Mode                     | ✅ Supported  | ✅ Supported     |
| 2        | Multi-user (No Network)              | ❌ (HaveNet)  | ✅ Supported     |
| 3        | Multi-user (Network, No GUI)         | ✅ Supported  | ✅ Supported     |
| 4        | Custom/User Defined                  | ✅ Supported  | ✅ Supported     |
| 5        | Multi-user (GUI Mode) / Halt *(err)* | ❌ (GUI Mode) | ❌ (Halt/Error?) |
| 6        | Reboot                               | ✅ Supported  | ✅ Supported     |

> 💡 **Note**:
>
> * On **Red Hat**, runlevel 5 typically starts the system with a graphical user interface (GUI).
> * On **Debian**, runlevel 5 is often unused or reserved for custom setups.
> * Runlevel behavior can be customized depending on system configuration.

---

## 🔧 Commands

### Check Current Runlevel

```bash
runlevel
```

### Change Runlevel

```bash
telinit <runlevel>
```

or

```bash
init <runlevel>
```

> ⚠️ Changing runlevels may stop or restart services. Use with caution, especially on production systems.

---

## 📚 Additional Tips

* Modern Linux systems (especially systemd-based) may not rely on traditional runlevels. Instead, they use *targets*. Example:

  ```bash
  systemctl get-default
  systemctl isolate graphical.target
  ```

