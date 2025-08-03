aggregate default-route (BGP-VPN instance IPv6 address family view)
===================================================================

aggregate default-route (BGP-VPN instance IPv6 address family view)

Function
--------



The **aggregate default-route** command enables a BGP device to summarize the routes that match a specified IPv6 prefix list into a summary default route.

The **undo aggregate default-route** command restores the default configuration.



By default, BGP cannot summarize the routes that match a specified IPv6 prefix list into a summary default route.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**aggregate default-route origin-ipv6-prefix** *ipv6-prefix-name* [ **attribute-policy** *attribute-policy-name* ]

**undo aggregate default-route**

**undo aggregate default-route origin-ipv6-prefix** *ipv6-prefix-name* [ **attribute-policy** *attribute-policy-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **attribute-policy** *attribute-policy-name* | Specifies the name of an attribute route-policy for the summary default route. | The value is a string ranging from 1 to 200. |
| **origin-ipv6-prefix** *ipv6-prefix-name* | Specifies the name of an IPv6 prefix list. | The value is a string of 1 to 169 characters and cannot contain spaces. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent traffic that does not match the IPv4 prefix filter from being imported to the local device, run this command to configure the local device to advertise default routes to the peer device based on the IPv4 prefix filter. This saves bandwidth resources. For details, see Configuration > IP Routing > BGP4+ Configuration > Configuring BGP4+ to Summarize Default Routes.

**Prerequisites**

An IPv6 prefix list has been configured using the **ip ipv6-prefix** command.

**Precautions**

The number of entries in the IPv6 prefix list specified in the aggregate default-route command cannot exceed 200.


Example
-------

# Enable a BGP device to summarize the routes that match an IPv6 prefix list into a summary default route.
```
<HUAWEI> system-view
[~HUAWEI] ip ipv6-prefix prefix-a deny 2001:db8:: 32 less-equal 128
[*HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv6-family
[*HUAWEI-vpn-instance-vrf1-af-ipv6] quit
[*HUAWEI-vpn-instance-vrf1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vrf1
[*HUAWEI-bgp-6-vrf1] aggregate default-route origin-ipv6-prefix prefix-a

```

# Enable a BGP device to summarize the routes that match an IPv4 prefix list into a summary default route and specify an attribute route-policy for the summary default route.
```
<HUAWEI> system-view
[~HUAWEI] ip ipv6-prefix prefix-a deny 2001:db8:: 32 less-equal 128
[*HUAWEI] route-policy policy1 permit node 10
[*HUAWEI-route-policy] if-match ipv6 address prefix-list prefix-a
[*HUAWEI-route-policy] apply cost 100
[*HUAWEI-route-policy] quit
[*HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] ipv6-family
[*HUAWEI-vpn-instance-vrf1-af-ipv6] quit
[*HUAWEI-vpn-instance-vrf1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vrf1
[*HUAWEI-bgp-6-vrf1] aggregate default-route origin-ipv6-prefix prefix-a attribute-policy policy1

```