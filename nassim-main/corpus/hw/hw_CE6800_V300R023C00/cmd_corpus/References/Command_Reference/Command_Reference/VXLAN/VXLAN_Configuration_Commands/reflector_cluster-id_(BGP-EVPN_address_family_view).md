reflector cluster-id (BGP-EVPN address family view)
===================================================

reflector cluster-id (BGP-EVPN address family view)

Function
--------



The **reflector cluster-id** command sets a cluster ID for an RR.

The **undo reflector cluster-id** command deletes the cluster ID configured for an RR.



By default, each RR uses its router ID as the cluster ID.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reflector cluster-id** { *cluster-id-value* | *cluster-id-ipv4* }

**undo reflector cluster-id**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cluster-id-value* | Specifies the cluster ID of an RR. | The value is an integer ranging from 1 to 4294967295. |
| *cluster-id-ipv4* | Specifies the IPv4 address of an RR. | The value is in dotted decimal notation. |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Sometimes, more than one RR needs to be configured in a cluster to improve network reliability and prevent a single point of failure (SPOF). If a cluster has more than one RR, the **reflector cluster-id** command needs to be used to set the same cluster ID for the RRs. This helps to identify the cluster and avoid routing loops.Configuring an RR allows IBGP peers to advertise routes learned in the local AS to each other. The Cluster\_List attribute is introduced to avoid loops within an AS. The Cluster\_List is composed of a series of Cluster\_IDs, and records all the RRs through which a route passes.

**Configuration Impact**

If the **reflector cluster-id** command is run several times, the latest configuration overrides the previous one.

**Precautions**

To ensure that a client can learn the routes reflected by an RR, the Cluster ID configured on the RR must be different from the Cluster ID of the client (By default, the client uses its Router ID as the cluster ID). If the Cluster ID is the same as the Cluster ID of the client, the client discards received routes.


Example
-------

# Set the cluster ID to 50 in the BGP-EVPN address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 1.1.1.1 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 enable
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 reflect-client
[*HUAWEI-bgp-af-evpn] reflector cluster-id 50

```