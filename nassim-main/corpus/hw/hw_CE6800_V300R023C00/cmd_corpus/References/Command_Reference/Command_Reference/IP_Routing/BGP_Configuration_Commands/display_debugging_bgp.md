display debugging bgp
=====================

display debugging bgp

Function
--------



The **display debugging bgp** command displays information about enabled BGP debugging functions.




Format
------

**display debugging bgp**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When a large amount of information is output, you can run the **display debugging bgp** command to view information about enabled BGP debugging functions and disable some unnecessary debugging functions to minimize the debugging information output.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about enabled debugging functions.
```
<HUAWEI> terminal debugging
<HUAWEI> debugging bgp packet all
<HUAWEI> display debugging bgp
[BGP] : Packet update send debugging switch is on
[BGP] : Packet update receive debugging switch is on
[BGP] : Packet keepalive send debugging switch is on
[BGP] : Packet keepalive receive debugging switch is on
[BGP] : Packet open send debugging switch is on
[BGP] : Packet open receive debugging switch is on
[BGP] : Packet route-refresh send debugging switch is on
[BGP] : Packet route-refresh receive debugging switch is on
<HUAWEI> debugging bgp packet open vpn-instance vrf1
<HUAWEI> display debugging bgp
[BGP] : Packet open send (VPN)vrf1 debugging switch is on
[BGP] : Packet open receive (VPN)vrf1 debugging switch is on
<HUAWEI> debugging bgp event peer 10.1.1.1
<HUAWEI> display debugging bgp
[BGP] : EVENT (VPN)_public_ (Peer) 10.1.1.1 debugging switch is on
<HUAWEI> debugging bgp packet update ipv4 unicast
<HUAWEI> display debugging bgp
[BGP] : Packet update send (VPN)_public_ IPv4-unicast debugging switch is on
[BGP] : Packet update receive (VPN)_public_ IPv4-unicast debugging switch is on

```

**Table 1** Description of the **display debugging bgp** command output
| Item | Description |
| --- | --- |
| Packet keepalive send debugging switch is on | BGP keepalive send debugging is enabled. |
| Packet keepalive receive debugging switch is on | BGP keepalive receive debugging is enabled. |
| Packet open send debugging switch is on | BGP open send debugging is enabled. |
| Packet open receive debugging switch is on | BGP open receive debugging is enabled. |
| Packet route-refresh send debugging switch is on | BGP route-refresh send debugging is enabled. |
| Packet route-refresh receive debugging switch is on | BGP route-refresh receive debugging is enabled. |
| Packet update send debugging switch is on | BGP update send debugging is enabled. |
| Packet update receive debugging switch is on | BGP update receive debugging is enabled. |
| Packet open send (VPN)vrf1 debugging switch is on | (VPN)vrf: Debugging is enabled for packets in a specified VPN instance. |
| EVENT (VPN)\_public\_ (Peer) 10.1.1.1 debugging switch is on | (VPN)\_public\_: indicates that the debugging of the public network is enabled.  peer 10.1.1.1: enables the debugging of the peer 10.1.1.1.  This field can also be displayed in other forms, for example:   * ipv4 unicast: Debugging is enabled for packets in the BGP-IPv4 unicast address family. * ipv6 unicast: Debugging is enabled for packets in the BGP-IPv6 unicast address family. * vpnv4: Debugging is enabled for packets in the BGP-VPNv4 address family. * vpnv6: Debugging is enabled for packets in the BGP-VPNv6 address family. |
| [BGP] | BGP debugging is enabled. |