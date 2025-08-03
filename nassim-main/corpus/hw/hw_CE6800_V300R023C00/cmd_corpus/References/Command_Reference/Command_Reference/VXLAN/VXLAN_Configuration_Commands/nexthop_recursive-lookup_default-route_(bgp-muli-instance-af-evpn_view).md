nexthop recursive-lookup default-route (bgp-muli-instance-af-evpn view)
=======================================================================

nexthop recursive-lookup default-route (bgp-muli-instance-af-evpn view)

Function
--------

By default, the function to send packets over a default route when the recursive next-hop IP address is unavailable is not enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**nexthop recursive-lookup default-route**

**undo nexthop recursive-lookup default-route**


Parameters
----------

None

Views
-----

bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In an EVPN over VXLAN scenario, a PE device at one end may fail to establish a VXLAN tunnel because the next hop of the Layer 3 prefix route is unreachable due to incorrect configurations or faults. As a result, services are interrupted. To prevent this problem, run the **nexthop recursive-lookup default-route** command on the PE and configure the remote PE to send a default route to the local PE. When the next hop of a specific route on the local PE is unreachable, the local PE can iterate the default route to establish a VXLAN tunnel for forwarding, ensuring normal service running.


Example
-------

# Enable the function to send packets over a default route when the recursive next-hop IP address is unavailable.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] l2vpn-family evpn
[*HUAWEI-bgp-instance-a-af-evpn] nexthop recursive-lookup default-route

```