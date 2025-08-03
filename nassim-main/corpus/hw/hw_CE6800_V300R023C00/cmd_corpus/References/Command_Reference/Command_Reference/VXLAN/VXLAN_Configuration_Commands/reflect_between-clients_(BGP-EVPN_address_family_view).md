reflect between-clients (BGP-EVPN address family view)
======================================================

reflect between-clients (BGP-EVPN address family view)

Function
--------



The **reflect between-clients** command enables route reflection among clients.

The **undo reflect between-clients** command disables route reflection among clients. If the clients of an RR are fully meshed, you can disable route reflection between the clients to reduce the cost.



By default, route reflection among clients through the RR is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reflect between-clients**

**undo reflect between-clients**


Parameters
----------

None

Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On some networks, if the clients of an RR establish full-mesh connections with each other, they can directly exchange routing information. Route reflection among clients through the RR is unnecessary. The **undo reflect between-clients** command can be used to prohibit the clients from reflecting routes to each other to reduce costs.

**Prerequisites**

An RR has been configured.

**Precautions**

The **reflect between-clients** command is run only on RRs.


Example
-------

# Disable route reflection among fully-meshed clients through the RR in the BGP-EVPN address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 1.1.1.1 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 enable
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 reflect-client
[*HUAWEI-bgp-af-evpn] undo reflect between-clients

```