peer peer-as-check(BGP-IPv4 unicast address family view/BGP-IPv6 unicast address family view)(group)
====================================================================================================

peer peer-as-check(BGP-IPv4 unicast address family view/BGP-IPv6 unicast address family view)(group)

Function
--------



The **peer peer-as-check** command prevents the routes received from an EBGP peer from being broadcast to other peers with the same AS number as the EBGP peer.

The **undo peer peer-as-check** command cancels the configuration.



By default, the routes received from an EBGP peer are broadcast to other EBGP peers in the same AS.


Format
------

**peer** *peerGroupName* **peer-as-check**

**undo peer** *peerGroupName* **peer-as-check**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP-IPv4 unicast address family view,BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, after receiving a route from an EBGP peer in AS 200, the local device in AS 100 advertises the route to all EBGP peers in AS 200. After the **peer peer-as-check** command is run, the local device does not advertise the routes learned from an EBGP peer to the peers in a peer group with the same AS number as that of the EBGP peer. This reduces BGP memory and CPU consumption and shortens route convergence time during route flapping.

**Configuration Impact**

After this command is run, the number of BGP update peer-groups on the device is affected. If the AS numbers of BGP peers configured with this function are different, these BGP peers cannot be added to the same BGP update peer-group.

**Precautions**

This command applies only to EBGP peers.


Example
-------

# Configure a device not to advertise the routes learned from an EBGP peer to peers with the same AS number as this EBGP peer in a peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group a external
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer a enable
[*HUAWEI-bgp-af-ipv4] peer a peer-as-check

```