Clearing DHCP Snooping Binding Entries
======================================

Clearing DHCP Snooping Binding Entries

#### Context

If the networking environment changes, DHCP snooping binding entries do not age immediately. However, the following information in DHCP snooping binding entries may change, causing packet forwarding errors:

* VLAN to which users belong
* Interface to which users are connected

To resolve this issue, clear all DHCP snooping binding entries manually before changing the networking environment, so that the device generates a new DHCP snooping binding table based on the new networking environment.

![](../public_sys-resources/notice_3.0-en-us.png) 

After the DHCP snooping binding entries are cleared, network communication can recover only after all the DHCP users connected to the device log in again and new binding entries are generated. Exercise caution when performing this operation.



#### Procedure

1. In the user view, clear DHCP snooping binding entries based on VLANs, interfaces, BDs, or IPv4 addresses.
   
   
   ```
   [reset dhcp snooping user-bind](cmdqueryname=reset+dhcp+snooping+user-bind)
   ```