ip path detection packet-format icmp
====================================

ip path detection packet-format icmp

Function
--------



The **ip path detection packet-format icmp** command enables the connectivity detection function and sets the packet type for connectivity detection to ICMPv4 Echo Request message.

The **undo ip path detection packet-format icmp** command restores the default settings.



By default, the connectivity detection function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ip path detection packet-format icmp src-ip** *srcip* **dst-ip** *dstip*

**undo ip path detection packet-format icmp src-ip** *srcip* **dst-ip** *dstip*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dst-ip** *dstip* | Specifies the destination IPv4 address as the detection flag. | The value is in dotted decimal notation. |
| **src-ip** *srcip* | Sets the source IPv4 address as the detection flag. | The value is in dotted decimal notation. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

This function corresponds to the IP ping function in connectivity detection on iMaster NCE-Fabric. It detects connectivity between two VMs only on an IPv4 network. iMaster NCE-Fabric automatically delivers the configuration corresponding to the **ip path detection packet-format icmp** command to the device through NETCONF, and specifies the source and destination IPv4 addresses as the detection flags. iMaster NCE-Fabric delivers the ICMPv4 Echo Request packet to the device through a Packet-out packet. The source and destination IPv4 addresses of the ICMPv4 Echo Request packet are used as those of the detection flags, respectively. After receiving the ICMPv4 Echo Reply packet corresponding to the ICMPv4 Echo Request packet, the device encapsulates the ICMPv4 Echo Reply packet into a Packet-in packet and sends the packet to iMaster NCE-Fabric. If iMaster NCE-Fabric receives an ICMPv4 Echo Reply packet within the timeout interval, the connectivity between the source and destination IPv4 addresses is normal. If iMaster NCE-Fabric does not receive any ICMPv4 Echo Reply packet within the timeout interval, the source IPv4 address is unreachable to the destination IPv4 address.This function corresponds to the IP ping function in connectivity detection on iMaster NCE-Fabric. It detects connectivity between two VMs on a Layer 2 or Layer 3 IPv4 network. iMaster NCE-Fabric automatically delivers the configuration corresponding to the **ip path detection packet-format icmp** command to the device through NETCONF, and specifies the source and destination IPv4 addresses as the detection flags. iMaster NCE-Fabric delivers the ICMPv4 Echo Request packet to the device through a Packet-out packet. The source and destination IPv4 addresses of the ICMPv4 Echo Request packet are used as those of the detection flags, respectively. After receiving the ICMPv4 Echo Reply packet corresponding to the ICMPv4 Echo Request packet, the device encapsulates the ICMPv4 Echo Reply packet into a Packet-in packet and sends the packet to iMaster NCE-Fabric. If iMaster NCE-Fabric receives an ICMPv4 Echo Reply packet within the timeout interval, the connectivity between the source and destination IPv4 addresses is normal. If iMaster NCE-Fabric does not receive any ICMPv4 Echo Reply packet within the timeout interval, the source IPv4 address is unreachable to the destination IPv4 address.


Example
-------

# Enable the connectivity detection function and set the packet type for connectivity detection to ICMPv4 Echo Request message. The device identifies ICMPv4 Echo Request messages based on the source and destination IPv4 addresses.
```
<HUAWEI> system-view
[~HUAWEI] ip path detection packet-format icmp src-ip 10.1.1.1 dst-ip 10.2.2.2

```