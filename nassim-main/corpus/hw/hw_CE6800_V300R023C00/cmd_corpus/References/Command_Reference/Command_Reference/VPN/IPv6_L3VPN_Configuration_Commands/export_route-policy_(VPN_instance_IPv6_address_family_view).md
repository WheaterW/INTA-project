export route-policy (VPN instance IPv6 address family view)
===========================================================

export route-policy (VPN instance IPv6 address family view)

Function
--------



The **export route-policy** command associates an export route-policy with a VPN instance IPv6 address family.

The **undo export route-policy** command dissociates an export route-policy from a VPN instance IPv6 address family.



By default, no export route-policy is associated with a VPN instance IPv6 address family.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**export route-policy** *policy-name* [ **add-ert-first** ]

**undo export route-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of an export route-policy to be associated with a VPN instance IPv6 address family. | The value is a string of 1 to 200 case-sensitive characters. |
| **add-ert-first** | Adds ERTs to VPN routes before these routes are matched against an export routing policy. | - |



Views
-----

VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a scenario in which the routes of a VPN instance IPv6 address family need to be imported into a public network VPNv6 routing table, if the routing information to be imported into the VPNv6 routing table needs to be specified or attributes need to be set for the routes imported into the VPNv6 routing table, an export route-policy must be applied to the VPNv6 instance IPv6 address family.Compared with the **export route-policy** command, the peer route-policy export or peer filter-policy export command configured in the BGP-VPN instance IPv6 address family view is used to filter the routes advertised by the VPN instance IPv6 address family to the CE (a BGP peer).By default, ERTs are added to VPN routes before these routes are matched against an export routing policy. If the export routing policy contains RT-related filtering rules, these rules cannot apply to these routes. If you want to apply the RT-related filtering rules defined in an export routing policy to VPN routes, run the add-ert-first command to configure the system to add ERTs to VPN routes before matching these routes against the export routing policy.In local route leaking scenarios, you can run the **export route-policy** command to filter out locally leaked routes and set the attributes of these routes. Locally leaked routes include both locally imported routes and routes learned from VPN peers.

**Prerequisites**

The **ipv6-family** command has been run in the VPN instance view to enable the IPv6 address family, and the **route-distinguisher** command has been run in the VPN instance view to set an RD for the VPN instance IPv6 address family.

**Configuration Impact**

Only one export route-policy can be associated with a VPN instance IPv6 address family. If the **export route-policy** command is run more than once, the latest configuration overrides the previous one.

**Follow-up Procedure**

If the export route-policy to be associated with a VPN instance IPv6 address family does not exist, configure the route-policy.


Example
-------

# Associate an export route-policy named poly-1 with a VPN instance IPv6 address family.
```
<HUAWEI> system-view
[~HUAWEI] route-policy poly-1 permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv6-family
[*HUAWEI-vpn-instance-vrf1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vrf1-af-ipv6] export route-policy poly-1

```