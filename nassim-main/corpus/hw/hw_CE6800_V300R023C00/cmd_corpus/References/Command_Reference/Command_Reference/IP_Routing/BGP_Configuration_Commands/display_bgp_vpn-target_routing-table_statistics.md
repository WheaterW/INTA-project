display bgp vpn-target routing-table statistics
===============================================

display bgp vpn-target routing-table statistics

Function
--------



The **display bgp vpn-target routing-table statistics** command displays statistics about routes in the BGP-VPN-Target address family.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bgp vpn-target routing-table** { [ **peer** { *ipv4-address* | *ipv6-address* } { **advertised-routes** | **received-routes** } ] | [ **origin-as** *origin-as-num* ] } **statistics**

For CE6885-LL (low latency mode):

**display bgp vpn-target routing-table** { [ **peer** *ipv4-address* { **advertised-routes** | **received-routes** } ] | [ **origin-as** *origin-as-num* ] } **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** *ipv4-address* | Specifies an IPv4 address. | It is in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **advertised-routes** | Displays information about routes advertised to a specified peer. | - |
| **received-routes** | Displays information about the routes received from the specified peer. | - |
| **origin-as** *origin-as-num* | Displays information about RT routes with the specified origin AS number. | The value is an integer that ranges from 0 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display bgp vpn-target routing-table statistics command displays statistics about routes in the BGP-VPN-Target address family.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about routes in the BGP VPN-target address family.
```
<HUAWEI> display bgp vpn-target routing-table peer 10.2.2.2 received-routes statistics
 Total Number of Routes: 1

```

**Table 1** Description of the **display bgp vpn-target routing-table statistics** command output
| Item | Description |
| --- | --- |
| Total Number of Routes | Number of BGP routes. |