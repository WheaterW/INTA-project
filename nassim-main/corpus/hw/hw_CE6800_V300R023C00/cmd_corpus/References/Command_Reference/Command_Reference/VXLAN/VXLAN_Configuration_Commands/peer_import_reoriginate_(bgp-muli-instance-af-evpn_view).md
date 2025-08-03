peer import reoriginate (bgp-muli-instance-af-evpn view)
========================================================

peer import reoriginate (bgp-muli-instance-af-evpn view)

Function
--------



The **peer import reoriginate** command enables a device to add a regeneration flag to the routes received from BGP multi-instance EVPN peers.

The **undo peer import reoriginate** command restores the default configuration.



By default, a device does not add a regeneration flag to the routes received from BGP multi-instance EVPN peers.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** { *peerIpv4Addr* | *peerIpv6Addr* } **import** **reoriginate**

**undo peer** { *peerIpv4Addr* | *peerIpv6Addr* } **import** **reoriginate**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a BGP EVPN peer. | The value is in dotted decimal notation. |
| *peerIpv6Addr* | Specifies the IPv6 address of a BGP EVPN peer. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

DCI enables inter-DC VM communication. It uses technologies, such as VXLAN and BGP EVPN, to securely and reliably transmit packets from DCs over carrier networks.In a segment VXLAN scenario for DCI, an edge node that connects to a carrier network does not re-encapsulate the routes received from BGP EVPN peers, causing the EVPN routes to be terminated on the edge node. As a result, the EVPN routes from one DC cannot be advertised to the BGP EVPN peers of another DC. To address this problem, run the **peer import reoriginate** command to enable the edge node to add a regeneration flag to the routes received from BGP EVPN peers. The edge node then re-encapsulates the EVPN routes received from one DC before sending them to another DC for inter-DC VM communication.


Example
-------

# Configure the device to add the regeneration flag to the routes to be received from a BGP multi-instance EVPN peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance evrf
[*HUAWEI-bgp-instance-evrf] peer 1.1.1.1 as-number 100
[*HUAWEI-bgp-instance-evrf] l2vpn-family evpn
[*HUAWEI-bgp-instance-evrf-af-evpn] peer 1.1.1.1 enable
[*HUAWEI-bgp-instance-evrf-af-evpn] peer 1.1.1.1 import reoriginate

```