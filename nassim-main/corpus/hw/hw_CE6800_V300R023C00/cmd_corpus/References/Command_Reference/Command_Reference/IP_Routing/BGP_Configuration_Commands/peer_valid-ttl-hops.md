peer valid-ttl-hops
===================

peer valid-ttl-hops

Function
--------



The **peer valid-ttl-hops** command applies the GTSM on a BGP peer or a BGP peer group.

The **undo peer valid-ttl-hops** command cancels the GTSM configured on a BGP peer or a BGP peer group.



By default, GTSM is not configured on any BGP peer or peer group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **valid-ttl-hops** [ *hops* ]

**undo peer** *ipv6-address* **valid-ttl-hops**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The value is in the format of X:X:X:X:X:X:X:X. |
| *hops* | Specifies the number of TTL hops to be checked. | The value is an integer that ranges from 1 to 255. The default value is 255. If you specify the parameter hops, the valid range of the TTL value in the packet to be checked is [ 255-hops+1, 255 ]. |



Views
-----

BGP view


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

When this command is used in the BGP view, it is also applicable to MP-BGP extensions because they use the same TCP connection.The GTSM configurations are symmetrical, that is, GTSM must be enabled on both ends of the BGP connection.GTSM and EBGP-MAX-HOP are mutually exclusive because both of them affect the TTL of the sent BGP messages. Therefore, only one of the two functions can be enabled on a peer or peer group.If GTSM is enabled on two directly connected EBGP peers, the fast sensing function on the interfaces directly connecting the EBGP peers is invalid. This is because BGP regards the EBGP peers as indirectly connected when GTSM is enabled on the EBGP peers.


Example
-------

# Configure GTSM for a peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 200
[*HUAWEI-bgp] peer 2001:DB8:1::1 valid-ttl-hops 1

```