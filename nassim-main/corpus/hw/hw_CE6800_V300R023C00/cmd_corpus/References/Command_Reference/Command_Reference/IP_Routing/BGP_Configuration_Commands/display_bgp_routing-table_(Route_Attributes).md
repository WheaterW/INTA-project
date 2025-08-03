display bgp routing-table (Route Attributes)
============================================

display bgp routing-table (Route Attributes)

Function
--------



The **display bgp vpnv4 routing-table** command displays information about BGP VPNv4 routes and BGP VPN routes.

The **display bgp routing-table** command displays information about BGP public network routes.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display bgp routing-table** *ipv4-address* [ *mask* | *mask-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }

**display bgp vpnv4 all routing-table** *ipv4-address* [ *mask* | *mask-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }

**display bgp vpnv4 vpn-instance** *vpn-instance-name* **routing-table** *ipv4-address* [ *mask* | *mask-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }

**display bgp routing-table peer** *remoteIpv4Addr* **advertised-routes** *ipv4-address* [ *mask* | *mask-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }

**display bgp vpnv4 all routing-table peer** *remoteIpv4Addr* **advertised-routes** *ipv4-address* [ *mask* | *mask-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }

**display bgp vpnv4 vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv4Addr* **advertised-routes** *ipv4-address* [ *mask* | *mask-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }

**display bgp instance** *instance-name* **vpnv4** **all** **routing-table** *ipv4-address* [ *mask* | *mask-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }

**display bgp instance** *instance-name* **vpnv4** **vpn-instance** *vpn-instance-name* **routing-table** *ipv4-address* [ *mask* | *mask-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }

**display bgp instance** *instance-name* **vpnv4** **all** **routing-table** **peer** *remoteIpv4Addr* **advertised-routes** *ipv4-address* [ *mask* | *mask-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }

**display bgp instance** *instance-name* **vpnv4** **vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv4Addr* **advertised-routes** *ipv4-address* [ *mask* | *mask-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bgp routing-table peer** *remoteIpv6Addr* **advertised-routes** *ipv4-address* [ *mask* | *mask-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *mask* | Specifies a mask. | The value is in dotted decimal notation. |
| *mask-length* | Length of IP address mask. | The value is an integer ranging from 0 to 32. |
| **as-path** | Displays AS\_Path attribute information. | - |
| **community-list** | Displays the community attribute contained in a route. | - |
| **large-community** | Displays the routes with the specified BGP Large-Community in the routing table. | - |
| **ext-community** | Displays the extended community list of the route. | - |
| **cluster-list** | Displays the cluster list of a route. | - |
| **advertised-peer** | Displays the list of the peers for which a route is destined. | - |
| **all** | Displays all the VPNv4 and VPN instance routes. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **peer** *remoteIpv4Addr* | Displays the IPv4 address of a peer on which public network routes are to be displayed. | The value is in dotted decimal notation. |
| *remoteIpv6Addr* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **advertised-routes** | Displays public network routes advertised to a specified peer. | - |
| **instance** *instance-name* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



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


# Display the Large-Community attributes of all routes in the BGP routing table.
```
<HUAWEI> display bgp routing-table 192.168.1.1 24 large-community
BGP routing table entry information of 192.168.1.1/24:
 Aggregated oute.
 Large-community: 200:1:1>, 300:1:1>

```

# Display the community attributes of all routes in the BGP public network routing table.
```
<HUAWEI> display bgp routing-table 192.168.1.1 24 community-list
BGP routing table entry information of 192.168.1.0/24:
 From: 192.168.1.1
 Community: <400:1>

```

# Display AS\_Path information contained in BGP public network routes.
```
<HUAWEI> display bgp routing-table 192.168.1.1 24 as-path
BGP routing table entry information of 192.168.1.0/24:
 From: 192.168.1.1
 AS-path 100

```

**Table 1** Description of the **display bgp routing-table (Route Attributes)** command output
| Item | Description |
| --- | --- |
| BGP routing table entry information | The following information is about a specified BGP routing entry. |
| AS-path | AS\_Path attribute.  Nil indicates that the attribute value is null. |
| From | IP address of the device that advertised routes. |
| Community | Community attribute of the route. |
| Large-community | Large-community attribute information. |