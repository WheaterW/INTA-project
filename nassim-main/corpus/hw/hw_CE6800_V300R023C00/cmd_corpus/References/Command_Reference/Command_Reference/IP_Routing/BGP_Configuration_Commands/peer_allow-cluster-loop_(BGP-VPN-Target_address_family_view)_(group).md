peer allow-cluster-loop (BGP-VPN-Target address family view) (group)
====================================================================

peer allow-cluster-loop (BGP-VPN-Target address family view) (group)

Function
--------



The **peer allow-cluster-loop** command sets the maximum number of times the local cluster ID can be included in the Cluster\_List of each received route.

The **undo peer allow-cluster-loop** command does not allow the local cluster ID to be included in the Cluster\_List of each received route.



By default, the local cluster ID cannot be included in the Cluster\_List of each received route.


Format
------

**peer** *group-name* **allow-cluster-loop** [ *loop-number* ]

**undo peer** *group-name* **allow-cluster-loop**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *loop-number* | Specifies the number of local AS number repetitions. | The value is an integer ranging from 1 to 10. The default value is 1. |



Views
-----

BGP-VPN-target address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



All PEs and RRs are in the same AS, and the BGP-EVPN and VPN-Target address families are enabled for the peers on all PEs and RRs. PE1 is the client of RR1, PE2 is the client of RR2, RRR is the level-2 reflector, and RR1 and RR2 are the clients of RR2. A private network with RT 1:1 is configured on PE1 and PE2. PE1 receives a private network route from CE1.In the case that the cluster ID loop of the reflector is not allowed: RR1 and RR2 advertise the RT routes received from PEs to the level-2 RRR. The level-2 RRR selects routes, for example, it selects the route from RR1, and advertises the route to RR1 and RR2, respectively. However, the RR cluster list carried by RR1 contains the cluster ID of the local RR. Therefore, the VPN ORF route is discarded. As a result, RR1 does not have the RT filter of RRR and cannot instruct the BGP EVPN peer to advertise routes. As a result, CE2 cannot learn routes from CE1. In this case, you need to run the **peer allow-cluster-loop** command in the VPN ORF address family view of RR1 for the peer RRR so that RR1 can receive RT routes advertised by the level-2 RRR and guide route advertisement to BGP EVPN peers.




Example
-------

# Set the maximum number of times the local cluster ID can be included in the Cluster\_List of each received route to 1.
```
<HUAWEI> system-view
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test internal
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer test enable
[*HUAWEI-bgp-af-vpn-target] peer test allow-cluster-loop 1

```