peer ipv6-prefix export (BGP-VPN instance IPv6 address family view) (group)
===========================================================================

peer ipv6-prefix export (BGP-VPN instance IPv6 address family view) (group)

Function
--------



The **peer ipv6-prefix export** command configures a policy based on an IPv6 prefix list for filtering BGP routes to be advertised to a specified peer group.

The **undo peer ipv6-prefix export** command cancels this configuration.



By default, no route filtering policy based on an IP address prefix list is configured for a peer group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **ipv6-prefix** *ipv6-prefix-name* **export**

**undo peer** *group-name* **ipv6-prefix** [ *ipv6-prefix-name* ] **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **ipv6-prefix** *ipv6-prefix-name* | Indicates the filtering policy that is based on the IPv6 prefix list of the peer group. | The name is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **export** | Applies a route-filter to the routes to be advertised to a specified peer group. | - |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **peer ipv6-prefix export** command can be used to configure a route filtering policy that is based on an IPv6 prefix list to filter routes to be advertised, implementing route control.

**Prerequisites**

If the **peer ipv6-prefix** command specifies an IPv6 prefix list that does not exist for a peer group, use the **ip ipv6-prefix** command to create an IPv6 prefix list.

**Configuration Impact**

If an IPv6 prefix list is specified for a peer group, all the members of the peer group inherit the configuration.After an IPv6 prefix list is specified for a peer group, the peers in the peer group filter the routes to be advertised to other peers based on the IPv6 prefix list. Only the routes that pass the filtering of the IPv6 prefix list can be advertised.

**Precautions**

The **peer ipv6-prefix export** command is mutually exclusive with the **peer route-filter export** commands.


Example
-------

# Configure a route filtering policy based on an IPv6 prefix list.
```
<HUAWEI> system-view
[~HUAWEI] ip ipv6-prefix list1 permit 2001:DB8:1::1 8 greater-equal 17 less-equal 18
[*HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpn1
[*HUAWEI-bgp-6-vpn1] group test external
[*HUAWEI-bgp-6-vpn1] peer test as-number 200
[*HUAWEI-bgp-6-vpn1] peer test ipv6-prefix list1 export

```