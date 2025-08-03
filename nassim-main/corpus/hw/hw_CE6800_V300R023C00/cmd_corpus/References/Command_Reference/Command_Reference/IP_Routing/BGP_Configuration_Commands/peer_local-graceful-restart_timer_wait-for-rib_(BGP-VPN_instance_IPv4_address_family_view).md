peer local-graceful-restart timer wait-for-rib (BGP-VPN instance IPv4 address family view)
==========================================================================================

peer local-graceful-restart timer wait-for-rib (BGP-VPN instance IPv4 address family view)

Function
--------



The **peer local-graceful-restart timer wait-for-rib** command sets the maximum duration for a BGP restarter to wait for the End-of-RIB flag from a specified peer.

The **undo peer local-graceful-restart timer wait-for-rib** command deletes the configured duration.



By default, a BGP restarter waits for the End-of-RIB flag from a specified peer for a maximum of 600s.


Format
------

**peer** *ipv4-address* **local-graceful-restart** **timer** **wait-for-rib** *wfrtime*

**undo peer** *ipv4-address* **local-graceful-restart** **timer** **wait-for-rib**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *wfrtime* | Specifies the maximum duration for a BGP restarter to wait for the End-of-RIB flag. | The value is an integer ranging from 3 to 3000, in seconds. |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a device supports GR but a BGP peer specified on the device does not support GR, you can run the peer local-graceful-restart timer wait-for-rib command to set the maximum duration for the device to wait for the End-of-RIB flag from the peer. After the BGP session between the device and the peer is reestablished, if the device does not receive the End-of-RIB flag within the specified duration, the BGP session on the device exits from the GR process and the device selects the optimal route among reachable routes.


Example
-------

# Set the maximum duration during which a BGP restarter waits for the End-of-RIB flag from a specified peer to 100s.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] peer 10.1.1.2 as-number 100
[*HUAWEI-bgp-vpn1] peer 10.1.1.2 local-graceful-restart timer wait-for-rib 100

```