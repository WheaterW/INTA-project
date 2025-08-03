arp anti-attack check user-bind check-item
==========================================

arp anti-attack check user-bind check-item

Function
--------



The **arp anti-attack check user-bind check-item** command configures items to be checked against binding entries for ARP packets.

The **undo arp anti-attack check user-bind check-item** command restores the default check items.



By default, a device checks IP addresses, MAC addresses, and interface information of ARP packets against binding entries.


Format
------

**arp anti-attack check user-bind check-item** { **ip-address** | **mac-address** | **interface** } \*

**undo arp anti-attack check user-bind check-item**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip-address** | Indicates that the check item is an IP address. | - |
| **mac-address** | Indicates that the check item is a MAC address. | - |
| **interface** | Indicates that interface information is checked against binding entries for ARP packets. | - |



Views
-----

VLAN view,Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After DAI is enabled in a VLAN or BD, the device compares the source IP address, source MAC address, and interface number in an ARP packet with entries in the binding table. If a matching entry is found, the device considers the ARP packet valid and allows the ARP packet to pass through, otherwise, the device considers that the ARP packet is an attack packet and discards it.To allow some special ARP packets that match only one or two items in binding entries to pass through, configure the device to check ARP packets according to one or two specified items in binding entries.Only the CE6863H, CE6863H-K, CE6881H, and CE6881H-K support detection in a BD.




Example
-------

# Configure the device to check IP addresses in ARP packets from VLAN 100.
```
<HUAWEI> system-view
[~HUAWEI] vlan 100
[*HUAWEI-vlan100] arp anti-attack check user-bind enable
[*HUAWEI-vlan100] arp anti-attack check user-bind check-item ip-address

```