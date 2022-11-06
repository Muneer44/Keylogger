import subprocess
import optparse  # Take CLI arguments from user and parse into code
import re  # extract MAC using RegEX


class MacChanger:
    def __init__(self, iface, mac):
        self.arguments = {"interface": iface, "mac_addr": mac}

    def get_current_mac(self, interface):
        network_details = str(subprocess.check_output(["ifconfig", interface]))
        mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", network_details)

        # Error Handling
        if not mac_result:
            print(
                f"Error: The interface \"{interface}\" has no mac address")
            exit()
        else:
            return mac_result.group(0)

    def change_mac(self, interface, mac_addr):
        print(f"Changing MAC address of interface \"{interface}\" to \"{mac_addr}\" \n")
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", mac_addr])
        subprocess.call(["ifconfig", interface, "up"])

    def start(self):
        current_mac = self.get_current_mac(self.arguments['interface'])
        print(f"\nCurrent MAC Address : {current_mac}")

        self.change_mac(self.arguments['interface'], self.arguments['mac_addr'])

        current_mac = self.get_current_mac(self.arguments['interface'])
        if self.arguments['mac_addr'] == current_mac:
            print(f"-> MAC address has been successfully changed")
        else:
            print("Error: MAC address did not get changed.")


