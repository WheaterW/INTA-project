display bgp unnumbered peer interface statistics
================================================

display bgp unnumbered peer interface statistics

Function
--------



The **display bgp unnumbered peer interface statistics** command displays the route statistics of the BGP unnumbered peers.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display bgp unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **statistics**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bgp ipv6 unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 characters. |
| *IfType* | Specifies an interface type. | - |
| *IFNum* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **ipv6** | Indicates the IPv6 unicast address family.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

On a network with a monitoring server, routers send packets to the monitoring server to report BGP running statistics for monitoring. The **display bgp unnumbered peer interface statistics** command displays statistics about the routes learned from unnumbered BGP peers and sent by a device to a monitoring server.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about the routes of the BGP unnumbered peer.
```
<HUAWEI> display bgp unnumbered peer interface 100GE 1/0/1 statistics

Peer FE80::3AAE:90FF:FE11:309(100GE 1/0/1), IPv4 Unicast
   Number of prefixes rejected by inbound policy         : 0
   Number of (known) duplicate prefix advertisements     : 0
   Number of (known) duplicate withdraws                 : 0
   Number of updates invalidated due to CLUSTER_LIST loop: 0
   Number of updates invalidated due to AS_PATH loop     : 0
   Number of updates invalidated due to ORIGINATOR_ID    : 0
   Number of updates invalidated due to AS_CONFED loop   : 0
   Number of routes in Adj-RIBs-In (pre-policy)          : 1
   Number of routes in Adj-RIBs-In (post-policy)         : 1
   Number of best routes in Loc-RIB                      : 1

```

**Table 1** Description of the **display bgp unnumbered peer interface statistics** command output
| Item | Description |
| --- | --- |
| Number of prefixes rejected by inbound policy | Number of routes that are filtered out by the import policy. |
| Number of (known) duplicate prefix advertisements | Number of times that a route is re-advertised. |
| Number of (known) duplicate withdraws | Number of times that a route is re-deleted. |
| Number of updates invalidated due to CLUSTER\_LIST loop | Number of routes that are invalid because the local Cluster\_ID exists in the Cluster\_List. |
| Number of updates invalidated due to AS\_PATH loop | Number of routes that are invalid because the local AS number exists in the AS\_Path list. |
| Number of updates invalidated due to ORIGINATOR\_ID | Number of routes that are invalid because their Originator\_IDs are the same as the local router ID. |
| Number of updates invalidated due to AS\_CONFED loop | Number of routes that are invalid because their AS\_Paths contain the AS number of the local confederation. |
| Number of routes in Adj-RIBs-In (pre-policy) | Number of all received routes. |
| Number of routes in Adj-RIBs-In (post-policy) | Number of accepted routes. |
| Number of best routes in Loc-RIB | Number of optimal routes in the routing table. |