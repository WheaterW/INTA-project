peer log-change (BGP-VPN instance view)
=======================================

peer log-change (BGP-VPN instance view)

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
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The **peer log-change** command can be used to enable a device to log the session status and events of a specified peer, facilitating service management.


Example
-------

# Configure a BGP device to log the session status and events of peer 10.1.1.2.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] peer 10.1.1.2 as-number 200
[*HUAWEI-bgp-instance-vpn1] peer 10.1.1.2 log-change

```