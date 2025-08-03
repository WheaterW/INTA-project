arp anti-attack check user-bind enable
======================================

arp anti-attack check user-bind enable

Function
--------



The **arp anti-attack check user-bind enable** command enables dynamic ARP inspection (DAI) to check ARP packets against the binding table.

The **undo arp anti-attack check user-bind enable** command disables DAI.



By default, dynamic ARP detection is disabled.


Format
------

**arp anti-attack check user-bind enable**

**undo arp anti-attack check user-bind enable**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,VLAN view,Bridge domain view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



You can run this command to enable DAI to defend against MITM attacks, preventing authorized users' data from being intercepted. A device compares the source IP address, source MAC address, interface, BD, and VLAN information in a received ARP message with binding entries. If they match, the device considers the message valid and forwards it. If they do not match, the device considers the message invalid and discards it. You can enable DAI in the interface, BD, or VLAN view. If DAI is enabled in the interface view, the device checks all ARP messages received by the interface against binding entries. If DAI is enabled in the VLAN or BD view, the device checks the ARP messages received by the interfaces that belong to the VLAN or BD against binding entries.



You can run this command to enable DAI to defend against MITM attacks, preventing authorized users' data from being intercepted. A device compares the source IP address, source MAC address, interface, and VLAN information in a received ARP message with binding entries. If they match, the device considers the message valid and forwards it. If they do not match, the device considers the message invalid and discards it. You can enable DAI in the interface or VLAN view. If DAI is enabled in the interface view, the device checks all ARP messages received by the interface against binding entries. If DAI is enabled in the VLAN view, the device checks the ARP messages received by the interfaces that belong to the VLAN against binding entries.



**Precautions**

* The M-LAG and DAI functions are mutually exclusive and cannot be configured at the same time.
* DAI is enabled based on the gratuitous ARP principle. If the source IP address of an ARP packet to be checked is all 0s, the device uses the destination IP address as the source IP address to perform DAI check. If the destination IP address matches an entry in the binding table, the device forwards the ARP packet. Otherwise, the device discards the ARP packet.For the CE6885-LL in low latency mode, ARP port rate limiting and DAI are mutually exclusive and cannot be configured together.


Example
-------

# Enable DAI on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] arp anti-attack check user-bind enable

```

# Enable DAI in VLAN 100.
```
<HUAWEI> system-view
[~HUAWEI] vlan 100
[~HUAWEI-vlan100] arp anti-attack check user-bind enable

```