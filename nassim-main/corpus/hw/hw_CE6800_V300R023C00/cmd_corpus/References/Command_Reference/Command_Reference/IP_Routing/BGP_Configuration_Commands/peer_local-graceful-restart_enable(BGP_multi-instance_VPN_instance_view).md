peer local-graceful-restart enable(BGP multi-instance VPN instance view)
========================================================================

peer local-graceful-restart enable(BGP multi-instance VPN instance view)

Function
--------



The **peer local-graceful-restart enable** command enables local GR for a specified peer.

The **peer local-graceful-restart disable** command disables local GR for a specified peer.



By default, local GR is not enabled for a peer specified on a device.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**peer** *peerIpv4Addr* **local-graceful-restart** **enable**

**peer** *peerIpv4Addr* **local-graceful-restart** **disable**

**undo peer** *peerIpv4Addr* **local-graceful-restart** **enable**

**undo peer** *peerIpv4Addr* **local-graceful-restart** **disable**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** *peerIpv6Addr* **local-graceful-restart** **enable**

**peer** *peerIpv6Addr* **local-graceful-restart** **disable**

**undo peer** *peerIpv6Addr* **local-graceful-restart** **enable**

**undo peer** *peerIpv6Addr* **local-graceful-restart** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a BGP peer. | The value is in dotted decimal notation. |
| *peerIpv6Addr* | Specifies the IPv6 address of a BGP peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a device supports GR but a BGP peer specified on the device does not support GR, you can run the peer local-graceful-restart enable command on the device to enable local GR for the peer. This configuration ensures that the device does not delete the routes received from the peer and related forwarding entries before the GR time elapses, thereby preventing traffic interruption.


Example
-------

# Enable local GR for a specified peer on a device.
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
[*HUAWEI-bgp-instance-a-instance-vpn1] peer 10.1.1.1 local-graceful-restart enable

```