unknown-multicast discard
=========================

unknown-multicast discard

Function
--------



The **unknown-multicast discard** command disables interfaces in a VLAN from forwarding unknown multicast packets.

The **undo unknown-multicast discard** command restores the default configuration.



By default, interfaces in a VLAN forward unknown multicast, and unknown unicast packets.


Format
------

**unknown-multicast discard**

**undo unknown-multicast discard**


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



When interfaces in a VLAN receive unknown multicast packets, the interfaces broadcast these packets in the VLAN. If the interfaces broadcast a large number of attack packets, data forwarding and security are threatened.This command is used to disable interfaces in a VLAN from forwarding unknown multicast packets.



**Precautions**

When a VLANIF interface functions as a Layer 3 multicast outbound interface and the function of discarding unknown multicast packets is configured in the VLAN view:

* If IGMP snooping is not configured in a VLAN, IPv4 Layer 3 multicast protocol packets are discarded, affecting IPv4 Layer 3 multicast services.
* If MLD snooping is not configured in a VLAN, IPv6 Layer 3 multicast protocol packets are discarded, affecting IPv6 Layer 3 multicast services.


Example
-------

# Configure interfaces in a VLAN to discard unknown multicast packets.
```
<HUAWEI> system-view
[~HUAWEI] vlan 10
[*HUAWEI-vlan10] unknown-multicast discard

```