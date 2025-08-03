peer local-graceful-restart timer wait-for-rib(BGP multi-instance VPN instance view)
====================================================================================

peer local-graceful-restart timer wait-for-rib(BGP multi-instance VPN instance view)

Function
--------



The **peer local-graceful-restart timer wait-for-rib** command sets the maximum duration for a BGP restarter to wait for the End-of-RIB flag from a specified peer.

The **undo peer local-graceful-restart timer wait-for-rib** command deletes the configured duration.



By default, a BGP restarter waits for the End-of-RIB flag from a specified peer for a maximum of 600s.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**peer** *peerIpv4Addr* **local-graceful-restart** **timer** **wait-for-rib** *wfrtime*

**undo peer** *peerIpv4Addr* **local-graceful-restart** **timer** **wait-for-rib**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** *peerIpv6Addr* **local-graceful-restart** **timer** **wait-for-rib** *wfrtime*

**undo peer** *peerIpv6Addr* **local-graceful-restart** **timer** **wait-for-rib**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies an IPv4 peer address. | It is in dotted decimal notation. |
| *wfrtime* | Specifies the maximum duration for a BGP restarter to wait for the End-of-RIB flag. | The value is an integer ranging from 3 to 3000, in seconds. |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X |



Views
-----

BGP multi-instance VPN instance session view


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
[~HUAWEI] ip vpn-instance vpn
[*HUAWEI-vpn-instance-vpn] ipv4-family
[*HUAWEI-vpn-instance-vpn-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn] quit
[*HUAWEI] bgp 100 instance vpn1
[~HUAWEI-bgp-instance-vpn1] vpn-instance vpn
[*HUAWEI-bgp-instance-vpn1-instance-vpn] peer 10.1.1.2 as-number 100
[*HUAWEI-bgp-instance-vpn1-instance-vpn] peer 10.1.1.2 local-graceful-restart timer wait-for-rib 100

```