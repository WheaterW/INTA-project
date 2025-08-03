default med (BGP multi-instance VPN instance IPv4 address family view)
======================================================================

default med (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **default med** command configures a MED for BGP routes.

The **undo default med** command restores the default value.



By default, the MED value of a route imported from OSPF is the cost value of the imported route plus one; for other imported routes, the MED values are their cost values; the MED value of a route learned from a peer is the MED value of the route sent by the peer.


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

BGP multi-instance VPN instance IPv4 address family view


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
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vrf1
[*HUAWEI-bgp-instance-a-vrf1] default med 10

```