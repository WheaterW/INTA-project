reflector cluster-id (BGP view)
===============================

reflector cluster-id (BGP view)

Function
--------



The **reflector cluster-id** command sets a cluster ID for an RR.

The **undo reflector cluster-id** command deletes the cluster ID configured for an RR.



By default, each RR uses its Router ID as the cluster ID.


Format
------

**reflector cluster-id** { *cluster-id-value* | *cluster-id-ipv4* }

**undo reflector cluster-id**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cluster-id-value* | Specifies the IPv4 address of an RR. | The value is an integer ranging from 1 to 4294967295. |
| *cluster-id-ipv4* | Specifies the IPv4 address of an RR. | The value is in dotted decimal notation. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Sometimes, more than one RR needs to be configured in a cluster to improve network reliability and prevent single-point failures. If a cluster has more than one RR, the **reflector cluster-id** command needs to be used to set the same cluster ID for the RRs. This helps to identify the cluster and avoid routing loops.Configuring an RR allows IBGP peers to advertise routes learned in the local AS to each other. The Cluster\_List attribute is introduced to avoid loops within an AS. The Cluster\_List is composed of a series of Cluster\_IDs. It records all the RRs through which a route passes.

**Precautions**

To ensure that clients can learn routes from the RR, the cluster ID configured on the RR must not be the same as the cluster IDs of the clients. By default, the clients use their own router IDs as their cluster IDs. If the cluster IDs are the same, the clients discard the received routes.This command takes effect in the BGP-IPv4 unicast address family view.


Example
-------

# Configure the local device as one of the RRs in the cluster and set the cluster ID to 50.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] reflector cluster-id 50

```