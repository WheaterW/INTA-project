peer generate-link-bandwidth (BGP-IPv6 unicast address family view)
===================================================================

peer generate-link-bandwidth (BGP-IPv6 unicast address family view)

Function
--------



The **peer generate-link-bandwidth** command configures the local device to obtain the link bandwidth of a specified directly connected EBGP peer and generate an extended community attribute.

The **undo peer generate-link-bandwidth** command cancels the existing configuration.



By default, the local device is disabled from obtaining the link bandwidth of a specified directly connected EBGP peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** { *peerIpv4Addr* | *peerIpv6Addr* } **generate-link-bandwidth**

**peer** { *peerIpv4Addr* | *peerIpv6Addr* } **generate-link-bandwidth** **disable**

**undo peer** { *peerIpv4Addr* | *peerIpv6Addr* } **generate-link-bandwidth**

**undo peer** { *peerIpv4Addr* | *peerIpv6Addr* } **generate-link-bandwidth** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **disable** | Disables a device to obtaining the bandwidth of directly connected EBGP neighbor interfaces. | - |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the actual link bandwidth needs to be obtained and dynamically updated based on the actual bandwidth when routes are available for load balancing, run the **peer generate-link-bandwidth** command to obtain the link bandwidth of directly connected EBGP peer, generate the extended community attribute, and update route information.After a peer is added to a peer group, if the local device is enabled to obtain the link bandwidth of directly connected EBGP peers for the peer group, the peer inherits the configuration of the peer group. If the peer does not need to inherit the configuration of the peer group, disable the function of obtaining the link bandwidth of the directly connected EBGP peer.

**Precautions**

If the peer connect-interface, peer ebgp-max-hop, or ttl command is not run, you can run the **peer generate-link-bandwidth** command to obtain the link bandwidth of the directly connected EBGP peer.


Example
-------

# Configure the local device to obtain the link bandwidth of a specified directly connected EBGP peer and generate an extended community attribute.
```
<HUAWEI> system
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.2.1 as-number 200
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer 10.1.2.1 enable
[*HUAWEI-bgp-af-ipv6] peer 10.1.2.1 generate-link-bandwidth

```