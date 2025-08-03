display bgp ipv6 routing-table (Route Attributes)
=================================================

display bgp ipv6 routing-table (Route Attributes)

Function
--------



The **display bgp ipv6 routing-table** command displays BGP4+ public network routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 routing-table** *ipv6-address* [ *prefix-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }

**display bgp ipv6 routing-table peer** { *peerIpv4Addr* | *peerIpv6Addr* } **advertised-routes** *ipv6-address* [ *prefix-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer to be displayed. | The value is in the X:X:X:X:X:X:X:X format. |
| *prefix-length* | Specifies the mask length of a network address. | The value is an integer that ranges from 0 to 128. |
| **as-path** | Displays the AS\_Path attribute contained in a public network route. | - |
| **community-list** | Displays the community attribute contained in a public network route. | - |
| **large-community** | Displays the BGP routes with the specified Large-Community attribute. | - |
| **ext-community** | Displays the extended community attribute contained in a public network route. | - |
| **cluster-list** | Displays the cluster list contained in a route. | - |
| **advertised-peer** | Displays the list of the peers to which a route is advertised. | - |
| **peer** *peerIpv6Addr* | Specify an IPv6 peer address. | The value is in the X:X:X:X:X:X:X:X format. |
| *peerIpv4Addr* | Displays the IPv4 address of a peer on which public network routes are to be displayed. | The value is in dotted decimal notation. |
| **advertised-routes** | Displays the BGP4+ public network routes advertised to a specified peer. | - |



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


# Display the extended community attributes of all routes in the BGP4+ public network routing table.
```
<HUAWEI> display bgp ipv6 routing-table 2001:DB8:111::1 ext-community
BGP routing table entry information of 2001:DB8:100::/96:
 From: 2001:DB8:100::2
 BGP routing table entry information of 2001:DB8:101::101/128:
 From: 2001:DB8:100::2
 BGP routing table entry information of 2001:DB8:200::200/128:
 From: 2001:DB8:100::2
 Ext-Community: RT <300 : 1>

```

# Display AS-Path information about BGP IPv6 routes.
```
<HUAWEI> display bgp ipv6 routing-table 2001:DB8:111::1 as-path
BGP routing table entry information of 2001:DB8:111::1/128:
 Imported route.
 From: ::
 AS-path Nil
 BGP routing table entry information of ::FFFF:127.0.0.1/128:
 Imported route.
 From: ::
 AS-path Nil
 BGP routing table entry information of 2001:DB8:100::100/128:
 Imported route. 
 From: ::
 AS-path Nil

```

# Display the Large-Community attributes of all routes in the BGP4+ routing table.
```
<HUAWEI> display bgp ipv6 routing-table 2001:DB8:111::1 large-community
BGP routing table entry information of 2001:DB8:111::1/128:
 From: 2001:DB8:10::2
 Large-Community: <400:1:1>

```

# Display the cluster list attributes of all routes in the BGP4+ public network routing table.
```
<HUAWEI> display bgp ipv6  routing-table 2001:DB8:111::1 cluster-list
BGP routing table entry information of 2001:DB8:111::1/128:
 Imported route.
 From: ::
 BGP routing table entry information of ::FFFF:127.0.0.1/128:
 Imported route.
 From: ::
 BGP routing table entry information of 2001:DB8:100::/96:
 Imported route.
 From: ::
 BGP routing table entry information of 2001:DB8:100::/96:
 From: 2001:DB8:100::2
 BGP routing table entry information of 2001:DB8:100::1/128:
 Imported route.
 From: ::
 BGP routing table entry information of 2001:DB8:103::103/128:
 From: 2001:DB8:100::2
 Cluster list: 10.3.3.3
 BGP routing table entry information of 2001:DB8:200::200/128:
 From: 2001:DB8:100::2

```

# Display the community attributes of all routes in the BGP4+ public network routing table.
```
<HUAWEI> display bgp ipv6 routing-table 2001:DB8:111::1 community-list
BGP routing table entry information of 2001:DB8:100::/96:
 From: 2001:DB8:100::2
 Community: <400:1>
 BGP routing table entry information of 2001:DB8:101::101/128:
 From: 2001:DB8:100::2
 Community: <400:1>
 BGP routing table entry information of 2001:DB8:200::200/128:
 From: 2001:DB8:100::2
 Community: <400:1>

```

**Table 1** Description of the **display bgp ipv6 routing-table (Route Attributes)** command output
| Item | Description |
| --- | --- |
| BGP routing table entry information of | Routing entry information. |
| Imported route | Routes imported into the BGP routing table using the import-route command. |
| AS-path | AS\_Path attribute.  Nil indicates that the attribute value is null. |
| Cluster list | Cluster list of a route. |
| Large-Community | Large-Community attribute of a route. |
| Ext-Community | Extended community attribute of a route. |
| From | IP address of the device that advertises the route. |
| Community | Community attribute of a route. |