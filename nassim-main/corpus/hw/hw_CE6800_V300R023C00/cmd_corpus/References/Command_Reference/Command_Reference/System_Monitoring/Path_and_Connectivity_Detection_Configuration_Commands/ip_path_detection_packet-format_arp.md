ip path detection packet-format arp
===================================

ip path detection packet-format arp

Function
--------



The **ip path detection packet-format arp** command enables the connectivity detection function and sets the packet type for connectivity detection to ARP Request packet.

The **undo ip path detection packet-format arp** command restores the default settings.



By default, the connectivity detection function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ip path detection packet-format arp** [ **src-mac** *srcmacaddr* ] [ **dst-mac** *dstmacaddr* ] **src-ip** *srcip* **dst-ip** *dstip*

**undo ip path detection packet-format arp** [ **src-mac** *srcmacaddr* ] [ **dst-mac** *dstmacaddr* ] **src-ip** *srcip* **dst-ip** *dstip*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **src-mac** *srcmacaddr* | Specifies the source MAC address as the detection flag. | The value is in H-H-H format. H is a 4-bit hexadecimal number, such as 00e0 or fc01.  If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0.  The MAC address cannot be set to FFFF-FFFF-FFFF. |
| **dst-mac** *dstmacaddr* | Specifies the destination MAC address as the detection flag. | The value is in H-H-H format. H is a 4-bit hexadecimal number, such as 00e0 or fc01.  If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0.  The MAC address cannot be set to FFFF-FFFF-FFFF. |
| **src-ip** *srcip* | Sets the source IPv4 address as the detection flag. | The value is in dotted decimal notation. |
| **dst-ip** *dstip* | Specifies the destination IPv4 address as the detection flag. | The value is in dotted decimal notation. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

This function corresponds to the MAC ping function in connectivity detection on iMaster NCE-Fabric. It detects connectivity between two VMs only on a Layer 2 network. iMaster NCE-Fabric automatically delivers the configuration corresponding to the **ip path detection packet-format arp** command to the device through NETCONF, and specifies the source and destination IPv4 addresses as the detection flags. iMaster NCE-Fabric delivers the ARP request packet to the device through a Packet-out packet. The source and destination IPv4 addresses of the ARP request packet are used as those of the detection flags, respectively. After receiving the ARP Reply packet corresponding to the ARP Request packet, the device encapsulates the ARP Reply packet into a Packet-in packet and sends the packet to iMaster NCE-Fabric. If iMaster NCE-Fabric receives an ARP Reply packet within the timeout interval, the connectivity between the source and destination IPv4 addresses is normal. If iMaster NCE-Fabric does not receive any ARP Reply packet within the timeout interval, the source IPv4 address is unreachable to the destination IPv4 address.


Example
-------

# Enable the connectivity detection function and set the packet type for connectivity detection to ARP Request packet. Specify the source and destination IPv4 addresses as the detection flags. The device identifies ARP Request packets based on the source and destination IPv4 addresses.
```
<HUAWEI> system-view
[~HUAWEI] ip path detection packet-format arp src-ip 10.1.1.1 dst-ip 10.2.2.2

```