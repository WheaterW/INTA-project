ext-community-change enable (BGP-VPN instance IPv6 address family view)
=======================================================================

ext-community-change enable (BGP-VPN instance IPv6 address family view)

Function
--------



The **ext-community-change enable** command enables a device to change the VPN target, SoO, and link bandwidth extended community attributes based on a route-policy.

The **undo ext-community-change enable** command disables a device from changing VPN target, SoO, and link bandwidth extended community attributes based on a route-policy.



By default, the VPN target, SoO, and link bandwidth extended community attributes cannot be modified using a route-policy.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ext-community-change enable**

**undo ext-community-change enable**


Parameters
----------

None

Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, BGP is not allowed to use an import policy to change the VPN target and SoO extended community attributes and the link bandwidth attribute of the routes received from a specified peer or peer group, or use an export policy to change the VPN target and SoO extended community attributes and the link bandwidth attribute of the routes to be advertised to a specified peer or peer group. After the **ext-community-change enable** command is run, the VPN target and SoO extended community attributes and the link bandwidth attribute of the routes received from a specified peer or peer group can be modified based on an import policy, and the changed extended community attributes can be advertised to a specified peer or peer group based on an export policy. In this manner, the modified VPN target and SoO extended community attributes and the link bandwidth attribute of preferred routes can be advertised to the peer or peer group.

**Precautions**

* The **ext-community-change enable** command must be used together with the peer route-policy import command so that the extended community attributes received from a peer or peer group can be modified based on an import policy.
* The **ext-community-change enable** command must be used together with the peer advertise-ext-community and peer route-policy export commands so that the changed extended community attributes can be advertised to a peer or peer group based on an export policy.
* The **ext-community-change enable** command allows a device to change only VPN targets and SoO extended community attributes based on a route-policy.

Example
-------

# Enable the device to change extended community attributes based on a route-policy.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] ext-community-change enable

```