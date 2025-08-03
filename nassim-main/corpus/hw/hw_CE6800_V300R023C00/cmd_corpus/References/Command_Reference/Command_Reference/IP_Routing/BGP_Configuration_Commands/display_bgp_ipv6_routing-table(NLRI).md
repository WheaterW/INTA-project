display bgp ipv6 routing-table(NLRI)
====================================

display bgp ipv6 routing-table(NLRI)

Function
--------



The **display bgp ipv6 routing-table** command displays the routing information of the specified BGP4+ routes in public routing table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 routing-table** *ipv6-address* [ *mask-length* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer to be displayed. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *mask-length* | Specifies the mask length of a network address. | It is an integer ranging from 0 to 128. |



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


# Display details of IPv6 routes.
```
<HUAWEI> display bgp ipv6 routing-table 2001:DB8:9:3::1 64
 
 BGP local router ID : 10.3.3.3
 Local AS number : 65009
 Paths:   2 available, 1 best, 1 select, 0 best-external, 0 add-path
 BGP routing table entry information of 2001:DB8:9:3::/64:
 Network route.
 From: :: (0.0.0.0)  
 Route Duration: 1d11h38m10s
 Direct Out-interface: Loopback1
 Original nexthop: 2001:DB8:9:3::2
 Qos information : 0x0
 AS-path Nil, origin igp, MED 0, pref-val 0, valid, local, best, select, pre 0
 Advertised to such 1 peers:
    2001:DB8:9:3::1

 BGP routing table entry information of 2001:DB8:9:3::/64:
 From: 2001:DB8:9:3::1 (10.2.2.2)  
 Route Duration: 1d11h37m50s
 Relay IP Nexthop: 2001:DB8:9:3::1
 Relay IP Out-Interface: Loopback1
 Original nexthop: 2001:DB8:9:3::1
 Qos information : 0x0
 AS-path Nil, origin igp, MED 0, localpref 100, pref-val 0, internal, supernet, pre 255, invalid for super network
 Not advertised to any peer yet

```

**Table 1** Description of the **display bgp ipv6 routing-table(NLRI)** command output
| Item | Description |
| --- | --- |
| BGP local router ID | Router ID of the local BGP device. |
| Local AS number | Local AS number. |
| Route Duration | Route duration. |
| Direct Out-interface | Directly connected outbound interface. |
| Original nexthop | Original next hop. |
| AS-path | AS\_Path attribute. Nil indicates that the attribute value is null. |
| MED | Indicates the MED of the route. |
| Advertised to such 1 peer | Peers to which routes are advertised. |
| Relay IP Nexthop | Next hop for IP recursion. |
| Relay IP Out-Interface | Iterated outbound interface. |
| Not advertised to any peer yet | No route is advertised to the BGP peer. |
| Paths | Route selection result. |
| From | IP address of the router that sends the route. |