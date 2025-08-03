routing-table rib-only (BGP-VPN instance IPv6 address family view)
==================================================================

routing-table rib-only (BGP-VPN instance IPv6 address family view)

Function
--------



The **routing-table rib-only** command prohibits BGP routes from being added to the IP routing table.

The **undo routing-table rib-only** command restores the default configuration.



By default, the preferred BGP routes are added to the IP routing table.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**routing-table rib-only** [ **route-policy** *route-policy-name* ]

**undo routing-table rib-only**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-policy** *route-policy-name* | Specifies the name of a routing policy. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a route reflector (RR) is used and preferred BGP routes do not need to be used during the forwarding, the **routing-table rib-only** command can be used to make BGP routes unable to be added to the IP routing table or the forwarding layer. This improves forwarding efficiency and the system capacity.When route-policy-name is specified in the command, the routes matching the policy are not added to the IP routing table, and the routes not matching the policy are added to the IP routing table.

**Precautions**

If the source of the invalid routes imported using the **import-rib** command matches the instance and address family in which the **routing-table rib-only** command is run, the import-rib and **routing-table rib-only** commands are mutually exclusive.


Example
-------

# Prohibit BGP routes from being advertised to the IP routing table.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv6-family unicast
[*HUAWEI-vpn-instance-vrf1-af-ipv6] route-distinguisher 333:3
[*HUAWEI-vpn-instance-vrf1-af-ipv6] vpn-target 333:3
[*HUAWEI-vpn-instance-vrf1-af-ipv6] quit
[*HUAWEI-vpn-instance-vrf1-af] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vrf1
[*HUAWEI-bgp-6-vrf1] routing-table rib-only

```