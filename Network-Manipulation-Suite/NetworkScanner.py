#!/usr/bin/env python

"""Manually crafting network packets to scan hosts in a network using scapy module!"""

import scapy.all as scapy


class NetworkScanner:
    def __init__(self, target):
        if not target:
            print("\n-> Target argument missing!")
            exit()

        self.target = target

    def scan_clients(self, ip):
        print("Scanning for clients : ")
        arp_request = scapy.ARP(pdst=ip)  # Requests IP for MAC addr (who has...)
        # create Ethernet frame and send to the dst address
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        # Combine individual requests with ether frame
        arp_r_broadcast = broadcast / arp_request
        active_clients = scapy.srp(arp_r_broadcast, timeout=3, verbose=False)[
            0]  # Send and Receive the frames

        """extract useful data from active_clients list and store as a dictionary within list"""
        clients_list = []
        for client in active_clients:
            # Storing each client's data in a dict
            client_dict = {"ip": client[1].psrc, "mac": client[1].hwsrc}
            # appending client dicts to a single list
            clients_list.append(client_dict)
        return clients_list

    def print_result(self, clients_list):
        print("__________________________________________")
        print("IP \t\t\t MAC Address")
        print("------------------------------------------")
        if clients_list:
            for client in clients_list:
                print(client["ip"] + "\t \t" + client["mac"])
        else:
            print(f"-> No active clients found in : '{self.target}'")

    def start(self):
        active_clients_list = self.scan_clients(self.target)
        self.print_result(active_clients_list)



