arp validate
============

arp validate

Function
--------



The **arp validate** command enables an interface to check the consistency between source and destination Media Access Control (MAC) addresses in the Ethernet packet header and those in the data area of an Address Resolution Protocol (ARP) packet.

The **undo arp validate** command disables an interface from checking the consistency between source and destination MAC addresses in the Ethernet packet header and those in the data area of an ARP packet.



By default, the interface does not perform a consistency check.


Format
------

**arp validate source-mac**

**arp validate destination-mac**

**arp validate** { **destination-mac** **source-mac** | **source-mac** **destination-mac** }

**undo arp validate source-mac**

**undo arp validate destination-mac**

**undo arp validate** { **destination-mac** **source-mac** | **source-mac** **destination-mac** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **destination-mac** | Specifies that an interface checks the consistency between the destination MAC address in the Ethernet packet header and that in the data area of an ARP packet. | - |
| **source-mac** | Specifies that an interface checks the consistency between source MAC address in the Ethernet packet header and those in the data area of an ARP packet. | - |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Layer 2 Eth-Trunk interface view,Eth-Trunk interface view,Layer 2 GE interface view,VBDIF interface view,Interface group view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a Metro Ethernet, various forms of attacks on ARP entries exist. To ensure network security, you need to prevent ARP attacks on the access layer or convergence layer of the network.To prevent ARP spoofing, the arp validate command is used to enable an interface to check the consistency between source and destination MAC addresses in the Ethernet packet header and those in the data area of an ARP packet. If an inconsistency is detected, the ARP packet is directly discarded. If no inconsistency is detected, the ARP packet is accepted.When using the arp validate command, note the following:

* If source-mac is selected:
* The interface performs a consistency check on the source MAC address after receiving an ARP request packet.
* The interface performs a consistency check only on the source MAC address after receiving an ARP response packet.
* If destination-mac is selected:
* The interface does not perform a consistency check after receiving an ARP request packet. No consistency check is required because the received ARP request packet is a broadcast packet.
* The interface performs a consistency check on the destination MAC address after receiving an ARP response packet.
* If source-mac and destination-mac are selected:
* The interface performs a consistency check only on the source MAC address after receiving an ARP request packet.
* The interface performs a consistency check on the source and destination MAC addresses after receiving an ARP response packet.

**Precautions**

The sub-interfaces and the VLANIF interfaces are logical interfaces. The implementation of the device requires that the MAC address of a logical interface be the same as that of the corresponding physical interface.

* The arp validate command can be run on interfaces, but not on sub-interfaces. When a sub-interface receives an ARP packet through its interface, it checks whether the source and destination MAC addresses in the Ethernet packet header are the same as those in the data area of the ARP packet by following the rules configured on the interface.
* The arp validate command can be run on member interfaces of VLANIF interfaces, but not on VLANIF interfaces. When a VLANIF interface receives an ARP packet through its interface, it checks whether the source and destination MAC addresses in the Ethernet packet header are the same as those in the data area of the ARP packet by following the rules configured on the member interface.

Example
-------

# Enable the interface to perform a consistency check on the source and destination MAC addresses in the header of an Ethernet packet and the source and destination MAC addresses in the data area of an ARP packet.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] arp validate source-mac destination-mac

```