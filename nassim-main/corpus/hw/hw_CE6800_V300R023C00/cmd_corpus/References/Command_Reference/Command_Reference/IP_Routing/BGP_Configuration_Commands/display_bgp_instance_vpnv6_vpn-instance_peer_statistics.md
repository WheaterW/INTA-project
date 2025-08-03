display bgp instance vpnv6 vpn-instance peer statistics
=======================================================

display bgp instance vpnv6 vpn-instance peer statistics

Function
--------



The **display bgp instance vpnv6 vpn-instance peer statistics** command displays route statistics of a specified peer in the BGP multi-instance VPN instance IPv6 address family.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp instance** *bgpName* **vpnv6** **vpn-instance** *vpn-instance-name* **peer** *peerIpv6Addr* **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *peerIpv6Addr* | Specifies an IPv6 peer address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **instance** *bgpName* | Specifies a BGP instance name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp instance vpnv6 vpn-instance peer statistics** command displays route statistics of a specified peer in the BGP multi-instance VPN instance IPv6 address family.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display route statistics of a specified peer in the BGP multi-instance VPN instance IPv6 address family.
```
<HUAWEI> display bgp instance a vpnv6 vpn-instance vrf2 peer 2001:db8:1::1 statistics

Peer 2001:db8:1::1, IPv6 Unicast
   Number of prefixes rejected by inbound policy         : 0
   Number of (known) duplicate prefix advertisements     : 0
   Number of (known) duplicate withdraws                 : 0
   Number of updates invalidated due to CLUSTER_LIST loop: 0
   Number of updates invalidated due to AS_PATH loop     : 0
   Number of updates invalidated due to ORIGINATOR_ID    : 0
   Number of updates invalidated due to AS_CONFED loop   : 0
   Number of routes in Adj-RIBs-In (pre-policy)          : 0
   Number of routes in Adj-RIBs-In (post-policy)         : 1
   Number of best routes in Loc-RIB                      : 1

```

**Table 1** Description of the **display bgp instance vpnv6 vpn-instance peer statistics** command output
| Item | Description |
| --- | --- |
| Number of prefixes rejected by inbound policy | Number of routes that are filtered out by the import policy. |
| Number of (known) duplicate prefix advertisements | Number of times that a route is re-advertised. |
| Number of (known) duplicate withdraws | Number of times that a route is re-deleted. |
| Number of updates invalidated due to CLUSTER\_LIST loop | Number of routes that are invalid because the local Cluster\_ID exists in the Cluster\_List. |
| Number of updates invalidated due to AS\_PATH loop | Number of routes that are invalid because the local AS number exists in the AS\_Path list. |
| Number of updates invalidated due to ORIGINATOR\_ID | Number of routes that are invalid because their Originator\_IDs are the same as the local router ID. |
| Number of updates invalidated due to AS\_CONFED loop | Number of routes that are invalid because their AS\_Path lists contain the AS number of the local confederation. |
| Number of routes in Adj-RIBs-In (pre-policy) | Number of all received routes. |
| Number of routes in Adj-RIBs-In (post-policy) | Number of routes that match the import policy. |
| Number of best routes in Loc-RIB | Total number of optimal routes in the routing table. |