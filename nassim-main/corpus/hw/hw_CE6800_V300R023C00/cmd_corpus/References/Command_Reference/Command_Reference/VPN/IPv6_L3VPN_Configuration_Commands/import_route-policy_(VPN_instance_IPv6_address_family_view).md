import route-policy (VPN instance IPv6 address family view)
===========================================================

import route-policy (VPN instance IPv6 address family view)

Function
--------



The **import route-policy** command associates an import route-policy with a VPN instance IPv6 address family.

The **undo import route-policy** command dissociates an import route-policy from a VPN instance IPv6 address family.



By default, no import route-policy is associated with a VPN instance IPv6 address family.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**import route-policy** *policy-name*

**undo import route-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of an import route-policy to be associated with a VPN instance IPv6 address family. | The value is a string of 1 to 200 case-sensitive characters. |



Views
-----

VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If no import route-policy is configured, the routes to be imported into the VPN instance IPv6 address family can be filtered only based on the export VPN targets of the routes and the import VPN targets of the VPN instance. To control the import of the routes into the VPN instance IPv6 address family more precisely, use an import route-policy. An import route-policy can filter the routes imported by the VPN instance IPv6 address family and set the attributes for routes that pass the filtering. Routes are filtered based on their export VPN targets and the import VPN targets of the VPN instance and then based on the import route-policy.Compared with the **import route-policy** command, the peer route-policy import or peer filter-policy import command configured in the BGP-VPN instance IPv6 address family view filters the routes received by the VPN instance IPv6 address family from a CE (a BGP peer).

**Prerequisites**

The **ipv6-family** command has been run in the VPN instance view to enable the IPv6 address family, and the **route-distinguisher** command has been run in the VPN instance view to set an RD for the VPN instance IPv6 address family.

**Configuration Impact**

Only one import route-policy can be associated with a VPN instance IPv6 address family. If the **import route-policy** command is run more than once, the latest configuration overrides the previous one.

**Follow-up Procedure**

If the import route-policy to be associated with a VPN instance IPv6 address family does not exist, configure the route-policy.


Example
-------

# Associate an import route-policy named poly-1 with a VPN instance IPv6 address family.
```
<HUAWEI> system-view
[~HUAWEI] route-policy poly-1 permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv6-family
[*HUAWEI-vpn-instance-vrf1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vrf1-af-ipv6] import route-policy poly-1

```