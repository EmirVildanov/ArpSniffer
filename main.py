from __future__ import print_function
from scapy.all import *
from scapy.layers.l2 import ARP, Ether

from oui_file_worker import get_mac_vendor
from utils import print_red, print_green


def handle_arp_packet(packet):
    if packet[ARP].op == 1:
        print_red('ARP Request:')
        print(packet.summary())
        print(f"Vendor mac: {packet[Ether].src}")
        print(f"Vendor: {get_mac_vendor(packet[Ether].src)}")
    elif packet[ARP].op == 2:
        print_green('ARP Reply:')
        print(packet.summary())
        print(f"Vendor mac: {packet[Ether].src}")
        print(f"Vendor: {get_mac_vendor(packet[Ether].src)}")
    return


def get_interfaces():
    return list(IFACES.data.keys())


if __name__ == "__main__":
    print(f"Default iface: {conf.iface}")

    # in case you want to pass program another iface
    ifaces = get_interfaces()
    chosen_iface_index = random.randrange(0, len(ifaces))
    chosen_iface = ifaces[chosen_iface_index]
    print(f"Random iface: {chosen_iface}")

    sniff(filter="arp", iface=conf.iface, prn=handle_arp_packet)
    print("program finished")
