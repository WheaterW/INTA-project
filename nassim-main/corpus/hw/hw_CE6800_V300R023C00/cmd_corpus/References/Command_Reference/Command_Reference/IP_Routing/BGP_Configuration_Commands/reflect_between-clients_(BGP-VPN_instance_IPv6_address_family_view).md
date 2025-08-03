reflect between-clients (BGP-VPN instance IPv6 address family view)
===================================================================

reflect between-clients (BGP-VPN instance IPv6 address family view)

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

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On some networks, if the clients of an RR establish full-mesh connections with each other, they can directly exchange routing information. Route reflection among clients through the RR is unnecessary. The **undo reflect between-clients** command can be used to prohibit the clients from reflecting routes to each other to reduce costs.

**Prerequisites**

An RR has been configured.

**Configuration Impact**

After the **undo reflect between-clients** command is run, the clients of an RR are prohibited from reflecting routes.

**Precautions**

The **reflect between-clients** command is run only on RRs.


Example
-------

# Displays routes with the large-community attribute.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] reflect between-clients

```