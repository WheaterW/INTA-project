peer local-graceful-restart timer restart(BGP multi-instance VPN instance view)(IPv4)
=====================================================================================

peer local-graceful-restart timer restart(BGP multi-instance VPN instance view)(IPv4)

Function
--------



The **peer local-graceful-restart timer restart** command sets the maximum duration for a device to wait for the BGP peer relationship with a specified peer to be reestablished. After this command is run, the device will not advertise the maximum duration to the specified peer.

The **undo peer local-graceful-restart timer restart** command deletes the configured duration.



By default, a device waits for the peer relationship with a peer to be reestablished for a maximum of 150 seconds.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**peer** *peerIpv4Addr* **local-graceful-restart** **timer** **restart** *restart-time*

**undo peer** *peerIpv4Addr* **local-graceful-restart** **timer** **restart**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** *peerIpv6Addr* **local-graceful-restart** **timer** **restart** *restart-time*

**undo peer** *peerIpv6Addr* **local-graceful-restart** **timer** **restart**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a BGP peer. | The value is in dotted decimal notation. |
| *restart-time* | Specifies the maximum duration for a device to wait for the GR recovery of a specified peer. | The value is an integer that ranges from 3 to 3600, in seconds. |
| *peerIpv6Addr* | Specifies the IPv6 address of a BGP peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If the local device supports GR but the specified peer does not support GR, you can run this command to set the maximum waiting time for the local device to wait for the re-establishment of the BGP peer relationship.After the **peer local-graceful-restart timer restart** command is run, if the local end finds that the peer group is Down, the BGP session enters the GR process. The local end must establish a connection with the peer group within the configured maximum waiting time. Otherwise, the local end selects the optimal route from the existing routes.


Example
-------

# Set the maximum duration to 250 seconds for a device to wait for the peer relationship with a specified peer to be reestablished.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] vpn-instance vpn1
[*HUAWEI-bgp-instance-a-instance-vpn1] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-a-instance-vpn1] peer 10.1.1.1 local-graceful-restart timer restart 250

```