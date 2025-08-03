peer log-change (BGP-VPN instance IPv4 address family view)
===========================================================

peer log-change (BGP-VPN instance IPv4 address family view)

Function
--------



The **peer log-change** command enables a BGP device to log the session status and events of a specified peer or a peer.

The **undo peer log-change** command cancels the configuration.



By default, a BGP device is enabled to log the session status and events of a specified peer.


Format
------

**peer** *ipv4-address* **log-change**

**undo peer** *ipv4-address* **log-change**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The **peer log-change** command can be used to enable a device to log the session status and events of a specified peer, facilitating service management.


Example
-------

# Configure a BGP device to log the session status and events of peer.
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
[*HUAWEI-bgp-vpn1] peer 10.1.1.1 log-change

```