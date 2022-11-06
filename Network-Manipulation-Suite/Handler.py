#!/usr/bin/env python

import MACSpoofer
import NetworkScanner
import ARPSpoofer
import ARPSpoofDetector
import PacketSniffer
import time


print(r""" 
 ┌┐┌┌─┐┌┬┐┬ ┬┌─┐┬─┐┬┌─  ┌┬┐┌─┐┌┐┌┬┌─┐┬ ┬┬  ┌─┐┌┬┐┬┌─┐┌┐┌  
 │││├┤  │ ││││ │├┬┘├┴┐  │││├─┤││││├─┘│ ││  ├─┤ │ ││ ││││  
 ┘└┘└─┘ ┴ └┴┘└─┘┴└─┴ ┴  ┴ ┴┴ ┴┘└┘┴┴  └─┘┴─┘┴ ┴ ┴ ┴└─┘┘└┘  
                   ┌─┐┬ ┬┬┌┬┐┌─┐┬                         
                   └─┐│ ││ │ ├┤ │                         
                   └─┘└─┘┴ ┴ └─┘o                  
                                   """)
print("---------------------------------------------------------")


def options(choice):
    if choice == "0":  # Exit
        print("Program terminated with Exit code.")
        exit()

    elif choice == "1":  # MAC Changer
        iface = input("Enter interface: ")
        mac = input("Enter new MAC Addr: ")
        mac_changer = MACSpoofer.MacChanger(iface, mac)
        mac_changer.start()

    elif choice == "2":  # Network Scanner
        target_address = input("Enter target IP addr or CIDR IP range: ")
        network_scanner = NetworkScanner.NetworkScanner(target_address)
        network_scanner.start()

    elif choice == "3":  # ARP Spoofing
        target_address = input("Enter target IP addr: ")
        gateway_address = input("Enter gateway IP addr: ")
        arp_spoof = ARPSpoofer.ARPSpoof(target_address, gateway_address)
        arp_spoof.start()

    elif choice == "4":  # ARP Spoof Detector
        arp_spoof_detector = ARPSpoofDetector.ARPSpoofDetector()
        arp_spoof_detector.start()

    elif choice == "5":  # Packet Sniffer
        packet_sniffer = PacketSniffer.PacketSniffer()
        packet_sniffer.start()

    else:
        print(choice)
        print(f"Invalid option: {choice} \nChoose from options 1-5")
        time.sleep(2)
        handler_start()


def handler_start():
    print("\n=> CHOOSE YOUR OPTION : \n")
    choice = input("1] MAC Spoofer \n2] Network Scanner \n3] ARP Spoofer \n4] ARP Spoof Detector"
                   "\n5] Packet Sniffer \n\n0] Exit \n\n=>")
    options(choice)


handler_start()
