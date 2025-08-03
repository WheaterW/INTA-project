display bgp instance vpnv6 vpn-instance routing-table peer statistics
=====================================================================

display bgp instance vpnv6 vpn-instance routing-table peer statistics

Function
--------



The display bgp instance vpnv6 vpn-instance routing-table peer advertised-routes statistics command displays statistics about routes advertised to a specified peer in the BGP multi-instance VPN instance IPv6 address family.

The display bgp instance vpnv6 vpn-instance routing-table peer received-routes statistics command displays statistics about routes received from a specified peer in the BGP multi-instance VPN instance IPv6 address family.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp instance** *bgpName* **vpnv6** **vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv6Addr* **advertised-routes** **statistics**

**display bgp instance** *bgpName* **vpnv6** **vpn-instance** *vpn-instance-name* **routing-table** **peer** *remoteIpv6Addr* **received-routes** [ **active** ] **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specify a VPN-Instance (VRF) name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *remoteIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |
| **active** | Displays the active routes learned from a specified peer. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp instance vpnv6 vpn-instance routing-table peer advertised-routes statistics** command displays statistics about routes advertised to a specified peer in the BGP multi-instance VPN instance IPv6 address family.The **display bgp instance vpnv6 vpn-instance routing-table peer received-routes statistics** command displays statistics about routes received from a specified peer in the BGP multi-instance VPN instance IPv6 address family.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about BGP multi-instance VPNv6 routes advertised to a specified peer.
```
<HUAWEI> display bgp instance a vpnv6 vpn-instance  vrf2 routing-table peer 2001:db8:1::1 advertised-routes statistics

 Advertised routes total: 2
 
 Default originated : 0

```

# Display statistics about BGP multi-instance VPNv6 routes received from a specified peer.
```
<HUAWEI> display bgp instance a vpnv6 vpn-instance  vrf2 routing-table peer 2001:db8:1::1 received-routes statistics

 Received routes total: 1

```

**Table 1** Description of the **display bgp instance vpnv6 vpn-instance routing-table peer statistics** command output
| Item | Description |
| --- | --- |
| Advertised routes total | Total number of advertised routes. |
| Default originated | Total number of Default originated. |
| Received routes total | Total number of received routes. |