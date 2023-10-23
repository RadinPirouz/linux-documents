in the name of god 
how to install nmap and use ESTEFADEH AZ nmap
harja "" didi khodet vared kon
harja moshkel dashti sudo bezan agar nashod -Pn ham bezan
1.update
sudo apt-get update
2.install nmap
sudo apt install nmap
3.nmap IP
nmap "your IP"
4.nmap IP,IP1,IP2
nmap "your IP,1,2"
5.nmap IP-IP100
nmap "your IP-100"
6.nmap open textfile
nmap -iL filename.txt
7.check for live system
nmap –sn "yourIP"
8.ping sweep
nmap -sP "yourIP"
9.agar ICMP masdod shode
Nmap -PN "your IP"
10. port
nmap -p "yourport"
agar nashod nmap -PN "yourip" -p "your port"
11.nmap -p port1,port2,port3-port6 IP
nmap -p "yourport,port2,port3-6" "your ip"
12.protocol
nmap -p http,https,ftp IP
13.Tcp port
nmap -p T:"port,port2" "yourIP"
15.more information
nmap -p "yourport" -sV "yourIP"
16.OS
nmap -O "yourIP" -p "yourport"
17.Fast Scan (top 100 ports)
nmap -F "yourIP"
18.Aggressive Scan = -sV , -sC , -O
nmap -A "yourip" -p "yourport"
19.whois
nmap -p "your port" --script whois-ip "your IP or domain"
20.location
nmap -p "your port" --script ip-geolocation-* "IP"
21.Web Application Firewall
nmap -p "your port" –script http-waf-detect "your domain"
22.Nmap File(Text file)
nmap -Pn -p "your port" "your IP" -oN your filename.txt
23.xml file
nmap -Pn -p "your port" "your IP" -oX filename.xml
24.grep
nmap -Pn -p "your port" "your IP" -oG filename.gnmap
25.all file
nmap -Pn -p "your port" "your IP" -oA filename
26.top port
nmap --top-ports "number" "your domain"
27.open
nmap --top-ports "number" "your domain" --open
28.Check for open ports
nmap -sT "yourIP" (TCP Scan)
nmap -sS "yourIP" (SYN Scan)
nmap -sX "yourIP" (XMAS Scan)
nmap -sF "yourIP" (FIN Scan)
nmap -sN "yourIP" (Null Scan)
