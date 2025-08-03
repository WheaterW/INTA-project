peer valid-ttl-hops (BGP multi-instance view)
=============================================

peer valid-ttl-hops (BGP multi-instance view)

Function
--------



The **peer valid-ttl-hops** command applies the GTSM on a BGP peer or a BGP peer group.

The **undo peer valid-ttl-hops** command cancels the GTSM configured on a BGP peer or a BGP peer group.



By default, GTSM is not configured on any BGP peer or peer group.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **valid-ttl-hops** [ *hops* ]

**undo peer** { *ipv4-address* | *ipv6-address* } **valid-ttl-hops**

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **valid-ttl-hops** [ *hops* ]

**undo peer** *ipv4-address* **valid-ttl-hops**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *hops* | Specifies the number of TTL hops to be checked. | The value is an integer that ranges from 1 to 255. The default value is 255. If you specify the parameter hops, the valid range of the TTL value in the packet to be checked is [ 255-hops+1, 255 ]. |
| **peer** *ipv4-address* | Specifies the IPv4 address of a BGP peer. | It is in dotted decimal notation. |
| **peer** *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To protect a device against the attacks by the forged BGP packets, you can configure GTSM to check whether the TTL value in the IP packet header is within the valid range.

**Prerequisites**

Before configuring GTSM for a peer group, you need to run the **peer group** command to add peers to the peer group.

**Precautions**

When this command is used in the BGP view, it is also applicable to MP-BGP extensions because they use the same TCP connection.The GTSM configurations are symmetrical, that is, GTSM must be enabled on both ends of the BGP connection at the same time.GTSM and EBGP-MAX-HOP are mutually exclusive because both of them affect the TTL of the sent BGP packet. Therefore, the two functions cannot be enabled on a peer or peer group simultaneously.If GTSM is enabled on two directly connected EBGP peers, the fast sensing function on the interfaces directly connecting the EBGP peers is invalid. This is because BGP regards the EBGP peers as indirectly connected when GTSM is enabled on the EBGP peers.


Example
-------

# Configure GTSM for a peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] peer 10.1.1.2 as-number 200
[*HUAWEI-bgp-instance-a] peer 10.1.1.2 valid-ttl-hops 1

```