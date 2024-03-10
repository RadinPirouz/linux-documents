```markdown
# iptables
## First Whitelist Port and Block Ports at the End
```



```bash
iptables -A/-I/-D INPUT/OUTPUT/FORWARD -i/-o interface -s/-d address -p tcp/udp/icmp --sport/--dport 80 -j ACCEPT/REJECT/DROP/LOG/MASQUARATE 
```

- `-A`: Append
- `-I`: Insert
- `-D`: Delete
- `-i`: Input interface
- `-o`: Output interface
- `-s`: Source
- `-d`: Destination
- `-p`: Protocol
- `--sport`: Source port
- `--dport`: Destination port
- `-j`: Action
  - `ACCEPT`: Accept the packet
  - `REJECT`: Reject the packet with an appropriate ICMP message
  - `DROP`: Silently discard the packet
  - `LOG`: Log the packet
  - `MASQUERADE`: Source NAT

### Examples:

- `iptables -nvL`: Print Iptables Rules
- `iptables -P INPUT DROP`: Drop All Incoming Packets
- `iptables -P OUTPUT DROP`: Drop All Outgoing Packets
- `iptables -A INPUT -p tcp --dport 22 -j ACCEPT`: Accept Incoming Traffic to Port 22 with TCP Protocol
- `iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT`: Accept Outgoing Traffic from Port 22 with TCP Protocol
- `iptables -A INPUT -p tcp -s 192.168.1.100 -j DROP`: Drop All Packets Incoming With TCP Protocol From 192.168.1.100
- `iptables -A INPUT -p tcp --dport 443 -j ACCEPT`: Accept Incoming Traffic to Port 443 (HTTPS) with TCP Protocol
- `iptables -A INPUT -p tcp -m multiport --dport 22,443,80,3306 -j ACCEPT`: Accept Incoming Traffic to Multiple Ports: 22 (SSH), 80 (HTTP), 3306 (Database), 443 (HTTPS) with TCP Protocol
- `iptables -A INPUT -p tcp -m multiport --dport 22,443,80,3306 -d 192.168.10.0/24 -j ACCEPT`: Accept Incoming Traffic to Multiple Ports: 22 (SSH), 80 (HTTP), 3306 (Database), 443 (HTTPS) with TCP Protocol to Destination 192.168.10.0
- `iptables -A INPUT -p tcp --dport 80 -m limit --limit 100/minute --limit-burst 200 -j ACCEPT`: Allow incoming TCP traffic on port 80 with rate limiting
- `iptables -t NAT -A PREROUTING -i ens33 -p tcp --dport 80 -j REDIRECT --to-port 443`: Redirect traffic from port 80 to port 443 using NAT

### Saving rules for permanent:

To save the rules for permanent usage, you can install the `iptables-persistent` package:

```bash
apt install iptables-persistent
```

Then, save the rules to the appropriate file:

```bash
iptables-save > /etc/iptables/rule.v4
```
