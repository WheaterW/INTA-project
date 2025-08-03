reset bgp flap-info
===================

reset bgp flap-info

Function
--------



The **reset bgp flap-info** command clears route flapping statistics.




Format
------

**reset bgp** [ **instance** *instance-name* ] [ **vpn-instance** *vpn-instance-name* **ipv4-family** ] **flap-info** *network-address* [ *mask* | *mask-length* ]

**reset bgp** [ **instance** *instance-name* ] [ **vpn-instance** *vpn-instance-name* **ipv4-family** ] *ipv4-address* **flap-info**

**reset bgp** [ **instance** *instance-name* ] [ **vpn-instance** *vpn-instance-name* **ipv4-family** ] **flap-info**

**reset bgp** [ **instance** *instance-name* ] [ **vpn-instance** *vpn-instance-name* **ipv4-family** ] **flap-info** **as-path-filter** { *as-path-filter-number* | *as-path-filter-name* }

**reset bgp** [ **instance** *instance-name* ] [ **vpn-instance** *vpn-instance-name* **ipv4-family** ] **flap-info** **regexp** *as-path-regexp*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-name* | Specifies a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **vpn-instance** *vpn-instance-name* | Clears the route flapping information of a specified VPN instance enabled with an IPv4 address family. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name cannot be \_public\_. If the string is enclosed in double quotation marks (" "), the string can contain spaces.. |
| **ipv4-family** | Indicates the IPv4 address family. | - |
| *network-address* | Specifies the network address of an IPv4 peer. | The value is in dotted decimal notation. |
| *mask* | Specifies the network mask that is used to filter the BGP IPv4 routes. If neither of the mask nor mask length is specified, the address is considered as a classful address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the network mask length that is used to filter the BGP IPv4 routes. If neither of the mask nor mask length is specified, the address is considered as a classful address. | The value is an integer in the range from 0 to 32. |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **as-path-filter** *as-path-filter-number* | Clears route flapping statistics based on a specified AS\_Path filter. | The value is an integer ranging from 1 to 256. |
| *as-path-filter-name* | Clears route flapping statistics based on a specified AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |
| **regexp** *as-path-regexp* | Clear statistics about the flapping routes that match the AS\_Path regular expression. | The value is a string of 1 to 80 case-sensitive characters with spaces supported. |



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



You can use **display bgp routing-table flap-info** command to view the information about BGP route flapping.If there are a large number of flapping routes, define an AS\_Path filter or an AS\_Path regular expression to be referenced in the **reset bgp flap-info** command. The flapping statistics of the routes matching the AS\_Path filter or the AS\_Path regular expression are then cleared.



**Follow-up Procedure**



After the flapping statistics of routes are cleared, you can run the **display bgp routing-table flap-info** command again to view the flapping statistics of BGP routes to locate the fault.




Example
-------

# Clear the flapping statistics about the routes that match AS\_Path filter 10.
```
<HUAWEI> reset bgp flap-info as-path-filter 10

```