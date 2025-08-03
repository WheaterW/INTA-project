display bgp error discard
=========================

display bgp error discard

Function
--------



The **display bgp error discard** command displays BGP errors.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bgp error discard** [ **peer** { *ipv4-address* | *ipv6-address* } ]

**display bgp error discard vpn-instance** *vpn-instance-name* **peer** { *ipv4-address* | *ipv6-address* }

**display bgp instance** *instance-name* **error** **discard** **vpn-instance** *vpn-instance-name* **peer** { *ipv4-address* | *ipv6-address* }

For CE6885-LL (low latency mode):

**display bgp error discard** [ **peer** *ipv4-address* ]

**display bgp error discard vpn-instance** *vpn-instance-name* **peer** *ipv4-address*

**display bgp instance** *instance-name* **error** **discard** **vpn-instance** *vpn-instance-name* **peer** *ipv4-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies the IPv6 address of a peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **vpn-instance** *vpn-instance-name* | Displays the BGP errors of a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **instance** *instance-name* | Specifies a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When a BGP fault occurs, you can run this command to check BGP errors. BGP error information includes peer error information, route error information, and resource threshold-crossing error information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about discarded BGP error packets.
```
<HUAWEI> display bgp error discard
BGP discard Info Counts: 
 Routes received with cluster ID loop            : 0
 Routes received with As path count over limit   : 0
 Routes advertised with As path count over limit : 0
 Routes received with As loop                    : 0
 Routes received with Zero RD(0:0)               : 0
 Routes received with no prefix                  : 0
 Routes received with error path-attribute       : 0
 Routes received with originator ID loop         : 0
 Routes received with total number over limit    : 0
 Routes received with error router id            : 0
 Routes received with same soo                   : 2
 
BGP discard info:(IPv4 Unicast)
 Routes received with cluster ID loop            : 0
 Routes received with As path count over limit   : 0
 Routes advertised with As path count over limit : 0
 Routes received with As loop                    : 0
 Routes received with Zero RD(0:0)               : 0
 Routes received with error path-attribute       : 0
 Routes received with originator ID loop         : 0
 Routes received with total number over limit    : 0
 Routes received with same soo                   : 2

No discard record.

```

**Table 1** Description of the **display bgp error discard** command output
| Item | Description |
| --- | --- |
| BGP discard info | Number of routes discarded by BGP. |
| Routes received with cluster ID loop | Number of routes discarded due to duplicate cluster IDs. |
| Routes received with As loop | Number of routes discarded due to repeated AS numbers. |
| Routes received with Zero RD(0:0) | Number of routes discarded because the RD value is 0. |
| Routes received with no prefix | Number of routes discarded because there are no route prefixes. |
| Routes received with error path-attribute | Number of BGP routes with invalid attributes. |
| Routes received with originator ID loop | Total number of routes that carry the original ID. |
| Routes received with total number over limit | Total number of routes that are discarded because the number of routes exceeds the upper limit. |
| Routes received with error router id | Number of routes with incorrect router IDs and connection failures. |
| Routes received with As path count over limit | Number of received routes that are discarded because the number of AS\_Paths exceeds the upper limit. |
| Routes advertised with As path count over limit | Number of sent routes discarded because the AS\_Path exceeds the upper limit. |
| Routes received with same soo | Number of routes discarded because the SoO values of the received routes are the same. |