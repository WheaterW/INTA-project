c-multicast signaling
=====================

c-multicast signaling

Function
--------



The **c-multicast signaling** command configures the signaling protocol for transmitting C-multicast routes.

The **undo c-multicast signaling** command deletes the signaling protocol for transmitting C-multicast routes.



By default, no signaling protocol is configured for transmitting C-multicast routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**c-multicast signaling bgp**

**undo c-multicast signaling**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **bgp** | Specifies BGP as the signaling protocol for transmitting C-multicast routes. | - |



Views
-----

VPN instance IPv4 address family MVPN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a Next Generation Multicast Virtual Private Network (NG MVPN) network, after a receiver PE receives a PIM Join/Prune message or an IGMP Join message, the receiver PE converts the message to a C-multicast route and sends the C-multicast route to a sender PE. To configure the signaling protocol for transmitting C-multicast routes, run the **c-multicast signaling** command.

**Precautions**

Only BGP can be used as the signaling protocol for transmitting C-multicast routes.


Example
-------

# Configure BGP as the signaling protocol for transmitting C-multicast routes.
```
<HUAWEI> system-view
[~HUAWEI] multicast mvpn 2.2.2.2
[*HUAWEI] ip vpn-instance mcast1
[*HUAWEI-vpn-instance-mcast1] ipv4-family
[*HUAWEI-vpn-instance-mcast1-af-ipv4] route-distinguisher 22:1
[*HUAWEI-vpn-instance-mcast1-af-ipv4] multicast routing-enable
[*HUAWEI-vpn-instance-mcast1-af-ipv4] mvpn
[*HUAWEI-vpn-instance-mcast1-af-ipv4-mvpn] c-multicast signaling bgp

```