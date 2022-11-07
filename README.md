# Python based Network Manipulation Suite


The Network Manipulation Suite is extinsively designed to ease the network handling tasks. 
It includes features such as :
- MAC Spoofing
- Network Clients Scanning
- ARP Spoofing
- ARP Spoof Detector
- Packet Sniffer 


This application exclusively depends on Python 3.* and Linux.


## Installation process
clone this repository with `git clone`, install the `scapy` module and execute the `Handler.py` file.
```
user@host:~$ git clone https://github.com/Muneer44/Network-Manipulation-Suite.git
user@host:~$ cd Network-Manipulation-Suite
user@host:~/Network-Manipulation-Suite$ pip install scapy
user@host:~/Network-Manipulation-Suite$ sudo python3 Network-Manipulation-Suite/Handler.py
```

*The `sudo` command is required as the script performs core system functionalities.*

*Notice that the existence of `scapy` may require the virtual environment to have scapy module installed for executing in the venv interpreter (if you use one),
instead of just using the system interpreter.*

## Usage
```
 
 ┌┐┌┌─┐┌┬┐┬ ┬┌─┐┬─┐┬┌─  ┌┬┐┌─┐┌┐┌┬┌─┐┬ ┬┬  ┌─┐┌┬┐┬┌─┐┌┐┌  
 │││├┤  │ ││││ │├┬┘├┴┐  │││├─┤││││├─┘│ ││  ├─┤ │ ││ ││││  
 ┘└┘└─┘ ┴ └┴┘└─┘┴└─┴ ┴  ┴ ┴┴ ┴┘└┘┴┴  └─┘┴─┘┴ ┴ ┴ ┴└─┘┘└┘  
                   ┌─┐┬ ┬┬┌┬┐┌─┐┬                         
                   └─┐│ ││ │ ├┤ │                         
                   └─┘└─┘┴ ┴ └─┘o                  
                                   
---------------------------------------------------------

=> CHOOSE YOUR OPTION : 

1] MAC Spoofer 
2] Network Scanner 
3] ARP Spoofer 
4] ARP Spoof Detector
5] Packet Sniffer 

0] Exit 

=>

```
### I. MAC Spoofer
- *Change device's MAC address to desired new MAC address.*

![MAC-Spoofer](https://user-images.githubusercontent.com/117259069/200348959-5992fa38-5199-4404-871c-c202b7039b8e.gif)

### II. Network Scanner
- *Scan for active clients in the network.*

![Network-Scanner-m](https://user-images.githubusercontent.com/117259069/200354111-be6f9163-c157-4f99-80df-7b8febfb03dc.gif)

### III. ARP Spoofer
- *Perform MiTM(Man in The Middle).*

![ARP-Spoofer](https://user-images.githubusercontent.com/117259069/200348952-fe250132-05fe-4dc4-8463-d1d45a628710.gif)

### IV. ARP Spoof Detector
- *Detects and Alerts on being attacked*
- The program works even if executed in the middle of an ongoing ARP-Spoof attack.

![ARP-Detector](https://user-images.githubusercontent.com/117259069/200347861-1aa659f0-5624-4c9c-85a5-3fdd5bf14365.gif)

### V. Packet Sniffer
- *Sniff network packets, and filter to retrieve remote Host's 'requested URL and Potential Credentials'*
- Notice 'ARP Spoofer' is separately started in a different terminal prior to packet sniffing.

![Packet-Sniffer](https://user-images.githubusercontent.com/117259069/200348965-f82ce63b-a873-436c-aafb-2e1947e41131.gif)

NOTE: This function is deliberately limited to HTTP websites only to prevent malicious use.


## Legal Disclaimer
The use of code contained in this repository, either in part or in its totality,
for engaging targets without prior mutual consent is illegal. **It is
the end user's responsibility to obey all applicable local, state and
federal laws.**

This script is purely intended for educational purpose [PoC]. Do not use it to compromise any unauthorized device, demonstrate on your own device only.
