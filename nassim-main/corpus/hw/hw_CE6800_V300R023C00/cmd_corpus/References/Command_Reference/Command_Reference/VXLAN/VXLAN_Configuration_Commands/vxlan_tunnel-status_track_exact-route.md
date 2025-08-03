vxlan tunnel-status track exact-route
=====================================

vxlan tunnel-status track exact-route

Function
--------



The **vxlan tunnel-status track exact-route** command enables subscription to the status of the exact route to a VXLAN tunnel destination.

The **undo vxlan tunnel-status track exact-route** command disables subscription to the status of the exact route to a VXLAN tunnel destination.



By default, subscription to the status of the exact route to a VXLAN tunnel destination is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vxlan tunnel-status track exact-route**

**undo vxlan tunnel-status track exact-route**


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

By default, if the exact route to the source IP address of a VXLAN tunnel is reachable and the route to the network segment where the destination IP address resides is reachable, the VXLAN tunnel is considered Up. In actual networking, however, there may be multiple destination addresses on the same network segment. If one destination address is reachable, the network segment is reachable. If an IP address on the network segment is unreachable, the tunnel status is incorrectly reported and network problems cannot be detected in a timely manner. In this case, you can run the **vxlan tunnel-status track exact-route** command to enable subscription to the status of the exact route to the VXLAN tunnel destination. In this case, the VXLAN tunnel is Up only when the 32-bit or 128-bit host IP address of the destination VTEP is reachable. Otherwise, the VXLAN tunnel is Down.You can run the **display vxlan tunnel** command to view the VXLAN tunnel status.


Example
-------

# Enable subscription to the status of the exact route to a VXLAN tunnel destination.
```
<HUAWEI> system-view
[~HUAWEI] vxlan tunnel-status track exact-route

```