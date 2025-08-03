ip path detection packet-format icmpv6
======================================

ip path detection packet-format icmpv6

Function
--------



The **ip path detection packet-format icmpv6** command enables connectivity detection and sets the packet type for connectivity detection to ICMPv6 Echo Request message.

The **undo ip path detection packet-format icmpv6** command restores the default settings.



By default, the connectivity detection function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ip path detection packet-format icmpv6 src-ipv6** *srcip* **dst-ipv6** *dstip*

**undo ip path detection packet-format icmpv6 src-ipv6** *srcip* **dst-ipv6** *dstip*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dst-ipv6** *dstip* | Sets the destination IPv6 address as the detection flag. | The value is a 32-digit hexadecimal number, in the format X:X:X:X:X:X:X:X. |
| **src-ipv6** *srcip* | Sets the source IPv6 address as the detection flag. | The value is a 32-digit hexadecimal number, in the format X:X:X:X:X:X:X:X. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

This function corresponds to the IPv6 ping function in connectivity detection on iMaster NCE-Fabric. It detects connectivity between two VMs only on an IPv6 network. iMaster NCE-Fabric automatically delivers the configuration corresponding to the **ip path detection packet-format icmpv6** command to the device through NETCONF, and specifies the source and destination IPv6 addresses as the detection flags. iMaster NCE-Fabric delivers the ICMPv6 Echo Request packet to the device through a Packet-out packet. The source and destination IPv6 addresses of the ICMPv6 Echo Request packet are used as those of the detection flags, respectively. After receiving the ICMPv6 Echo Reply packet corresponding to the ICMPv6 Echo Request packet, the device encapsulates the ICMPv6 Echo Reply packet into a Packet-in packet and sends the packet to iMaster NCE-Fabric. If iMaster NCE-Fabric receives an ICMPv6 Echo Reply packet within the timeout interval, the connectivity between the source and destination IPv6 addresses is normal. If iMaster NCE-Fabric does not receive any ICMPv6 Echo Reply packet within the timeout interval, the source IPv6 address is unreachable to the destination IPv6 address.This function corresponds to the IPv6 ping function in connectivity detection on iMaster NCE-Fabric. It detects connectivity between two VMs only on an IPv6 over IPv4 VXLAN network. iMaster NCE-Fabric automatically delivers the configuration corresponding to the **ip path detection packet-format icmpv6** command to the device through NETCONF, and specifies the source and destination IPv6 addresses as the detection flags. iMaster NCE-Fabric delivers the ICMPv6 Echo Request packet to the device through a Packet-out packet. The source and destination IPv6 addresses of the ICMPv6 Echo Request packet are used as those of the detection flags, respectively. After receiving the ICMPv6 Echo Reply packet corresponding to the ICMPv6 Echo Request packet, the device encapsulates the ICMPv6 Echo Reply packet into a Packet-in packet and sends the packet to iMaster NCE-Fabric. If iMaster NCE-Fabric receives an ICMPv6 Echo Reply packet within the timeout interval, the connectivity between the source and destination IPv6 addresses is normal. If iMaster NCE-Fabric does not receive any ICMPv6 Echo Reply packet within the timeout interval, the source IPv6 address is unreachable to the destination IPv6 address.


Example
-------

# Enable the connectivity detection function and set the packet type for connectivity detection to ICMPv6 Echo Request message. The device identifies ICMPv6 Echo Request messages based on the source and destination IPv6 addresses.
```
<HUAWEI> system-view
[~HUAWEI] ip path detection packet-format icmpv6 src-ipv6 2001:db8:1::1 dst-ipv6 2001:db8:2::2

```