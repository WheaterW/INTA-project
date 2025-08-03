peer graceful-shutdown manual-activate(BGP-VPN instance IPv4 address family view)(IPv4)
=======================================================================================

peer graceful-shutdown manual-activate(BGP-VPN instance IPv4 address family view)(IPv4)

Function
--------



The **peer graceful-shutdown manual-activate** command activates the g-shut function for a specified peer.

The **undo peer graceful-shutdown manual-activate** command restores the default configuration.



By default, the g-shut function of a peer is not activated.


Format
------

**peer** *peerIpv4Addr* **graceful-shutdown** **manual-activate**

**peer** *peerIpv4Addr* **graceful-shutdown** **manual-activate** **disable**

**undo peer** *peerIpv4Addr* **graceful-shutdown** **manual-activate**

**undo peer** *peerIpv4Addr* **graceful-shutdown** **manual-activate** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| **disable** | Deactivates the g-shut feature of a peer. The difference between this parameter and the undo command is that this parameter enables the device not to inherit the g-shut activation status of a peer group. | - |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



You can run this command to activate the g-shut feature for a single peer.




Example
-------

# Activate the g-shut function for a specified peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-vpn1] peer 10.1.1.1 graceful-shutdown manual-activate

```