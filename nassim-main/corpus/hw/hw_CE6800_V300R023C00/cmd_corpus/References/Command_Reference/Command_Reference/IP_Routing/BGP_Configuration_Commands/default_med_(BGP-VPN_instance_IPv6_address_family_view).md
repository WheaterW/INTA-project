default med (BGP-VPN instance IPv6 address family view)
=======================================================

default med (BGP-VPN instance IPv6 address family view)

Function
--------



The **default med** command configures a MED for BGP routes.

The **undo default med** command restores the default value.



By default, the MED value of a route imported from OSPF is the cost value of the imported route plus one; for other imported routes, the MED values are their cost values; the MED value of a route learned from a peer is the MED value of the route sent by the peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**default med** *med*

**undo default med**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *med* | Specifies the MED for BGP routes. | The value is an integer ranging from 0 to 4294967295. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **default med** command is valid only for the routes imported using the **import-route** command and BGP summary routes on the local device.The **default med** command configures a default MED value for the routes to be advertised to common EBGP peers or confederation EBGP peers so that the optimal route can be selected based on the MED for the traffic that enters an AS. With other conditions being the same, the route with the smallest MED value is selected as the optimal route.

**Configuration Impact**

If more than one MED is configured for BGP routes, the latest configuration overrides the previous one.

**Precautions**

The MED attribute is transmitted only between two neighboring ASs. The AS that receives the MED attribute does not advertise it to a third AS.


Example
-------

# Set the MED of BGP routes to 10.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] default med 10

```