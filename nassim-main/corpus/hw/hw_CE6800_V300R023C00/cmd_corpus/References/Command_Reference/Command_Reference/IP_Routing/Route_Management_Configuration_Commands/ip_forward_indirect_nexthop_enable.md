ip forward indirect nexthop enable
==================================

ip forward indirect nexthop enable

Function
--------



The **ip forward indirect nexthop enable** command enables indirect next hop for BGP remote peers.

The **undo ip forward indirect nexthop enable** command disables indirect next hop for remote BGP peers.



By default, indirect next hop is disabled for remote BGP peers.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ip forward indirect nexthop enable**

**undo ip forward indirect nexthop enable**


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

When an IGP route changes, the BGP routes that depend on the IGP route need to be recursed and delivered separately. When a public network tunnel changes, all VPN routes that are recursed to the tunnel need to be traversed, and then each related VPN forwarding table needs to be updated through the delivery process of the routing table and FIB table. As a result, the route convergence performance is low. After indirect next hop is enabled for remote BGP peers, the direct relationship between route prefixes and next hop forwarding information changes to the indirect relationship. Next hop information can be refreshed separately, without the need to refresh a large number of prefixes one by one. This speeds up route convergence. The **ip forward indirect nexthop enable** command takes effect for BGP and BGP4+ routes.


Example
-------

# Enable indirect next hop for remote BGP peers.
```
<HUAWEI> system-view
[~HUAWEI] ip forward indirect nexthop enable

```