display bgp vpnv6 routing-table statistics(Attribute Filter)
============================================================

display bgp vpnv6 routing-table statistics(Attribute Filter)

Function
--------



The **display bgp vpnv6 routing-table statistics** command displays statistics about BGP VPNv6 routes and BGP4+ VPN routes based on specified multiple attribute filters.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **community-filter** { { *community-filter-num* | *community-filter-numEx* | *community-filter-name* } | { *community-filter-num* | *community-filter-name* } **whole-match** }

**display bgp vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **extcommunity-filter** { *basic-extcomm-flt-num* | *adv-extcomm-flt-num* | *extcommunity-filter-name* }

**display bgp vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **large-community-filter** *largeComFilName* [ **whole-match** ]

**display bgp instance** *bgpName* **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp instance** *bgpName* **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **community-filter** { { *community-filter-num* | *community-filter-numEx* | *community-filter-name* } | { *community-filter-num* | *community-filter-name* } **whole-match** }

**display bgp instance** *bgpName* **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **extcommunity-filter** { *basic-extcomm-flt-num* | *adv-extcomm-flt-num* | *extcommunity-filter-name* }

**display bgp instance** *bgpName* **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **large-community-filter** *largeComFilName* [ **whole-match** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays BGP VPNv6 routes and BGP4+ routes of VPN instances. | - |
| **vpn-instance** *vpn-instance-name* | Displays the BGP routing information of the specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **as-path-filter** *as-path-filter-num* | Specifies the number of an AS\_Path filter. | The value is an integer that ranges from 1 to 256. |
| **as-path-filter** *as-path-filter-name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. |
| **community-filter** *community-filter-name* | Specifies the name of a community filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |
| **community-filter** *community-filter-num* | Specifies the number of a basic community filter. | The value is an integer that ranges from 1 to 99. |
| **community-filter** *community-filter-numEx* | Specifies the number of an advanced community filter. | The value is an integer that ranges from 100 to 199. |
| **whole-match** | Matches the specified community attribute. | - |
| **whole-match** | Indicates that the Large-Community attribute is fully matched. | - |
| **extcommunity-filter** *basic-extcomm-flt-num* | Specifies the number of a basic extcommunity filter. | The value is an integer ranging from 1 to 199. |
| **extcommunity-filter** *adv-extcomm-flt-num* | Specifies the number of an advanced extcommunity filter. | The value is an integer ranging from 200 to 399. |
| **extcommunity-filter** *extcommunity-filter-name* | Specifies the name of the extended community filter. | The value is a string of 1 to 51 characters. |
| **large-community-filter** *largeComFilName* | Specifies the name of a Large-Community filter. | The value is a string of 1 to 51 case-sensitive characters. It cannot contain spaces. |
| **instance** *bgpName* | Displays BGP routes of a specified BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To query statistics about BGP VPNv6 routes and BGP4+ VPN routes based on specified multiple attribute filters, run this command. Multiple attribute filters can be specified in this command for query.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about BGP VPNv6 routes that match community filter 10.
```
<HUAWEI> display bgp vpnv6 all routing-table statistics community-filter 10
 
 Total number of routes from all PE: 2

 VPN-Instance vrf, Router ID 10.1.123.1:
 Total Number of Routes: 2

```

# Display statistics about BGP4+ private routes that match large community filter aaa.
```
<HUAWEI> display bgp vpnv6 vpn-instance vrf routing-table statistics large-community-filter aaa
 Total Number of Routes: 1

```

# Display statistics about BGP4+ private routes that match AS path filter pas.
```
<HUAWEI> display bgp vpnv6 vpn-instance vrf routing-table statistics as-path-filter pas
 Total Number of Routes: 3

```

**Table 1** Description of the **display bgp vpnv6 routing-table statistics(Attribute Filter)** command output
| Item | Description |
| --- | --- |
| Total number of routes from all PE | Number of VPNv6 routes. |
| Total Number of Routes | Total number of routes. |
| VPN-Instance | Name of a VPN instance. |
| Router ID | Router ID of the VPN instance. |