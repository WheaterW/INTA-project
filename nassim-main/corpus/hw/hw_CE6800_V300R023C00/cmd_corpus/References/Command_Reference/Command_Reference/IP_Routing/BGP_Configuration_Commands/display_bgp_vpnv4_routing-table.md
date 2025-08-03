display bgp vpnv4 routing-table
===============================

display bgp vpnv4 routing-table

Function
--------



The **display bgp vpnv4 routing-table** command displays information about BGP VPNv4 routes and BGP VPN routes.




Format
------

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table**

**display bgp vpnv4** { **route-distinguisher** *route-distinguisher* | **all** | **vpn-instance** *vpn-instance-name* } **routing-table** *ipv4-address* [ *mask-length* | *mask* ]

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **statistics**

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **cidr**

**display bgp vpnv4** { **route-distinguisher** *route-distinguisher* | **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **cidr**

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **different-origin-as**

**display bgp vpnv4** { **route-distinguisher** *route-distinguisher* | **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **different-origin-as**

**display bgp instance** *instance-name* **vpnv4** { **route-distinguisher** *route-distinguisher* | **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **different-origin-as**

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community-filter** { *basic-community-filter-number* | *advanced-community-filter-number* }

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community-filter** *community-filter-name*

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community** [ *community-number* | *aa:nn* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] &<1-33>

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community** [ *community-number* | *aa:nn* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] &<1-33> **whole-match**

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **community-filter** { *basic-community-filter-number* | *advanced-community-filter-number* }

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **community-filter** *community-filter-name*

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **community** [ *community-number* | *aa:nn* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] &<1-33>

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **community** [ *community-number* | *aa:nn* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] &<1-33> **whole-match**

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **regular-expression** *as-regular-expression*

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **regular-expression** *as-regular-expression*

**display bgp vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** *ipv4-address* { *mask-length* | *mask* } **longer-prefixes**

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community-filter** *basic-community-filter-number* **whole-match**

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community-filter** *community-filter-name* **whole-match**

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **community-filter** *basic-community-filter-number* **whole-match**

**display bgp vpnv4 route-distinguisher** *route-distinguisher* **routing-table** **community-filter** *community-filter-name* **whole-match**

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table**

**display bgp instance** *instance-name* **vpnv4** { **route-distinguisher** *route-distinguisher* | **all** | **vpn-instance** *vpn-instance-name* } **routing-table** *ipv4-address* [ *mask-length* | *mask* ]

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **statistics**

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **cidr**

**display bgp instance** *instance-name* **vpnv4** { **route-distinguisher** *route-distinguisher* | **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **cidr**

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **different-origin-as**

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **statistics** **as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community-filter** { *basic-community-filter-number* | *advanced-community-filter-number* }

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community-filter** *community-filter-name*

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community** [ *community-number* | *aa:nn* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] &<1-33>

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community** [ *community-number* | *aa:nn* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] &<1-33> **whole-match**

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **community-filter** { *basic-community-filter-number* | *advanced-community-filter-number* }

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **community-filter** *community-filter-name*

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **community** [ *community-number* | *aa:nn* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] &<1-33>

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **community** [ *community-number* | *aa:nn* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] &<1-33> **whole-match**

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **statistics** **regular-expression** *as-regular-expression*

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **regular-expression** *as-regular-expression*

**display bgp instance** *instance-name* **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** *ipv4-address* { *mask-length* | *mask* } **longer-prefixes**

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community-filter** *basic-community-filter-number* **whole-match**

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community-filter** *community-filter-name* **whole-match**

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **community-filter** *basic-community-filter-number* **whole-match**

**display bgp instance** *instance-name* **vpnv4** **route-distinguisher** *route-distinguisher* **routing-table** **community-filter** *community-filter-name* **whole-match**

**display bgp vpnv4** { **route-distinguisher** *route-distinguisher* | **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **active**

**display bgp instance** *instance-name* **vpnv4** { **route-distinguisher** *route-distinguisher* | **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **active**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-distinguisher** *route-distinguisher* | Displays statistics about the BGP routes with a specified RD. | The value is a string of 3 to 21 case-sensitive characters, spaces not supported. |
| **all** | Displays statistics about all BGP VPNv4 routes. | - |
| **vpn-instance** *vpn-instance-name* | Displays the BGP routes of a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *ipv4-address* | Specify an IPv4 peer address. | Dotted decimal notation. |
| *mask-length* | Length of IP address mask. | The value is an integer ranging from 0 to 32. |
| *mask* | Specifies a mask. | The value is in dotted decimal notation. |
| **statistics** | Displays statistics about routes advertised to or received from a specified peer. | - |
| **cidr** | Displays CIDR information. | - |
| **different-origin-as** | Displays routes that have the same destination address but different source AS numbers. | - |
| **instance** *instance-name* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |
| **as-path-filter** *as-path-filter-num* | Displays the routes that match the AS\_Path filter of a specified number. | It is an integer ranging from 1 to 256. |
| *as-path-filter-name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. |
| **community-filter** *basic-community-filter-number* | Specifies the number of a basic community filter. | The value is an integer ranging from 1 to 99. |
| **community-filter** *community-filter-name* | Specifies the name of a community filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |
| **community-filter** *advanced-community-filter-number* | Specifies the number of an advanced community filter. | The value is an integer ranging from 100 to 199. |
| **community** *community-number* | Specifies a community number. | The value is an integer ranging from 0 to 4294967295. |
| **community** *aa:nn* | Specifies a community number. | The value is a string of 1 to 11 case-sensitive characters, spaces not supported. |
| **internet** | Allows the routes that match the community filter to be sent to all peers. | - |
| **no-advertise** | Displays the BGP routes carrying the No-Advertise community attribute. | - |
| **no-export** | Displays the BGP public network routes carrying the No-Export community attribute. | - |
| **no-export-subconfed** | Displays the BGP routes carrying the No-Export-Subconfed community attribute. | - |
| **whole-match** | Indicates exact matching. | - |
| **regular-expression** *as-regular-expression* | Displays the routes that match the regular expression. | The value is a string of 1 to 80 characters. |
| **longer-prefixes** | Matches any route whose prefix mask is longer than the specified length. | - |
| **active** | Displays the active routes learned from a specified peer. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can view only specific routing information by specifying different parameters.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about the VPNv4 routes with a specified RD in a BGP multi-instance.
```
<HUAWEI> display bgp instance aaa vpnv4 route-distinguisher 1:1 routing-table statistics best
 Route Distinguisher: 1:1
Total Number of Best Routes from All PE: 1
Total Number of Add-path Routes from All PE: 0
Total Number of Best-external Routes from All PE: 1
 VPN-Instance vrf1, Router ID 11.11.11.11:
Total Number of Best Routes: 1

```

# Display information about optimal VPNv4 routes.
```
<HUAWEI> display bgp vpnv4 all routing-table statistics best
 Total Number of Best Routes from All PE: 1
 Total Number of Add-path Routes from All PE: 0 
 Total Number of Best-external Routes from All PE: 1
 VPN-Instance vrf1, Router ID 11.11.11.11:
Total Number of Best Routes: 1
 VPN-Instance vrf2, Router ID 11.11.11.11:
Total Number of Best Routes: 1

```

# Display statistics about the VPNv4 routes with the specified RD.
```
<HUAWEI> display bgp vpnv4 route-distinguisher 100:1 routing-table statistics
 Route Distinguisher: 100:1
 Total Number of Routes: 1
 Total number of routes of IPv4-family for vpn-instance vrf1: 3

```

# Display statistics about dampened VPNv4 routes.
```
<HUAWEI> display bgp vpnv4 all routing-table statistics dampened
 Total Number of Routes: 2

```

# Display statistics about active VPNv4 routes.
```
<HUAWEI> display bgp vpnv4 all routing-table statistics active
 Total number of routes from all PE: 2
 VPN-Instance vrf1, router ID 1.1.1.1:
 Total Number of Prefix Advertised to RM : 2
 Total Number of Active Route : 2

```

**Table 1** Description of the **display bgp vpnv4 routing-table** command output
| Item | Description |
| --- | --- |
| Route Distinguisher | Route distinguisher (RD) of a route. |
| Total number of routes from all PE | Total number of VPNv4 routes. |
| Total number of routes of IPv4-family for vpn-instance vrf1 | Number of routes in the BGP-VPN instance IPv4 address family. |
| Total Number of Routes | Total number of VPNv4 routes with a specified RD. |
| Total Number of Best Routes from All PE | Number of optimal routes that are selected among the routes received from all PEs. |
| Total Number of Best-external Routes from All PE | Number of Best-External routes from all PEs. |
| Total Number of Add-path Routes from All PE | Number of Add-Path routes from all PEs. |
| Total Number of Best Routes | Number of optimal routes. |
| Total Number of Prefix Advertised to RM | Number of routes delivered to the RM module. |
| Total Number of Active Route | Number of active routes. |
| Prefix | Prefix of a BGP route. |