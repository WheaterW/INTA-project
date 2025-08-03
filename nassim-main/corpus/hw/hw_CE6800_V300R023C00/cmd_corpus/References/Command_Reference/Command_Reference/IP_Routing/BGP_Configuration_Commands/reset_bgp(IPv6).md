reset bgp(IPv6)
===============

reset bgp(IPv6)

Function
--------



The **reset bgp** command resets a specified BGP IPv6 connection.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset bgp ipv6** { *as-number* | *ipv4-address* | **external** | **internal** | **group** *group-name* }

**reset bgp ipv6 all**

**reset bgp ipv6** *ipv6-address*

**reset bgp** [ **instance** *bgpName* ] **vpn-instance** *vpn-instance-name* **ipv6-family** { **all** | *as-number* | *ipv6-address* | **external** | **internal** | **group** *group-name* }

**reset bgp vpn-instance** *vpn-instance-name* **ipv6-family** *ipv4-address*

**reset bgp ipv6** [ *ipv6-address* ] **slow-peer**

**reset bgp instance** *bgpName* **vpn-instance** *vpn-instance-name* **ipv6-family** [ *ipv6-address* ] **slow-peer**

**reset bgp vpn-instance** *vpn-instance-name* **ipv6-family** [ *ipv4-address* | *ipv6-address* ] **slow-peer**

**reset bgp ipv6** *ipv4-address* **slow-peer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *as-number* | Specifies a 2-byte AS number (number<1-65535>) or a 4-byte AS number (number<1-65535>.number<0-65535>). | For an integral AS number, the value is an integer ranging from 1 to 4294967295.  For an AS number in dotted notation, the value is in the format of x.y, where x and y are integers ranging from 1 to 65535 and from 0 to 65535, respectively. |
| *ipv4-address* | Resets the BGP connection with a specified peer. | The value is in dotted decimal notation. |
| **external** | Reset all EBGP connections. | - |
| **internal** | Resets all IBGP connections. | - |
| **group** *group-name* | Resets BGP connections with the specified peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **ipv6** | Resets BGP IPv6 connections. | - |
| **all** | Reset all BGP connections. | - |
| *ipv6-address* | Resets the TCP connection with a specified BGP4+ peer (all the routes learned by using the connection are deleted). | The value is in the format of X:X:X:X:X:X:X:X. |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **vpn-instance** *vpn-instance-name* | Resets the connection of a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name cannot be \_public\_. If the string is enclosed in double quotation marks (" "), the string can contain spaces.. |
| **ipv6-family** | Indicates the IPv6 address family. | - |
| **slow-peer** | Restores a slow peer connection to a normal peer connection. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **reset bgp** command is used to make new BGP configurations take effect.If a BGP routing policy is changed on a device that does not support the route-refresh capability, the **reset bgp** command can be used to make the new routing policy take effect.

**Configuration Impact**

This command resets all TCP connections established between BGP peers and therefore results in the re-establishment of the BGP peer relationships. Exercise caution when running this command.


Example
-------

# Reset BGP connections with the peer 2001:DB8:1::9.
```
<HUAWEI> reset bgp ipv6 2001:DB8:1::9

```