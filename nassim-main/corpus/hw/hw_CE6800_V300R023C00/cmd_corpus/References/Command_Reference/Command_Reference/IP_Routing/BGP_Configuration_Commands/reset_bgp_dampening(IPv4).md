reset bgp dampening(IPv4)
=========================

reset bgp dampening(IPv4)

Function
--------



The **reset bgp dampening** command clears BGP route dampening information and releases suppressed routes.




Format
------

**reset bgp** [ **vpn-instance** *vpn-instance-name* **ipv4-family** ] **dampening**

**reset bgp** [ **vpn-instance** *vpn-instance-name* **ipv4-family** ] **dampening** *ipv4-address* [ *mask* | *mask-length* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Clears route dampening information of a specified VPN instance enabled with an IPv4 address family. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **ipv4-family** | Indicates the IPv4 address family. | - |
| *ipv4-address* | Specifies an IPv4 network address. | The value is in dotted decimal notation. |
| *mask* | Specifies the network mask in dotted decimal notation. If neither of the mask nor mask length is specified, the address is considered as a classful address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the network mask length. If neither of the mask nor mask length is specified, the address is considered as a classful address. | The value is an integer in the range from 0 to 32. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Route dampening is enabled to solve the problem of route instability. In most situations, BGP is applied to complex networks where routes change frequently. Route dampening is then used to suppress unstable routes.The **reset bgp dampening** command is used to clear dampening information about specified routes on the public network and release specified suppressed routes. If no IP address is specified in the command, dampening information about all routes on the public network is cleared and all suppressed routes are released.

**Prerequisites**



You can use **display bgp routing-table dampened** command to view information about suppressed routes.



**Configuration Impact**

After the **reset bgp dampening** command is run, suppressed routes are released. If the status of some routes still changes frequently, route flapping may occur. Routing flapping consumes a large number of bandwidth and CPU resources.


Example
-------

# Clear dampening information about IPv4 routes and release suppressed routes.
```
<HUAWEI> reset bgp dampening 10.1.0.0 255.255.0.0

```