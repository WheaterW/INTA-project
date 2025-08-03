reset bgp evpn (IPv6)
=====================

reset bgp evpn (IPv6)

Function
--------



The **reset bgp evpn** command resets a specified BGP EVPN IPv6 connection.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset bgp evpn** *peerIpv6Addr*

**reset bgp instance** *bgpName* **evpn** *peerIpv6Addr*

**reset bgp evpn** *peerIpv6Addr* **slow-peer**

**reset bgp instance** *bgpName* **evpn** *peerIpv6Addr* **slow-peer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies a BGP EVPN peer IPv6 address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **instance** *bgpName* | Indicates BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters. If spaces are used, the string must be enclosed in double quotation marks (" "). |
| **slow-peer** | Slow peer. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To reset the BGP EVPN connection of a peer, run the **reset bgp evpn** command.

**Configuration Impact**

This command resets all TCP connections established between BGP EVPN IPv6 peers and therefore results in the re-establishment of BGP EVPN IPv6 peer relationships. Exercise caution when running this command.


Example
-------

# Reset specified BGP EVPN IPv6 connection.
```
<HUAWEI> reset bgp evpn 2001:db8:1::1

```