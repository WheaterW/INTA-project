export route-policy evpn
========================

export route-policy evpn

Function
--------



The **export route-policy evpn** command associates the VPN instance IPv4/IPv6 address family of a VPN instance with an export routing policy to filter routes to be advertised to the EVPN.

The **undo export route-policy evpn** command disassociates the VPN instance IPv4/IPv6 address family of a VPN instance with an export routing policy.



By default, the VPN instance IPv4/IPv6 address family of a VPN instance is not associated with any export routing policy.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**export route-policy** *policy-name* **evpn**

**undo export route-policy** *policy-name* **evpn**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of a routing policy. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

VPN instance IPv4 address family view,VPN instance IPv6 address family view,VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, the VPN IPv4/IPv6 address family of a VPN instance adds all VPN targets in the export VPN target list to routes to be advertised to the EVPN. To control route export more precisely, run the **export route-policy evpn** command to associate the VPN IPv4/IPv6 address family with an export routing policy and set attributes for eligible routes.

**Prerequisites**

An RD has been configured for the VPN instance IPv4/IPv6 address family using the **route-distinguisher** command.

**Configuration Impact**

The current VPN instance address family can be associated with only one import route-policy. If this command is run more than once, the latest configuration overrides the previous one.The **export route-policy** command does not affect the export route-policy configured using the **export route-policy** command.

**Precautions**

If the specified routing policy does not exist, run the **route-policy** command to create the routing policy.


Example
-------

# Associate the VPN instance IPv4 address family of a VPN instance named vrf1 with an export routing policy named policy-2 to filter routes to be advertised to the EVPN.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy-2 permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv4-family
[*HUAWEI-vpn-instance-vrf1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vrf1-af-ipv4] export route-policy policy-2 evpn

```