peer bfd enable (BGP multi-instance VPN instance view)
======================================================

peer bfd enable (BGP multi-instance VPN instance view)

Function
--------



The **peer bfd enable** command enables a device to establish a BFD session with its peer using default detection parameter values.

The **undo peer bfd enable** command cancels this function.



By default, a BGP device does not establish any BFD session with its peer.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**peer** *peerIpv4Addr* **bfd** **enable** [ **single-hop-prefer** ] [ **compatible** ]

**peer** *peerIpv4Addr* **bfd** **enable** **per-link** **one-arm-echo**

**peer** *peerIpv4Addr* **bfd** **enable** **one-arm-echo**

**undo peer** *peerIpv4Addr* **bfd** **enable**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** *peerIpv6Addr* **bfd** **enable** [ [ **single-hop-prefer** ] [ **compatible** ] ]

**peer** *peerIpv6Addr* **bfd** **enable** **per-link** **one-arm-echo**

**peer** *peerIpv6Addr* **bfd** **enable** **one-arm-echo**

**undo peer** *peerIpv6Addr* **bfd** **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| **single-hop-prefer** | Preferentially creates a single-hop BFD session for BGP peers. | - |
| **compatible** | Indicates the compatibility mode. If this keyword is specified, the TTL in packets sent by BFD is set to 255. | - |
| **per-link** | Preferentially creates a single-hop BFD session for BGP peers. | - |
| **one-arm-echo** | Indicates a one-arm BFD echo session. | - |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The address is in the format of X:X:X:X:X:X:X:X. |



Views
-----

BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

BGP uses BFD to quickly detect faults in links between BGP peers. This accelerates network convergence. You can run this command to create a BFD session with default detection parameters for a peer or peer group.If single-hop-prefer is specified, single-hop detection is preferentially used when a BFD session is established between BGP peers. This parameter is used to detect IP connectivity between BGP peers. That is, only one BFD session exists on a specified BGP interface. This parameter is used to ensure that the local and peer ends use the same detection mode when a Huawei device is connected to a non-Huawei device.The per-link one-arm-echo parameter enables one-arm BFD echo for each link. This parameter ensures that the local and peer ends use the same detection mode when a Huawei device is connected to a non-Huawei device.After a peer is added to a peer group, the peer inherits the BFD configuration of the peer group regardless of whether BFD is enabled on the peer. If the peer does not need to inherit the configuration of the peer group, run the **peer bfd block** command on the peer to prevent the peer from inheriting the BFD function of the peer group.If neither single-hop-prefer nor compatible is specified, the multi-hop mode is used by default when a BFD session is established between BGP peers, and the TTL value in BFD packets is 253 by default.


Example
-------

# Configure BFD for a peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] vpn-instance vpna
[*HUAWEI-bgp-instance-a-instance-vpna] peer 192.168.1.1 as-number 100
[*HUAWEI-bgp-instance-a-instance-vpna] peer 192.168.1.1 bfd enable

```