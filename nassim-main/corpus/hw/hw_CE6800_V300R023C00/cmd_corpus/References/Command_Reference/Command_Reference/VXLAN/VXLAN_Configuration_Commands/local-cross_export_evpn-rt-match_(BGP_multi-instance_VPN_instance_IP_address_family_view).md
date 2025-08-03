local-cross export evpn-rt-match (BGP multi-instance VPN instance IP address family view)
=========================================================================================

local-cross export evpn-rt-match (BGP multi-instance VPN instance IP address family view)

Function
--------



The **local-cross export evpn-rt-match** command enables local EVPN route leaking.

The **undo local-cross export evpn-rt-match** command disables local EVPN route leaking.



By default, the local EVPN route leaking function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**local-cross export evpn-rt-match**

**undo local-cross export evpn-rt-match**


Parameters
----------

None

Views
-----

BGP multi-instance VPN instance IPv4 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, the locally imported routes and VPN peer routes of a VPN instance cannot be locally leaked into other VPN instances through EVPN. To resolve this problem, run the **local-cross export evpn-rt-match** command to enable local EVPN route leaking. After the command is run, the locally imported routes and VPN peer routes of a VPN instance can be leaked into other VPN instances.


Example
-------

# Enable the local EVPN route leaking function.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] vpn-target 100:1 both evpn
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100 instance test
[*HUAWEI-bgp-instance-test] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-instance-test-vpn1] local-cross export evpn-rt-match

```