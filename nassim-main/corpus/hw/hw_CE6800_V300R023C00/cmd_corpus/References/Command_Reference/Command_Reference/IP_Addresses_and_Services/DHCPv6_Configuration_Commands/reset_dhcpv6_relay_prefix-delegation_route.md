reset dhcpv6 relay prefix-delegation route
==========================================

reset dhcpv6 relay prefix-delegation route

Function
--------



The **reset dhcpv6 relay prefix-delegation route** command deletes routing information learned from DHCPv6 PD terminals on a DHCPv6 relay agent.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset dhcpv6 relay prefix-delegation route** [ **vpn6-instance** *vpn-instance-name* ] *ipv6-address* *mask-length*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn6-instance** *vpn-instance-name* | Specifies the vpn6-instance name. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| *ipv6-address* | Specifies the destination IPv6 address of the routes to be deleted. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *mask-length* | Specifies the mask length. | It is an integer ranging from 0 to 128. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The **reset dhcpv6 relay prefix-delegation route** command is used on DHCPv6 relay agents. Before collecting routing information about a specified IPv6 address, run the **reset dhcpv6 relay prefix-delegation route** command to delete the existing routing information.


Example
-------

# Delete routing information with destination IPv6 address fc00:1::1 learned from DHCPv6 PD terminals.
```
<HUAWEI> reset dhcpv6 relay prefix-delegation route fc00:1::1 64

```