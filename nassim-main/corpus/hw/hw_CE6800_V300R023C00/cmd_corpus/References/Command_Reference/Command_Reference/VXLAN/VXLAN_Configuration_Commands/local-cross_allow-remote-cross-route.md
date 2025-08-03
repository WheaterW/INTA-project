local-cross allow-remote-cross-route
====================================

local-cross allow-remote-cross-route

Function
--------



The **local-cross allow-remote-cross-route** command enables local EVPN route leaking for remotely leaked routes.

The **undo local-cross allow-remote-cross-route** command disables local EVPN route leaking for remotely leaked routes.



By default, local EVPN route leaking is disabled for remotely leaked routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**local-cross allow-remote-cross-route**

**undo local-cross allow-remote-cross-route**


Parameters
----------

None

Views
-----

BGP-VPN instance IPv4 address family view,BGP-VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, remote EVPN routes received from the remote end can only be remotely leaked into a VPN instance. The routes of a VPN instance cannot be locally leaked into other VPN instances. To solve the problem of mutual access between different VPN instances, run the **local-cross allow-remote-cross-route** command to enable local leaking of remote EVPN routes. Then, the remote routes received by EVPN can be sent to a VPN instance and then locally leaked into other VPN instances.


Example
-------

# Enable the local EVPN route leaking function for remotely leaked routes.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] vpn-target 100:1 both evpn
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] local-cross export evpn-rt-match
[*HUAWEI-bgp-vpn1] local-cross allow-remote-cross-route

```