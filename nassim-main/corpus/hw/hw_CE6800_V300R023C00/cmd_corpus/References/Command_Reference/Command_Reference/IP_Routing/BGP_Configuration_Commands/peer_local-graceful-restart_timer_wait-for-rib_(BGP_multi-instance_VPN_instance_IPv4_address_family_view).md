peer local-graceful-restart timer wait-for-rib (BGP multi-instance VPN instance IPv4 address family view)
=========================================================================================================

peer local-graceful-restart timer wait-for-rib (BGP multi-instance VPN instance IPv4 address family view)

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
| *ipv4-address* | Specifies the IPv4 address of a BGP peer. | The value is in dotted decimal notation. |
| *wfrtime* | Specifies the maximum duration for a BGP restarter to wait for the End-of-RIB flag. | The value is an integer ranging from 3 to 3000, in seconds. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If a device supports GR but a BGP peer specified on the device does not support GR, you can run the peer local-graceful-restart timer wait-for-rib command to set the maximum duration for the device to wait for the End-of-RIB flag from the peer. After the BGP session between the device and the peer is reestablished, if the device does not receive the End-of-RIB flag within the specified duration, the BGP session on the device exits from the GR process and the device selects the optimal route among reachable routes.




Example
-------

# Set the maximum duration for a device to wait for the End-of-RIB flag from a specified peer to 100s.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100 instance vpn1
[~HUAWEI-bgp-instance-vpn1] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1-vpn1] peer 10.1.1.2 as-number 100
[*HUAWEI-bgp-instance-vpn1-vpn1] peer 10.1.1.2 local-graceful-restart timer wait-for-rib 100

```