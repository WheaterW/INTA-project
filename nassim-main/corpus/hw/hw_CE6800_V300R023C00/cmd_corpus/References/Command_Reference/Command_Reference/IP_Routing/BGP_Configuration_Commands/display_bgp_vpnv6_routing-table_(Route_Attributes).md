display bgp vpnv6 routing-table (Route Attributes)
==================================================

display bgp vpnv6 routing-table (Route Attributes)

Function
--------



The **display bgp vpnv6 routing-table** command displays BGP VPNv6 routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp** [ **instance** *bgpName* ] **vpnv6** **all** **routing-table** *ipv6-address* [ *ipv6-mask-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **routing-table** *ipv6-address* [ *ipv6-mask-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **routing-table** **peer** *peerIpv6Addr* **advertised-routes** *ipv6-address* [ *ipv6-mask-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *bgpName* | Specifies the name of a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all** | Displays all information about VPNv6 and IPv6 VPN instances. | - |
| *ipv6-address* | Specifies an ipv6 network address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *ipv6-mask-length* | Specifies an IP address mask length. | The value is an integer ranging from 0 to 128. |
| **as-path** | Indicates the AS path list. | - |
| **community-list** | Indicates the BGP community list. | - |
| **large-community** | Displays routes with large communities. | - |
| **ext-community** | Indicates the BGP ext-community list. | - |
| **cluster-list** | Indicates a BGP RR cluster list. | - |
| **advertised-peer** | Indicates the list of peers to which routes are sent. | - |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **peer** *peerIpv6Addr* | Specifies an IPv6 peer address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **advertised-routes** | Indicates the routes advertised to the peer. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv6 routing-table** command displays BGP VPNv6 routes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the cluster list contained in a VPNv6 route with a specified prefix.
```
<HUAWEI> display bgp vpnv6 all routing-table 2001:DB8:2:3:: cluster-list
Routes of vpn-instance vrf2:
 BGP routing table entry information of 2001:DB8:2:3::/64:
 From: 2001:DB8:42:4::7:7

```

# Display the Ext-Community information contained in a VPNv6 route with a specified prefix.
```
<HUAWEI> display bgp vpnv6 all routing-table 2001:DB8:2:3:: ext-community
Routes of vpn-instance vrf2:
 BGP routing table entry information of 2001:DB8:2:3::/64:
 From: 2001:DB8:42:4::7:7

```

# Display the AS\_Path information contained in a VPNv6 route with a specified prefix.
```
<HUAWEI> display bgp vpnv6 all routing-table 2001:DB8:2:3:: as-path
Routes of vpn-instance vrf2:
 BGP routing table entry information of 2001:DB8:2:3::/64:
 From: 2001:DB8:42:4::7:7
 AS-path 65004

```

**Table 1** Description of the **display bgp vpnv6 routing-table (Route Attributes)** command output
| Item | Description |
| --- | --- |
| BGP routing table entry information of | The following information is about a specified BGP routing entry. |
| AS-path | AS\_Path attribute.  Nil indicates that the attribute value is null. |
| From | IPv6 address of the route originator. |