display bgp vpnv6 routing-table
===============================

display bgp vpnv6 routing-table

Function
--------



The **display bgp vpnv6 routing-table** command displays BGP VPNv6 routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community-filter** { *basic-community-filter-number* | *advanced-community-filter-number* }

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community-filter** *community-filter-name*

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table** **community-filter** { *basic-community-filter-number* | *advanced-community-filter-number* }

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table** **community-filter** *community-filter-name*

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community** [ *community-number* | *aa:nn* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** | **g-shut** ] &<1-33>

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community** [ *community-number* | *aa:nn* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** | **g-shut** ] &<1-33> **whole-match**

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table** **community** [ *community-number* | *aa:nn* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** | **g-shut** ] &<1-33>

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table** **community** [ *community-number* | *aa:nn* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** | **g-shut** ] &<1-33> **whole-match**

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table** **as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table** **regular-expression** *as-regular-expression*

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **regular-expression** *as-regular-expression*

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **statistics**

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table**

**display bgp** [ **instance** *bgpName* ] **vpnv6** { **route-distinguisher** *route-distinguisher* | **all** | **vpn-instance** *vpn-instance-name* } **routing-table** *ipv6-address* [ *prefix-length* ]

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table** **different-origin-as**

**display bgp vpnv6** { **route-distinguisher** *route-distinguisher* | **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **different-origin-as**

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table** **community-filter** *basic-community-filter-number* **whole-match**

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table** **community-filter** *community-filter-name* **whole-match**

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community-filter** *basic-community-filter-number* **whole-match**

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **community-filter** *community-filter-name* **whole-match**

**display bgp vpnv6** { **route-distinguisher** *route-distinguisher* | **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **best**

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table** **extcommunity** [ { **rt** | **soo** } *strExtCommunity* ] &<1-33>

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table** **extcommunity** [ { **rt** | **soo** } *strExtCommunity* ] &<1-33> **match-any**

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **extcommunity** [ { **rt** | **soo** } *strExtCommunity* ] &<1-33>

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **extcommunity** [ { **rt** | **soo** } *strExtCommunity* ] &<1-33> **match-any**

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table** **extcommunity-filter** { *basic-extcomm-filter-number* | *advanced-extcomm-filter-number* }

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **extcommunity-filter** { *basic-extcomm-filter-number* | *advanced-extcomm-filter-number* }

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table** **extcommunity-filter** *extcomm-filter-name*

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **extcommunity-filter** *extcomm-filter-name*

**display bgp** [ **instance** *bgpName* ] **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** *ipv6-address* *prefix-length* **longer-prefixes**

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **large-community** [ *aa:bb:cc* ] &<1-33>

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **large-community** [ *aa:bb:cc* ] &<1-33> **whole-match**

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table** **large-community** [ *aa:bb:cc* ] &<1-33>

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table** **large-community** [ *aa:bb:cc* ] &<1-33> **whole-match**

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table** **large-community-filter** *large-community-filter-name*

**display bgp** [ **instance** *bgpName* ] **vpnv6** **route-distinguisher** *route-distinguisher* **routing-table** **large-community-filter** *large-community-filter-name* **whole-match**

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **large-community-filter** *large-community-filter-name*

**display bgp vpnv6 route-distinguisher** *route-distinguisher* **routing-table** **statistics** **large-community-filter** *large-community-filter-name* **whole-match**

**display bgp vpnv6** { **route-distinguisher** *route-distinguisher* | **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **active**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-distinguisher** *route-distinguisher* | Specifies an RD of a remote route. | The value is in the format of a:b:c. The values of a, b, and c are integers ranging from 0 to 4294967295. |
| **routing-table** | Displays the BGP routing table. | - |
| **statistics** | Displays statistics of routes. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **community-filter** *basic-community-filter-number* | Specifies the number of a basic community filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |
| **community-filter** *community-filter-name* | Specifies the name of a community filter. | The value is an integer ranging from 100 to 199. |
| **community-filter** *advanced-community-filter-number* | Specifies the number of an advanced community filter. | The value is an integer ranging from 1 to 199. |
| **vpnv6** | Indicates the VPNv6 address family. | - |
| **instance** *bgpName* | Specifies the name of a BGP multi-instance. | The value is an integer ranging from 200 to 399. |
| **community** *community-number* | Specifies a community number. | The value is an integer that ranges from 0 to 4294967295. |
| **community** *aa:nn* | Specifies a community number. | aa and nn are integers, each ranging from 0 to 65535. |
| **internet** | Indicates the Internet (well-known) community attribute. | - |
| **no-advertise** | Indicates a community that prevents routes from being advertised to any peer. | - |
| **no-export** | Indicates a community that prevents routes from being advertised outside an AS. | - |
| **no-export-subconfed** | Indicates a community that prevents routes from being advertised outside a sub-AS. | - |
| **g-shut** | Display routes with the Grateful-Shutdown community attribute. | - |
| **whole-match** | Indicates exact match with the specified community. | The value is a string of 1 to 80 characters. |
| **as-path-filter** *as-path-filter-num* | Specifies an AS\_Path filter index. | The value is a string of 1 to 51 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |
| **as-path-filter** *as-path-filter-name* | Specifies an AS\_Path filter name (a string of 1 to 51 characters, which cannot contain only digits.). | The value is an integer ranging from 1 to 99. |
| **regular-expression** *as-regular-expression* | Displays the routes that match the regular expression. | The value is a string of 1 to 80 characters. |
| **all** | Displays all information on VPNv6 and IPv6 VPN instances. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name cannot be \_public\_. If the string is enclosed in double quotation marks (" "), the string can contain spaces.. |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name cannot be \_public\_. If the string is enclosed in double quotation marks (" "), the string can contain spaces.. |
| *ipv6-address* | Specifies an IPv6 network address. | The value is an integer ranging from 0 to 4294967295. |
| *prefix-length* | Specifies an IP network mask length. | It is an integer ranging from 0 to 128. |
| **different-origin-as** | Displays the routes with the same destination address and mask but different origin AS numbers. | The value is an integer ranging from 1 to 256. |
| **best** | Displays statistics about best, Add-path, and best-external routes. | - |
| **extcommunity** | Displays routes matching a specified ext-community. | - |
| **rt** | Specifies a route target extended community. | - |
| **soo** | Specifies the SoO extended community attribute. | - |
| *strExtCommunity* | Specifies the excommunity value. | The attribute value can be expressed in one of the following formats:   * 2-byte AS number:4-byte user-defined number, for example, 1:3. The AS number is an integer ranging from 0 to 65535, and the user-defined number is an integer ranging from 0 to 4294967295. The AS number and user-defined number cannot both be set to 0. That is, the SoO must not be 0:0. * IPv4 address:2-byte user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number is an integer ranging from 0 to 65535. * 4-byte AS number in integer format:2-byte user-defined number, for example, 65537:3. An AS number ranges from 65536 to 4294967295, and a user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535. A user-defined number also ranges from 0 to 65535. The AS number and user-defined number must not be both 0s. That is, the SoO must not be 0.0:0. |
| **match-any** | Matches any specified extended communities. | - |
| **extcommunity-filter** *extcomm-filter-name* | Specifies the name of an extcommunity filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |
| **extcommunity-filter** *basic-extcomm-filter-number* | Specifies the number of an extcommunity filter. | The value is a string of 1 to 31 case-sensitive characters. If spaces are used, the string must be enclosed in double quotation marks (" "). |
| **extcommunity-filter** *advanced-extcomm-filter-number* | Specifies the number of an advanced extcommunity filter. | The value is an integer ranging from 200 to 399. |
| **longer-prefixes** | Allows match against longer masks. | - |
| **large-community** *aa:bb:cc* | Specifies a value of the Large-Community attribute. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |
| **large-community-filter** *large-community-filter-name* | Specifies a Large-Community list name. | The value is a string of 1 to 51 case-sensitive characters. It cannot contain spaces. |
| **active** | Displays active routes. | - |



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


# Display statistics about the Best, Add-Path, and Best-External VPNv6 routes.
```
<HUAWEI> display bgp vpnv6 all routing-table statistics best
 Total Number of Best Routes from All PE: 1
 Total Number of Add-path Routes from All PE: 0 
 Total Number of Best-external Routes from All PE: 1
 VPN-Instance vrf1, Router ID 10.10.1.1:
Total Number of Best Routes: 1
 VPN-Instance vrf2, Router ID 10.10.1.1:
Total Number of Best Routes: 1

```

# Display the Ext-Community information contained in a VPNv6 route with a specified prefix.
```
<HUAWEI> display bgp vpnv6 all routing-table 2001:DB8:2:3:: ext-community
Routes of vpn-instance vrf2:
 BGP routing table entry information of 2001:DB8:2:3::/64:
 From: 2001:DB8:42:4::7:7

```

# Display statistics about active VPNv6 routes.
```
<HUAWEI> display bgp vpnv6 all routing-table statistics active
 Total number of routes from all PE: 2
 VPN-Instance vrf1, router ID 10.10.1.1:
 Total Number of Prefix Advertised to RM : 2
 Total Number of Active Route : 2

```

**Table 1** Description of the **display bgp vpnv6 routing-table** command output
| Item | Description |
| --- | --- |
| Total number of routes from all PE | Number of routes received from all PEs in the routing table. |
| Total Number of Best Routes from All PE | Number of Best routes. |
| Total Number of Add-path Routes from All PE | Number of Add-Path routes. |
| Total Number of Best-external Routes from All PE | Number of Best-external routes. |
| Total Number of Best Routes | Number of optimal routes. |
| Total Number of Prefix Advertised to RM | Number of routes delivered to the RM module. |
| Total Number of Active Route | Number of active routes. |
| From | Source peer that sent the route. |
| Pre | Preference of a route. |