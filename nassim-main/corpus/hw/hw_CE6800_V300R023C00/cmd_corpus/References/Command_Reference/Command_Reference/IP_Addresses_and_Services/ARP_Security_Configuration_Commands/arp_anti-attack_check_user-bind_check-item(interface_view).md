arp anti-attack check user-bind check-item(interface view)
==========================================================

arp anti-attack check user-bind check-item(interface view)

Function
--------



The **arp anti-attack check user-bind check-item** command configures items to be checked against the binding table for ARP packets on an interface.

The **undo arp anti-attack check user-bind check-item** command restores the default check items for ARP packets.



By default, the device checks the IP address, MAC address, and VLAN ID of an ARP packet against the binding table.


Format
------

**arp anti-attack check user-bind check-item** { **ip-address** | **mac-address** | **vlan** } \*

**undo arp anti-attack check user-bind check-item**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip-address** | Indicates that the check item is an IP address. | - |
| **mac-address** | Indicates that the check item is a MAC address. | - |
| **vlan** | Indicates that the check item is VLAN information. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After DAI is enabled on an interface, the device compares the source IP address, source MAC address, interface, and VLAN information in a received ARP packet with DHCP snooping binding entries. If they match, the device considers the packet valid and forwards it. If they do not match, the device considers the packet invalid and discards it.To allow ARP packets that match only one or two entries in the binding table to pass through, configure the device to check only one or two entries in the binding table.

**Prerequisites**

DAI has been enabled on the interface using the **arp anti-attack check user-bind enable** command.

**Precautions**

The configured items to be checked against binding entries for ARP packets do not take effect on users configured with static binding entries, meaning that the device still checks ARP packets of these users against the static binding entries.


Example
-------

# Configure a device to check only IP addresses in ARP packets against the binding table on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] arp anti-attack check user-bind enable
[~HUAWEI-100GE1/0/1] arp anti-attack check user-bind check-item ip-address

```