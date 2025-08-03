arp l2-proxy enable (Bridge domain view)
========================================

arp l2-proxy enable (Bridge domain view)

Function
--------



The **arp l2-proxy enable** command enables Layer 2 proxy ARP.

The **undo arp l2-proxy enable** command disables Layer 2 proxy ARP.



By default, Layer 2 proxy ARP is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**arp l2-proxy enable**

**undo arp l2-proxy enable**


Parameters
----------

None

Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After receiving an ARP request packet, the device broadcasts the packet in its broadcast domain. If the device receives a large number of ARP request packets in a short period of time and broadcasts the packets, excessive ARP request packets are forwarded in the broadcast domain. As a result, the bandwidth is wasted, and traffic congestion may occur.To resolve this problem, run the **arp l2-proxy enable** command to enable Layer 2 proxy ARP on the device. After receiving an ARP request packet, the device checks whether the destination IP address in the packet matches an ARP entry. If a matching ARP entry is found, the device sends an ARP reply packet with the MAC address of the destination. If no matching ARP entry is found, the device discards the packet.



**Precautions**

Layer 2 proxy ARP and binding a VLAN to a BD are mutually exclusive. After a VLAN is configured as a VXLAN service access point, you are not advised to enable Layer 2 proxy ARP.Layer 2 proxy ARP cannot be configured in the following situations:

* A VLANIF interface has been configured in the VLAN where Layer 2 proxy ARP needs to be configured.
* Local proxy ARP, proxy ARP anyway, or routed proxy ARP has been configured on the VBDIF interface corresponding to the BD for which Layer 2 proxy ARP needs to be configured.


Example
-------

# Enable BD-based Layer 2 proxy ARP.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] arp l2-proxy enable

```