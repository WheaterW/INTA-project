display bgp vpnv4 routing-table statistics(Attribute Filter)
============================================================

display bgp vpnv4 routing-table statistics(Attribute Filter)

Function
--------



The **display bgp vpnv4 routing-table statistics** command displays statistics about BGP VPNv4 routes and BGP VPN routes based on specified multiple attribute filters.




Format
------

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **community-filter** { { *community-filter-num* | *community-filter-numEx* | *community-filter-name* } | { *community-filter-num* | *community-filter-name* } **whole-match** }

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **large-community-filter** *largeComFilName* [ **whole-match** ]

**display bgp instance** *bgpName* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp instance** *bgpName* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **community-filter** { { *community-filter-num* | *community-filter-numEx* | *community-filter-name* } | { *community-filter-num* | *community-filter-name* } **whole-match** }

**display bgp instance** *bgpName* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **large-community-filter** *largeComFilName* [ **whole-match** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays BGP VPNv4 routes and BGP routes of VPN instances. | - |
| **vpn-instance** *vpn-instance-name* | Displays about the BGP routes of a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **statistics** | Displays BGP route statistics. | - |
| **as-path-filter** *as-path-filter-num* | Specifies the number of an AS\_Path filter. | The value is an integer that ranges from 1 to 256. |
| **as-path-filter** *as-path-filter-name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. |
| **community-filter** *community-filter-name* | Specifies the name of a community filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |
| **community-filter** *community-filter-num* | Specifies the number of a basic community filter. | The value is an integer that ranges from 1 to 99. |
| **community-filter** *community-filter-numEx* | Specifies the number of an advanced community filter. | The value is an integer that ranges from 100 to 199. |
| **whole-match** | Matches the specified community attribute. | - |
| **whole-match** | Indicates that the Large-Community attribute is fully matched. | - |
| **large-community-filter** *largeComFilName* | Specifies the name of a Large community filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. |
| **instance** *bgpName* | Specifies a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To query statistics about BGP VPNv4 routes and BGP VPN routes based on specified multiple attribute filters, run this command. Multiple attribute filters can be specified in this command for query.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about BGP multi-instance VPNv4 routes that match AS path filter pas.
```
<HUAWEI> display bgp instance a vpnv4 all routing-table statistics as-path-filter pas
 
 Total number of routes from all PE: 3

 VPN-Instance vpna, Router ID 10.3.123.1:
 Total Number of Routes: 3

```

# Display statistics about BGP private routes that match large community filter aaa.
```
<HUAWEI> display bgp vpnv4 vpn-instance vrf routing-table statistics large-community-filter aaa

 VPN-Instance vrf, Router ID 10.1.123.1:
 Total Number of Routes: 1

```

# Display statistics about BGP VPNv4 routes that exactly match large community filter aaa.
```
<HUAWEI> display bgp vpnv4 all routing-table statistics large-community-filter aaa whole-match
 
 Total number of routes from all PE: 1

 VPN-Instance vrf, Router ID 10.1.123.1:
 Total Number of Routes: 1

```

# Display statistics about BGP VPNv4 routes that match community filter 10.
```
<HUAWEI> display bgp vpnv4 all routing-table statistics community-filter 10
 
 Total number of routes from all PE: 2

 VPN-Instance vrf, Router ID 10.1.123.1:
 Total Number of Routes: 2

```

**Table 1** Description of the **display bgp vpnv4 routing-table statistics(Attribute Filter)** command output
| Item | Description |
| --- | --- |
| Total number of routes from all PE | Number of VPNv4 routes. |
| Total Number of Routes | Total number of routes. |
| VPN-Instance | Name of a VPN instance. |
| Router ID | Router ID of the VPN instance. |