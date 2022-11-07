#!/usr/bin/env python

import scapy.all as scapy
from datetime import datetime


class ARPSpoofDetector:
    def __init__(self, iface):
        self.iface = iface
        
    def get_mac(self, ip):
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        # combining to a single request-packet
        arp_r_broadcast = broadcast / arp_request
        active_clients = scapy.srp(arp_r_broadcast, timeout=3, verbose=False)[0]

        return active_clients[0][1].hwsrc

    def sniff(self, interface):
        print("\nMonitoring for ARP Spoof...\n")
        scapy.sniff(iface=interface, store=False, prn=self.process_arp_packets)

    def process_arp_packets(self, arp_packet):
        # Identify if ARP packet contains ARP-Response (op=2)
        if arp_packet.haslayer(scapy.ARP) and arp_packet[scapy.ARP].op == 2:
            # Verify arp_response contains spoofed mac
            try:
                genuine_mac = self.get_mac(arp_packet[scapy.ARP].psrc)
                response_mac = arp_packet[scapy.ARP].hwsrc
                if genuine_mac != response_mac:
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print(f"=> ARP spoof attack detected at [{current_time}]")
            except IndexError:
                pass

    def start(self):

        self.sniff(self.iface)  

