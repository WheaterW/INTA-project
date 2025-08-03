reset bgp flap-info(IPv6)
=========================

reset bgp flap-info(IPv6)

Function
--------



The **reset bgp flap-info** command clears the flapping statistics of IPv6 routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset bgp ipv6 flap-info** *network-ipv6-address* *prefix-length*

**reset bgp ipv6** *ipv6-address* **flap-info**

**reset bgp ipv6 flap-info**

**reset bgp** [ **instance** *bgpName* ] **vpn-instance** *vpn-instance-name* **ipv6-family** **flap-info** [ *network-ipv6-address* *prefix-length* ]

**reset bgp ipv6 flap-info as-path-filter** { *as-path-filter-num* | *as-path-filter-name* }

**reset bgp ipv6 flap-info regexp** *as-path-regexp*

**reset bgp ipv6** *peerIpv4Addr* **flap-info**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *network-ipv6-address* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the network mask that is used to filter the BGP IPv6 routes. If neither of the mask nor mask length is specified, the address is considered as a classful address. | It is an integer ranging from 0 to 128. |
| **ipv6** | Clears the route flapping statistics on all IPv6 peers. | - |
| *ipv6-address* | Specifies the network address of an IPv6 peer. | The format is X:X:X:X:X:X:X:X. |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **vpn-instance** *vpn-instance-name* | Clears route dampening information of a specified VPN instance enabled with an IPv6 address family. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name cannot be \_public\_. If the string is enclosed in double quotation marks (" "), the string can contain spaces.. |
| **ipv6-family** | Indicates the IPv6 address family. | - |
| **as-path-filter** *as-path-filter-num* | Clears route flapping statistics based on a specified AS\_Path filter. | The value is an integer ranging from 1 to 256. |
| **as-path-filter** *as-path-filter-name* | Clears route flapping statistics based on a specified AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |
| **regexp** *as-path-regexp* | Clears statistics about the flapping routes that match the AS\_Path regular expression. | The value is a string of 1 to 80 case-sensitive characters, spaces supported. |
| *peerIpv4Addr* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The process of adding a route to and then deleting the route from a routing table is called route flapping.When route flapping occurs, the routing protocol sends Update packets to neighbors. The neighbors that receive the Update packets need to recalculate routes and modify its routing table. Therefore, frequent route flapping consumes great bandwidth and CPU resources and even seriously affects network operations.The **reset bgp flap-info** command is used to clear the flapping information about routes. This allows the device to re-collect statistics about flapping routes and helps to monitor route changes and locate network problems.

**Prerequisites**

You can use **display bgp routing-table flap-info** command to view the information about BGP route flapping.If there are a large number of flapping routes, you can define as-path-filter or regexp, and then clear the statistics of the matched flapping routes.

**Configuration Impact**

After the **reset bgp flap-info** command is run, the flapping statistics of routes are reset and cannot be displayed.

**Follow-up Procedure**

After the flapping statistics of routes are cleared, you can run the **display bgp routing-table flap-info** command again to view the flapping statistics of BGP routes to locate the fault.


Example
-------

# Clear the flapping statistics about the BGP4+ routes of the VPN instance named vpn1.
```
<HUAWEI> reset bgp vpn-instance vpn1 ipv6-family flap-info

```