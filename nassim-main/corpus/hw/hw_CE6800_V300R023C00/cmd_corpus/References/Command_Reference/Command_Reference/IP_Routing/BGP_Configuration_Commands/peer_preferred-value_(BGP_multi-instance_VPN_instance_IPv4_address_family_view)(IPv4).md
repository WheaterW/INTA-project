peer preferred-value (BGP multi-instance VPN instance IPv4 address family view)(IPv4)
=====================================================================================

peer preferred-value (BGP multi-instance VPN instance IPv4 address family view)(IPv4)

Function
--------



The **peer preferred-value** command sets a preferred value for the routes that a BGP device learns from its peer.

The **undo peer preferred-value** command deletes the preferred value set for the routes that a BGP device learns from its peer.



By default, the preferred value of a route learned from a BGP peer is 0.


Format
------

**peer** *ipv4-address* **preferred-value** *preferredvalue*

**undo peer** *ipv4-address* **preferred-value**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *preferredvalue* | Specifies the preferred value of the routes that a BGP device learns from its peer. | The value is an integer ranging from 0 to 65535. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After a preferred value is configured for a peer, all the routes learned from the peer have the preferred value. If multiple routes with the same prefix are available, the route with the largest preferred value is preferred.



**Prerequisites**



A BGP peer has been configured. If the peer preferred-value command is used but no BGP peer exists, a message is displayed, indicating that the peer does not exist.



**Configuration Impact**



If a preferred value is set for the routes that a BGP device learns from a peer group, all members of the peer group inherit the configuration.




Example
-------

# Set the preferred value of a route received from a specified peer to 50.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vrfa
[*HUAWEI-bgp-instance-a-vrfa] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-a-vrfa] peer 10.1.1.1 preferred-value 50

```