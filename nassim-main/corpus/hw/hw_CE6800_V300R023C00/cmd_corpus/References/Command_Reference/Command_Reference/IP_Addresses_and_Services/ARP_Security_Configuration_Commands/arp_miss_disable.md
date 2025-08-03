arp miss disable
================

arp miss disable

Function
--------



The **arp miss disable** command disables a VBDIF interface from sending ARP Miss messages.

The **undo arp miss disable** command enables a VBDIF interface to send ARP Miss messages.



By default, a VBDIF interface can send ARP Miss messages.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**arp miss disable**

**undo arp miss disable**


Parameters
----------

None

Views
-----

VBDIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When the device wants to communicate with another device in the same network segment, it queries ARP entries to direct packet forwarding. If the device fails to find the corresponding ARP entry from the forwarding plane, it sends an ARP Miss message to the CPU. The ARP Miss message will trigger the device to send an ARP broadcast packet to start ARP learning. In some cases, customers may want to limit the number of broadcast packets on the VXLAN network. You can then disable a VBDIF interface from sending ARP Miss messages to achieve this purpose.After a VBDIF interface is disabled from sending ARP Miss messages, the device cannot learn ARP entries from this VBDIF interface, so ARP entries must be manually configured on it.


Example
-------

# Disable a VBDIF interface from sending ARP Miss messages.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] interface vbdif 10
[*HUAWEI-Vbdif10] arp miss disable

```