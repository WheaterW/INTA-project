display bgp instance vpnv6 routing-table statistics
===================================================

display bgp instance vpnv6 routing-table statistics

Function
--------



The **display bgp instance vpnv6 routing-table statistics** command displays statistics about BGP multi-instance VPNv6 routes that are filtered based on specified attributes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp instance** *bgpName* **vpnv6** **route-distinguisher** *strRd* **routing-table** **statistics** **community-filter** { *community-filter-num* | *community-filter-numEx* | *community-filter-name* }

**display bgp instance** *bgpName* **vpnv6** **route-distinguisher** *strRd* **routing-table** **statistics** **community-filter** { *community-filter-num* | *community-filter-name* } **whole-match**

**display bgp instance** *bgpName* **vpnv6** **route-distinguisher** *strRd* **routing-table** **statistics** **community** [ *communityNum* | *strCommunityNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** | **g-shut** ] &<1-33>

**display bgp instance** *bgpName* **vpnv6** **route-distinguisher** *strRd* **routing-table** **statistics** **community** [ *communityNum* | *strCommunityNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** | **g-shut** ] &<1-33> **whole-match**

**display bgp instance** *bgpName* **vpnv6** **route-distinguisher** *strRd* **routing-table** **statistics** **as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**display bgp instance** *bgpName* **vpnv6** **route-distinguisher** *strRd* **routing-table** **statistics** **regular-expression** *strRegular*

**display bgp instance** *bgpName* **vpnv6** **route-distinguisher** *strRd* **routing-table** **statistics**

**display bgp instance** *bgpName* **vpnv6** { **route-distinguisher** *strRd* | **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **different-origin-as**

**display bgp instance** *bgpName* **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** **label**

**display bgp instance** *bgpName* **vpnv6** **route-distinguisher** *strRd* **routing-table** **statistics** **extcommunity** [ { **rt** | **soo** } *strExtCommunity* ] &<1-33>

**display bgp instance** *bgpName* **vpnv6** **route-distinguisher** *strRd* **routing-table** **statistics** **extcommunity** [ { **rt** | **soo** } *strExtCommunity* ] &<1-33> **match-any**

**display bgp instance** *bgpName* **vpnv6** **route-distinguisher** *strRd* **routing-table** **statistics** **extcommunity-filter** { *basic-extcomm-flt-num* | *adv-extcomm-flt-num* | *extcommunity-filter-name* }

**display bgp instance** *bgpName* **vpnv6** **route-distinguisher** *strRd* **routing-table** **statistics** **large-community-filter** *largeComFilName*

**display bgp instance** *bgpName* **vpnv6** **route-distinguisher** *strRd* **routing-table** **statistics** **large-community-filter** *largeComFilName* **whole-match**

**display bgp instance** *bgpName* **vpnv6** **route-distinguisher** *strRd* **routing-table** **statistics** **large-community** [ *largeCommuStr* ] &<1-33>

**display bgp instance** *bgpName* **vpnv6** **route-distinguisher** *strRd* **routing-table** **statistics** **large-community** [ *largeCommuStr* ] &<1-33> **whole-match**

**display bgp instance** *bgpName* **vpnv6** { **route-distinguisher** *strRd* | **all** | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** { **active** | **best** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-distinguisher** *strRd* | Specifies a remote RD. | The value is a string of 3 to 21 case-sensitive characters, spaces not supported. |
| **community-filter** *community-filter-num* | Specifies the number of a basic community filter. | The value is an integer ranging from 1 to 99. |
| **community-filter** *community-filter-numEx* | Specifies the number of an advanced community filter. | The value is an integer ranging from 100 to 199. |
| **community-filter** *community-filter-name* | Specifies the name of a community filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |
| **whole-match** | Indicates exact matching. | - |
| **community** *communityNum* | Specifies a community number. | The value is an integer ranging from 0 to 4294967295. |
| **community** *strCommunityNum* | Specifies a community number. | The value is a string of 1 to 11 case-sensitive characters, spaces not supported. |
| **internet** | Displays the BGP public network routes carrying the internet community attribute. | - |
| **no-advertise** | Displays the BGP routes carrying the No-Advertise community attribute. | - |
| **no-export** | Displays the BGP public network routes carrying the No-Export community attribute. | - |
| **no-export-subconfed** | Displays the BGP routes carrying the No-Export-Subconfed community attribute. | - |
| **g-shut** | Display routes with the Grateful-Shutdown community attribute. | - |
| **as-path-filter** *as-path-filter-num* | Specifies an AS\_Path filter index. | The value is a decimal integer ranging from 1 to 256. |
| **as-path-filter** *as-path-filter-name* | AS path filter name (the name is a string of 1 to 51 characters, which cannot contain only numbers.). | The value is a string of 1 to 51 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |
| **regular-expression** *strRegular* | Displays the routes that match the regular expression. | The value is a string of 1 to 80 characters. |
| **all** | Display all information on VPNv6 and IPv6 VPN instance. | - |
| **vpn-instance** *vpn-instance-name* | Specify a VPN-Instance (VRF) name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **different-origin-as** | Displays the routes with the same destination address and mask but different origin AS numbers. | - |
| **label** | Labeled route information. | - |
| **extcommunity** | Specifies the excommunity value. | - |
| **rt** | Displays information about routes with a specified RT. | - |
| **soo** | Displays information about IPv4 routes with the source of origin (SoO) extended community attribute. | - |
| *strExtCommunity* | Specifies the excommunity value. | The attribute is a BGP extended community attribute and can be expressed in any of the following formats:   * 2-byte AS number:4-byte user-defined number, for example, 1:3. The AS number ranges from 0 to 65535, and the user-defined number ranges from 0 to 4294967295. The AS number and user-defined number cannot both be set to 0. Specifically, the value of the SoO attribute cannot be 0:0. * IPv4-address:2-byte user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number ranges from 0 to 65535. * Integral 4-byte AS number:2-byte user-defined number, for example, 0:3 or 65537:3. An AS number ranges from 65536 to 4294967295. A user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers ranging from 0 to 65535. A user-defined number ranges from 0 to 65535. The AS number and user-defined number cannot be both 0s. Specifically, the value of the SoO attribute cannot be 0.0:0. |
| **match-any** | Displays information about routes with any of the specified extended community attributes. | - |
| **extcommunity-filter** *basic-extcomm-flt-num* | Specifies the number of an extcommunity filter. | The value is an integer ranging from 1 to 199. |
| **extcommunity-filter** *adv-extcomm-flt-num* | Specifies the number of an advanced extcommunity filter. | The value is an integer ranging from 200 to 399. |
| **extcommunity-filter** *extcommunity-filter-name* | Specifies the name of an extcommunity filter. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |
| **large-community-filter** *largeComFilName* | Large-Community filter name. | The value is a string of 1 to 51 case-sensitive characters. The string cannot be all digits. |
| **large-community** *largeCommuStr* | Specifies a value of the Large-Community attribute. | The value is in the format of a:b:c. The values of a, b, and c are integers ranging from 0 to 4294967295. |
| **active** | Displays the active routes. | - |
| **best** | Displays Best, add-path, and best-external routes. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view BGP multi-instance VPNv6 route statistics based on specified attributes, run the **display bgp instance vpnv6 routing-table statistics** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about BGP multi-instance VPNv6 routes carrying community attributes.
```
<HUAWEI> display bgp instance a vpnv6 route-distinguisher 11:11 routing-table statistics extcommunity
 
 Route Distinguisher: 11:11

 Total Number of Routes: 3

 VPN-Instance lzy, Router ID 10.1.123.1:
 Total Number of Routes: 3

```

**Table 1** Description of the **display bgp instance vpnv6 routing-table statistics** command output
| Item | Description |
| --- | --- |
| Route Distinguisher | Route distinguisher. |
| Total Number of Routes | Total number of routes. |