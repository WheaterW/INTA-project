peer local-graceful-restart timer wait-for-rib (BGP-VPN instance IPv6 address family view) (IPv6)
=================================================================================================

peer local-graceful-restart timer wait-for-rib (BGP-VPN instance IPv6 address family view) (IPv6)

Function
--------



The **peer local-graceful-restart timer wait-for-rib** command sets the maximum duration for a BGP restarter to wait for the End-of-RIB flag from a specified peer.

The **undo peer local-graceful-restart timer wait-for-rib** command deletes the configured duration.



By default, a BGP restarter waits for the End-of-RIB flag from a specified peer for a maximum of 600s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **local-graceful-restart** **timer** **wait-for-rib** *wfrtime*

**undo peer** *ipv6-address* **local-graceful-restart** **timer** **wait-for-rib**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *wfrtime* | Specifies the maximum duration for waiting for the End-Of-RIB flag. | The value is an integer ranging from 3 to 3000, in seconds. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a device supports GR but a BGP peer specified on the device does not support GR, you can run the peer local-graceful-restart timer wait-for-rib command to set the maximum duration for the device to wait for the End-of-RIB flag from the peer. After the BGP session between the device and the peer is reestablished, if the device does not receive the End-of-RIB flag within the specified duration, the BGP session on the device exits from the GR process and the device selects the optimal route among reachable routes.


Example
-------

# Set the maximum duration for a device to wait for the End-of-RIB flag from a specified peer to 100s.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpn1
[*HUAWEI-bgp-6-vpn1] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp-6-vpn1] peer 2001:DB8:1::1 local-graceful-restart timer wait-for-rib 100

```