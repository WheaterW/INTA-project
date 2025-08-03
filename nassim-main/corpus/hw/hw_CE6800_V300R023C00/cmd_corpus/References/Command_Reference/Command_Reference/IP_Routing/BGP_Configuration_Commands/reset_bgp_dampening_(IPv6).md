reset bgp dampening (IPv6)
==========================

reset bgp dampening (IPv6)

Function
--------



The **reset bgp dampening** command clears BGP route dampening information and releases suppressed routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset bgp ipv6 dampening**

**reset bgp ipv6 dampening** *ipv6-address* *prefix-length*

**reset bgp** [ **instance** *bgpName* ] **vpn-instance** *vpn-instance-name* **ipv6-family** **dampening** [ *ipv6-address* *prefix-length* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** | Clears IPv6 route dampening information and releases suppressed routes. | - |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the network mask in dotted decimal notation. If neither of the mask nor mask length is specified, the address is considered as a classful address. | It is an integer ranging from 0 to 128. |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **vpn-instance** *vpn-instance-name* | Clears route dampening information of a specified VPN instance enabled with an IPv6 address family. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name cannot be \_public\_. If the string is enclosed in double quotation marks (" "), the string can contain spaces.. |
| **ipv6-family** | Indicates the IPv6 address family. | - |



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

After the **reset bgp dampening** command is run, suppressed routes are released. If the status of some routes still changes frequently, route flapping may occur. Routing flapping consumes a large number of bandwidth and CPU resources.When ipv6-address prefix-length is not specified, after you run the **reset bgp ipv6 dampening** command, IPv6 route dampening information in the whole BGP routing table is cleared.


Example
-------

# Clear IPv6 route dampening information.
```
<HUAWEI> reset bgp ipv6 dampening

```

# Clear dampening information about the routes of IPv6 VPN instance named vpn1.
```
<HUAWEI> reset bgp vpn-instance vpn1 ipv6-family dampening

```