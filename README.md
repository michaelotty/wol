# Wake on LAN utility

Populate the mac_addresses.json file with all the PCs you would like to be able to wake.
Set the PC up to accept magic packets. Run the command
`python wake_on_lan.py pc1` with the name of the pc to wake as written in the json file.

If you are having issues, you can run wireshark on the PC with the filter set to `wol`
to see if the packets are being recieved. Otherwise, check your power saving settings
and settings in network driver as well as BIOS setup.