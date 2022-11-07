# Python based Network Manipulation Suite

[![LinkedIn](https://img.shields.io/badge/Reddit-EONRaider-FF4500?style=flat-square&logo=reddit)](https://www.linkedin.com/in/muneer44/)
[![Discord](https://img.shields.io/badge/Discord-EONRaider-7289DA?style=flat-square&logo=discord)](https://discord.gg/KVjWBptv)
[![Twitter](https://img.shields.io/badge/Twitter-eon__raider-38A1F3?style=flat-square&logo=twitter)](https://twitter.com/intent/follow?screen_name=eon_raider)

The Network Manipulation Suite is extinsively designed to ease the network handling tasks. 
It includes features such as :
- MAC Spoofing
- Network Clients Scanning
- ARP Spoofing
- ARP Spoof Detector
- Packet Sniffer 


This application depends exclusively on the Python 3.* 


## Demo
![sniffer_demo](https://user-images.githubusercontent.com/15611424/178045423-067df4ec-1853-400e-9b5a-10154cb6fcc1.gif)

## Installation process
clone this repository with `git clone`, install the `scapy` module and execute the `Handler.py` file.
```
user@host:~$ git clone https://github.com/Muneer44/Network-Manipulation-Suite.git
user@host:~$ cd Network-Manipulation-Suite
user@host:~/packet-sniffer$ pip install scapy
user@host:~/packet-sniffer$ sudo python3 Network-Manipulation-Suite/Handler.py
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


## Legal Disclaimer
The use of code contained in this repository, either in part or in its totality,
for engaging targets without prior mutual consent is illegal. **It is
the end user's responsibility to obey all applicable local, state and
federal laws.**

Developers assume **no liability** and are not
responsible for misuses or damages caused by any code contained
in this repository in any event that, accidentally or otherwise, it comes to
be utilized by a threat agent or unauthorized entity as a means to compromise
the security, privacy, confidentiality, integrity, and/or availability of
systems and their associated resources. In this context the term "compromise" is
henceforth understood as the leverage of exploitation of known or unknown vulnerabilities
present in said systems, including, but not limited to, the implementation of
security controls, human- or electronically-enabled.

The use of this code is **only** endorsed by the developers in those
circumstances directly related to **educational environments** or
**authorized penetration testing engagements** whose declared purpose is that
of finding and mitigating vulnerabilities in systems, limiting their exposure
to compromises and exploits employed by malicious agents as defined in their
respective threat models.
