assign forward nvo3 bum ecmp hash enable
========================================

assign forward nvo3 bum ecmp hash enable

Function
--------



The **assign forward nvo3 bum ecmp hash enable** command enables underlay network-based load balancing of VXLAN broadcast, unknown unicast, and multicast (BUM) packets.



By default, VXLAN BUM packets cannot be load balanced based on an underlay network.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H and CE6881H-K.



Format
------

**assign forward nvo3 bum ecmp hash enable**

**undo assign forward nvo3 bum ecmp hash enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the underlay network of a VXLAN tunnel has multiple equal-cost next hops, only one next hop is selected to forward Broadcast&Unknown-unicast&Multicast (BUM) packets.You can run this command to enable underlay network-based load balancing for VXLAN BUM packets so that BUM packets can be load balanced among multiple next hops.

**Precautions**

* BUM traffic load balancing over VXLAN tunnels cannot be used together with IGMP snooping over VXLAN or IPv4 Layer 3 multicast over VXLAN. That is, this command cannot be used together with the **igmp snooping enable** command in the system view or the **igmp enable** command in the VBDIF interface view.
* This command cannot be used together with the **local-preference enhanced** command in the ECMP load balancing view.


Example
-------

# Enable underlay network-based load balancing for VXLAN BUM packets.
```
<HUAWEI> system-view
[~HUAWEI] assign forward nvo3 bum ecmp hash enable

```