arp l2-proxy enable
===================

arp l2-proxy enable

Function
--------



The **arp l2-proxy enable** command enables Layer 2 proxy ARP.

The **undo arp l2-proxy enable** command disables Layer 2 proxy ARP.



By default, Layer 2 proxy ARP is disabled.


Format
------

**arp l2-proxy enable**

**undo arp l2-proxy enable**


Parameters
----------

None

Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After receiving an ARP request packet, the device broadcasts the packet in its broadcast domain. If the device receives a large number of ARP request packets in a short period of time and broadcasts the packets, excessive ARP request packets are forwarded in the broadcast domain. As a result, the bandwidth is wasted, and traffic congestion may occur.To resolve this problem, run the **arp l2-proxy enable** command to enable Layer 2 proxy ARP on the device. After receiving an ARP request packet, the device checks whether the destination IP address in the packet matches an ARP entry. If a matching ARP entry is found, the device sends an ARP reply packet with the MAC address of the destination. If no matching ARP entry is found, the device discards the packet.



**Precautions**



Layer 2 proxy ARP cannot be configured in the following situations:

A VLANIF interface has been configured in the VLAN where Layer 2 proxy ARP needs to be configured.




Example
-------

# Enable VLAN-based Layer 2 proxy ARP.
```
<HUAWEI> system-view
[~HUAWEI] vlan 10
[*HUAWEI-vlan10] arp l2-proxy enable

```