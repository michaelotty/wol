#!/bin/python3
"""Wake supplied MAC address with WoL."""

import argparse
import json
import socket


def wake_on_lan():
    """Wake up the device with specified MAC address."""
    with open("mac_addresses.json", encoding="utf-8") as fp:
        mac_addresses = json.load(fp)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "pc_choice", help="Choose a PC name to wake", choices=mac_addresses.keys()
    )
    args = parser.parse_args()

    mac_address = mac_addresses[args.pc_choice]
    mac_address = mac_address.replace(":", "")
    mac_address = bytes.fromhex(mac_address)

    packet = bytes.fromhex("FFFFFFFFFFFF") + mac_address * 16

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as sock:
        print("Waking", args.pc_choice, "on", mac_addresses[args.pc_choice])
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        for _ in range(5):
            sock.sendto(packet, ("192.168.1.255", 9))
            # NOTE: Get this to work, regardless of our subnet


if __name__ == "__main__":
    wake_on_lan()
