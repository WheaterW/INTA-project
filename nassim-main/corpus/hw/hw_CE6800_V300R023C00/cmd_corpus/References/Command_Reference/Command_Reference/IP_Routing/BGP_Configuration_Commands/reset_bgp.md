reset bgp
=========

reset bgp

Function
--------



The **reset bgp** command resets specified BGP connections.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**reset bgp** { *as-number* | *ipv4-address* | **external** | **internal** | **group** *group-name* | *ipv6-address* }

**reset bgp all**

**reset bgp ipv4 all**

**reset bgp vpn-instance** *vpn-instance-name* **ipv4-family** { **all** | *as-number* | *ipv4-address* | **external** | **internal** | **group** *group-name* }

**reset bgp vpn-instance** *vpn-instance-name* **ipv4-family** [ *ipv4-address* ] **slow-peer**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**reset bgp ipv4** [ *ipv4-address* | *ipv6-address* ] **slow-peer**

For CE6885-LL (low latency mode):

**reset bgp ipv4** [ *ipv4-address* ] **slow-peer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *as-number* | Specifies a 2-byte AS number (number<1-65535>) or a 4-byte AS number (number<1-65535>.number<0-65535>). | For an integral AS number, the value ranges from 1 to 4294967295.  For an AS number in dotted notation, the value is in the format of x.y, where x and y are integers ranging from 1 to 65535 and from 0 to 65535, respectively. |
| *ipv4-address* | Resets the BGP connection with a specified peer. | It is in dotted decimal notation. |
| **external** | Reset all EBGP connections. | - |
| **internal** | Resets all IBGP connections. | - |
| **group** *group-name* | Resets BGP connections with the specified peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **ipv4** | Resets BGP IPv4 connections. | - |
| **all** | Reset all BGP connections. | - |
| *ipv6-address* | Resets the TCP connection with a specified BGP4+ peer (all the routes learned by using the connection are deleted). | The value is in the format of X:X:X:X:X:X:X:X. |
| **slow-peer** | Restores a slow peer connection to a normal peer connection. | - |
| **vpn-instance** *vpn-instance-name* | Resets the connection of a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. In addition, the VPN instance name must not be \_public\_. The character string can contain spaces if it is enclosed in double quotation marks (""). |
| **ipv4-family** | Indicates the IPv4 address family. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After BGP configurations change, you can run the **reset bgp** command to make the new configurations take effect immediately.If a device does not support route-refresh, you can run the **reset bgp** command to make the new BGP routing policy take effect after the BGP routing policy changes.You can run the **reset bgp ipv4 all** command to reset all BGP IPv4 connections of the public network.**reset bgp** *as-number*can reset only BGP connections on the public network. To reset BGP connections on a private network, specify a VPN instance.

**Configuration Impact**

This command resets all TCP connections established between BGP peers and therefore results in the re-establishment of the BGP peer relationships. Exercise caution when running this command.


Example
-------

# Reset all BGP connections.
```
<HUAWEI> reset bgp all

```