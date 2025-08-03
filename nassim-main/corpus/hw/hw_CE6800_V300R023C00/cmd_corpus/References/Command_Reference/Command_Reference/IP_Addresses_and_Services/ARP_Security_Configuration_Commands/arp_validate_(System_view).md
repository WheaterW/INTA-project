arp validate (System view)
==========================

arp validate (System view)

Function
--------



The **arp validate** command enables the device to check whether the source MAC address in the Ethernet header of a received Address Resolution Protocol (ARP) packet matches that in the Data field of the packet.

The **undo arp validate** command disables the function.



By default, this function is disabled.


Format
------

**arp validate source-mac**

**undo arp validate source-mac**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **source-mac** | Specifies that the device checks the consistency between source MAC address in the Ethernet packet header and those in the data area of an ARP packet. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After receiving an ARP packet, the device will check the validity of the packet. The check items include but not limit to:

* Packet length
* Validity of the source and destination MAC addresses in the Ethernet header of the packet
* Packet type
* MAC address length
* IP address length
* Whether the frame of the packet is EthernetThese check items are used to check whether the format of the ARP packet matches that defined in the ARP protocol. The ARP packet of which the source MAC address in the Ethernet header does not match that in the Data field is allowed by the ARP protocol. However, the packet may be an attack packet. You can run the **arp validate source-mac** command to enable the device to check whether the source MAC address in the Ethernet header of a received ARP packet matches that in the Data field of the packet. If they match, the device considers the packet valid and allows it to pass. If they do not match, the device considers the packet an attack packet and discards it.

**Precautions**



You can run the **arp validate** command in the system view to enable the device to check whether the source MAC address in the Ethernet header of a received ARP packet matches that in the Data field of the packet. In addition, you can run the **arp validate** command in the interface view to enable the specified interface to check whether the source and destination MAC addresses in the Ethernet packet header match those in the data area of the ARP packet. If the arp validate source-mac and arp validate destination-mac commands are run in both the system view and interface view, the specified interface checks whether the source and destination MAC addresses in the Ethernet packet header match those in the data area of the ARP packet, and other interfaces check whether the source MAC address in the Ethernet header of the received ARP packet matches that in the Data field of the packet.




Example
-------

# Enable the device to check whether the source MAC address in the Ethernet header of a received ARP packet matches that in the Data field of the packet.
```
<HUAWEI> system-view
[~HUAWEI] arp validate source-mac

```