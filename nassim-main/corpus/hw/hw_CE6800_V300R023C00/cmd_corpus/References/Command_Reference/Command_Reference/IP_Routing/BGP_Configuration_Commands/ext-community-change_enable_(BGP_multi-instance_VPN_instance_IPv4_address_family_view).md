ext-community-change enable (BGP multi-instance VPN instance IPv4 address family view)
======================================================================================

ext-community-change enable (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **ext-community-change enable** command enables a device to change the VPN target, SoO, and link bandwidth extended community attributes based on a route-policy.

The **undo ext-community-change enable** command disables a device from changing VPN target, SoO, and link bandwidth extended community attributes based on a route-policy.



By default, the VPN target, SoO, and link bandwidth extended community attributes cannot be modified using a route-policy.


Format
------

**ext-community-change enable**

**undo ext-community-change enable**


Parameters
----------

None

Views
-----

BGP multi-instance VPN instance IPv4 address family view


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
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vrf1
[*HUAWEI-bgp-instance-a-vrf1] ext-community-change enable

```