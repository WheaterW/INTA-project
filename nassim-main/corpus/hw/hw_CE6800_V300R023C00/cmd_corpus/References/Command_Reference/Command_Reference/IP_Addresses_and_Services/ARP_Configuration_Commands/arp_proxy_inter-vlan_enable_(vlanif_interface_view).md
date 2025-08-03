arp proxy inter-vlan enable (vlanif interface view)
===================================================

arp proxy inter-vlan enable (vlanif interface view)

Function
--------



The **arp proxy inter-vlan enable** command enables inter-VLAN proxy ARP.

The **undo arp proxy inter-vlan enable** command disables inter-VLAN proxy ARP.



By default, inter-VLAN proxy ARP is disabled.


Format
------

**arp proxy inter-vlan enable**

**undo arp proxy inter-vlan enable**


Parameters
----------

None

Views
-----

VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By using VLANs, you can divide a network into different subnets, therefore dividing large broadcast domains into several small ones. This implements user isolation between VLANs, effectively limiting the scope of broadcast packets and improving network security. To implement Layer 2 communication between different VLANs, you must enable inter-VLAN proxy ARP on the interface.




Example
-------

# Enable inter-VLAN proxy ARP on a VLANIF interface.
```
<HUAWEI> system-view
[~HUAWEI] vlan 20
[*HUAWEI-vlan20] quit
[*HUAWEI] interface vlanif 20
[*HUAWEI-Vlanif20] arp proxy inter-vlan enable

```