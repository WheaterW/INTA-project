peer allow-cluster-loop (BGP-VPN-Target address family view)
============================================================

peer allow-cluster-loop (BGP-VPN-Target address family view)

Function
--------



The **peer allow-cluster-loop** command sets the maximum number of times the local cluster ID can be included in the Cluster\_List of each received route.

The **undo peer allow-cluster-loop** command does not allow the local cluster ID to be included in the Cluster\_List of each received route.



By default, the local cluster ID cannot be included in the Cluster\_List of each received route.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **allow-cluster-loop** [ *loop-number* ]

**undo peer** { *ipv4-address* | *ipv6-address* } **allow-cluster-loop**

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **allow-cluster-loop** [ *loop-number* ]

**undo peer** *ipv4-address* **allow-cluster-loop**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *loop-number* | Specifies the number of local AS number repetitions. | The value is an integer ranging from 1 to 10. The default value is 1. |



Views
-----

BGP-VPN-target address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

All PEs and RRs are in the same AS, and the BGP-EVPN and VPN-Target address families are enabled for the peers on all PEs and RRs. PE1 is the client of RR1, PE2 is the client of RR2, RRR is the level-2 reflector, and RR1 and RR2 are the clients of RR2. A private network with RT 1:1 is configured on PE1 and PE2. PE1 receives a private network route from CE1.In the case that the cluster ID loop of the reflector is not allowed: RR1 and RR2 advertise the RT routes received from PEs to the level-2 RRR. The level-2 RRR selects routes, for example, it selects the route from RR1, and advertises the route to RR1 and RR2, respectively. However, the RR cluster list carried by RR1 contains the cluster ID of the local RR. Therefore, the VPN ORF route is discarded. As a result, RR1 does not have the RT filter of RRR and cannot instruct the BGP EVPN peer to advertise routes. As a result, CE2 cannot learn routes from CE1. In this case, you need to run the **peer allow-cluster-loop** command in the VPN ORF address family view of RR1 for the peer RRR so that RR1 can receive RT routes advertised by the level-2 RRR and guide route advertisement to BGP EVPN peers.


Example
-------

# Set the maximum number of times the local cluster ID can be included in the Cluster\_List of each received route to 1.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.2.2.2 as-number 100
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer 10.2.2.2 enable
[*HUAWEI-bgp-af-vpn-target] peer 10.2.2.2 allow-cluster-loop 1

```