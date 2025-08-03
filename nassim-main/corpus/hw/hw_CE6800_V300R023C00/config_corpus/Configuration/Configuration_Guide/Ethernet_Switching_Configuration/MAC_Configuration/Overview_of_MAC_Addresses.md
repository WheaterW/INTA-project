Overview of MAC Addresses
=========================

Overview of MAC Addresses

#### Definition

A Media Access Control (MAC) address, also called a physical address, hardware address, or link address, is burned into the network interface card (NIC) of a network device by a vendor to uniquely identify the device's location. A MAC address consists of 48 bits and is displayed as a 12-digit hexadecimal number. Among the 48 bits, bits 0 to 23 are assigned by the Internet Engineering Task Force (IETF) or other institutions to identify vendors, and bits 24 to 47 are the unique ID assigned by vendors to identify their NICs.


#### Purpose

An IP address cannot identify a user over the Internet because the IP address is only a logical identifier and can be modified. To address this problem, a MAC address is used to uniquely identify a user.

MAC addresses fall into the following types:

* Physical MAC address: uniquely identifies a terminal on an Ethernet network and is the globally unique hardware address of the terminal.
* Broadcast MAC address: identifies all terminals on a LAN and is all 1s (FF-FF-FF-FF-FF-FF).
* Multicast MAC address: identifies a group of terminals on a LAN. MAC addresses, excluding broadcast MAC addresses, are multicast ones if their eighth bit is 1, for example, 01-00-00-00-00-00. The multicast MAC address starting from 01-80-c2 is the bridge protocol data unit (BPDU) MAC address, and is often used as the destination MAC address in protocol packets to indicate the protocol type.