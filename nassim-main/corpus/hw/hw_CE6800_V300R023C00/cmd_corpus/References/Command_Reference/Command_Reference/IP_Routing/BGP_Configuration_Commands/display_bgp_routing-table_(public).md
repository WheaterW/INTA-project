display bgp routing-table (public)
==================================

display bgp routing-table (public)

Function
--------



The **display bgp routing-table** command displays BGP public network routes.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display bgp routing-table peer** *ipv4-address* **received-routes**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bgp routing-table peer** *ipv6-address* **received-routes**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **received-routes** | Displays the public network routes received from a specified peer. | - |
| **peer** *ipv4-address* | Displays the IPv4 address of a peer on which public network routes are to be displayed. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies the IPv6 address of a peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp routing-table** command displays active and inactive BGP routes on the public network.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed routes information advertised to a specified peer.
```
<HUAWEI> display bgp routing-table peer 10.1.1.1 advertised-routes 10.9.9.9
BGP local router ID : 10.1.1.2
 Local AS number : 100
 BGP routing table entry information of 10.9.9.9/32:
 Label information (Received/Applied): 7505/NULL
 From: 172.16.1.3 (172.16.1.3)  
 Route Duration: 3d05h25m45s
 Relay IP Nexthop: 172.16.1.3
 Relay IP Out-interface: 100GE1/0/1
 Original nexthop: 172.16.1.3
 Advertised nexthop: 10.1.1.2
 Qos information : 0x0            
 AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
 Advertised to such 4 peers:
    10.3.1.1
    10.1.1.1
    10.2.1.1
    172.16.1.3

```

# Display detailed information of the specified routes.
```
<HUAWEI> display bgp routing-table 10.1.1.1
BGP local router ID : 192.168.2.2
 Local AS number : 100
 Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
 BGP routing table entry information of 10.1.1.1/32:
 From: 10.1.3.1 (192.168.2.3)
 Route Duration: 0d00h01m33s
 Direct Out-interface: 100GE1/0/1
 Relay is delayed as nexthop flapped frequently
 Original nexthop: 10.1.3.1
 Qos information : 0x0
 Primary Routing Table: vrf1
 AS-path 200, origin incomplete, MED 0, pref-val 0, valid, external, best, select, active, pre 255
 Advertised to such 1 peers:
    10.1.3.1

```

**Table 1** Description of the **display bgp routing-table (public)** command output
| Item | Description |
| --- | --- |
| BGP routing table entry information of | Routing Entry Info. |
| BGP local router ID | ID of the local BGP device. |
| Local AS number | Local AS number. |
| MED | MED of the route. |
| Label information (Received/Applied) | Label information (received label/advertised label). |
| Route Duration | Route duration. |
| Relay is delayed as nexthop flapped frequently | Route recursion to a specified next hop is suppressed because the next hop flaps. If the number of routes is small, the suppression period may be too short. In this case, this field is not displayed in the command output. |
| Relay IP Nexthop | IP recursive next hop. |
| Original nexthop | Original next hop. |
| Advertised to such 1 peers | Peers to which routes are sent. |
| Advertised nexthop | Advertisement next hop. |
| Qos information | Qos information. |
| Direct Out-interface | Directly connected outbound interface. |
| Primary Routing Table | Source routing table. |
| Paths | Route selection result. |
| From | IP address of the route advertiser. |