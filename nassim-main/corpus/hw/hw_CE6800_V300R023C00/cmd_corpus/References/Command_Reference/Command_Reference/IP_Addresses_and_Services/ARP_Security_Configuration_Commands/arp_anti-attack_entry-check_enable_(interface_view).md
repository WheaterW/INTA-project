arp anti-attack entry-check enable (interface view)
===================================================

arp anti-attack entry-check enable (interface view)

Function
--------



The **arp anti-attack entry-check enable** command enables fixed Address Resolution Protocol (ARP) and configures the fixed ARP mode.

The **undo arp anti-attack entry-check enable** command disables fixed ARP.



By default, fixed ARP is disabled.


Format
------

**arp anti-attack entry-check fixed-all enable**

**arp anti-attack entry-check fixed-mac enable**

**arp anti-attack entry-check send-ack enable**

**undo arp anti-attack entry-check** [ **fixed-all** | **fixed-mac** | **send-ack** ] **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **fixed-mac** | Specifies the fixed-mac mode of fixed ARP. | - |
| **send-ack** | Specifies the send-ack mode of fixed ARP. | - |
| **fixed-all** | Specifies the fixed-all mode of fixed ARP. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the device receives the first ARP packet from a user, the device generates an ARP entry for the user. If the information carried in subsequent ARP packets sent by the user changes, the ARP entry is updated. If attackers forge and send ARP packets to update ARP entries of authorized users, the device learns incorrect ARP entries and authorized users cannot use the network normally. To resolve this problem, run the **arp anti-attack entry-check enable** command to enable fixed ARP. After a device generates an ARP entry for a user, the device either allows specific information in the ARP entry to be updated or prohibits any information to be updated. Fixed ARP can be implemented in the following modes:

* Fixed-all mode: After receiving an ARP packet, the device checks whether the MAC address, interface information, and VLAN ID in the packet match an ARP entry in the ARP binding table. If a matching ARP entry exists, the device considers the packet valid and allows it to pass. If no matching entry exists, the device considers the packet an attack packet and discards it.
* Fixed-MAC mode: After receiving an ARP packet, the device is allowed to update interface information and VLAN ID in the ARP entry. However, the MAC address in the ARP entry cannot be updated.
* Send-ack mode: After receiving an ARP packet, the device constructs an ARP request packet with the destination IP address as the IP address in the ARP entry (also the source IP address in the received ARP packet) and broadcasts it. If the device receives a corresponding ARP reply packet, the ARP entry will be updated based on the received ARP reply packet. Otherwise, the ARP entry cannot be updated.

**Configuration Impact**



After the **arp anti-attack entry-check enable** command is run, the device will not update an ARP entry when the MAC address in subsequent ARP packets sent by the user changes. As a result, the device cannot update ARP entries, which may cause service interruptions.



**Precautions**

You can enable fixed ARP in the system view or in the interface view. They have the following differences:

* When you run the **arp anti-attack entry-check enable** command in the system view, fixed ARP is enabled for all interfaces.
* When you run the **arp anti-attack entry-check enable** command in the interface view, fixed ARP is enabled for a specified interface.Fixed ARP enabled in the system view is independent upon that enabled in the interface view.


Example
-------

# Enable fixed ARP for a VLANIF interface.
```
<HUAWEI> system-view
[~HUAWEI] vlan 20
[*HUAWEI-vlan20] quit
[*HUAWEI] interface vlanif 20
[*HUAWEI-vlanif20] arp anti-attack entry-check fixed-mac enable

```