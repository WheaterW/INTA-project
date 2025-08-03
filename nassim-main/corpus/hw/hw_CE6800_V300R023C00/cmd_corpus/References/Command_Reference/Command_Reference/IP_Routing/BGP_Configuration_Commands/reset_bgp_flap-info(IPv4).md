reset bgp flap-info(IPv4)
=========================

reset bgp flap-info(IPv4)

Function
--------



The **reset bgp flap-info** command clears route flapping statistics.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**reset bgp** [ **vpn-instance** *vpn-instance-name* **ipv4-family** ] **flap-info** *ipv4-address* [ *mask* | *mask-length* ]

**reset bgp** [ **vpn-instance** *vpn-instance-name* **ipv4-family** ] *peerIpv4Addr* **flap-info**

**reset bgp** [ **vpn-instance** *vpn-instance-name* **ipv4-family** ] **flap-info**

**reset bgp** [ **vpn-instance** *vpn-instance-name* **ipv4-family** ] **flap-info** **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* }

**reset bgp** [ **vpn-instance** *vpn-instance-name* **ipv4-family** ] **flap-info** **regexp** *as-path-regexp*

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**reset bgp** [ **instance** *bgpName* ] **vpn-instance** *vpn-instance-name* **ipv6-family** **flap-info** **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* }

**reset bgp** [ **instance** *bgpName* ] **vpn-instance** *vpn-instance-name* **ipv6-family** **flap-info** **regexp** *as-path-regexp*

**reset bgp** *peerIpv6Addr* **flap-info**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the network address of an IPv4 peer. | The value is in dotted decimal notation. |
| *mask* | Specifies the network mask that is used to filter the BGP IPv4 routes. If neither of the mask nor mask length is specified, the address is considered as a classful address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the network mask length that is used to filter the BGP IPv4 routes. If neither of the mask nor mask length is specified, the address is considered as a classful address. | The value is an integer ranging from 0 to 32. |
| *peerIpv4Addr* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **as-path-filter** *as-path-filter-number* | Clears route flapping statistics based on a specified AS\_Path filter. | The value is an integer ranging from 1 to 256. |
| **as-path-filter** *as-path-filter-name* | Clears route flapping statistics based on a specified AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |
| **regexp** *as-path-regexp* | Specifies the AS\_Path regular expression. | The value is a string of 1 to 80 case-sensitive characters, spaces supported. |
| **vpn-instance** *vpn-instance-name* | Clears the route flapping information of a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name cannot be \_public\_. If the string is enclosed in double quotation marks (" "), the string can contain spaces.. |
| **ipv6-family** | Indicates the IPv6 address family.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| *peerIpv6Addr* | Specifies the network address of an IPv6 peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is in the format of X:X:X:X:X:X:X:X. |
| **ipv4-family** | Indicates the IPv4 address family. | - |
| **instance** *bgpName* | Specifies the BGP multi-instance name.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a route is added to the routing table, the route is withdrawn. This process is called route flapping.When route flapping occurs, a device sends an Update message to its peers. The devices that receive the Update message need to recalculate routes and modify their routing tables. Therefore, frequent route flapping consumes a large number of bandwidth and CPU resources and even affects the normal operation of the network.You can run the **reset bgp flap-info** command to clear statistics about flapping BGP routes so that the device can recollect statistics about flapping routes. This helps you monitor route changes and locate network problems.

**Prerequisites**



You can use **display bgp routing-table flap-info** command to view the information about BGP route flapping.If there are a large number of flapping routes, define an AS\_Path filter or an AS\_Path regular expression to be referenced in the **reset bgp flap-info** command. The flapping statistics of the routes matching the AS\_Path filter or the AS\_Path regular expression are then cleared.



**Configuration Impact**



After the **reset bgp flap-info** command is run, the flapping statistics of routes are reset and cannot be displayed.



**Follow-up Procedure**



After the flapping statistics of routes are cleared, you can run the **display bgp routing-table flap-info** command again to view the flapping statistics of BGP routes to locate the fault.




Example
-------

# Clear the flapping statistics about the routes that match AS\_Path filter 10.
```
<HUAWEI> reset bgp flap-info as-path-filter 10

```