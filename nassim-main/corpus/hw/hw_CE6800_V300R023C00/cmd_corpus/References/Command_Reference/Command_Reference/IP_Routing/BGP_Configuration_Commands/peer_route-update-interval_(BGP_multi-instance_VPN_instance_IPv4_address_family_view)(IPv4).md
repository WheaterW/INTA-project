peer route-update-interval (BGP multi-instance VPN instance IPv4 address family view)(IPv4)
===========================================================================================

peer route-update-interval (BGP multi-instance VPN instance IPv4 address family view)(IPv4)

Function
--------



The **peer route-update-interval** command sets the interval for sending Update messages with the same route prefix to a peer.

The **undo peer route-update-interval** command restores the default configuration.



By default, the interval at which routing updates are sent to IBGP peers is 15s, and the interval at which routing updates are sent to EBGP peers is 30s.


Format
------

**peer** *ipv4-address* **route-update-interval** *interval*

**undo peer** *ipv4-address* **route-update-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *interval* | Specifies the minimum interval at which routing updates are sent. | The value is an integer that ranges from 0 to 600, in seconds. The value 0 indicates that the device immediately sends a BGP Update packet to notify the peer of the route change. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



When routes change, the device sends Update packets to notify the peers. If a route changes frequently, run this command to set an interval at which the device sends Update messages carrying the same route prefix to a specified peer or peer group. This prevents the device from sending Update messages for each route change.



**Implementation Procedure**



If the **peer route-update-interval** command is used but no peer exists, a message is displayed, indicating that the peer does not exist.



**Precautions**

After the **peer route-update-interval** command is run, all routes in the current BGP routing table are sent to peers.

* If the interval between two new route additions is longer than the interval configured using the **peer route-update-interval** command, the device immediately sends an Update message to notify its peers, regardless of the interval configured using the **peer route-update-interval** command.
* If the interval between two new route additions is shorter than the interval configured using the **peer route-update-interval** command, the device sends an Update message to notify its peers after the configured interval expires.If a route is withdrawn because the export policy denies the route, the device sends a Withdraw message to notify its peers after the configured interval expires.
* In other cases, if a route is withdrawn, the device immediately sends a Withdraw message to notify its peers, regardless of the interval set using the **peer route-update-interval** command.


Example
-------

# Set the interval for sending route update messages to the peer to 10 seconds.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-a-vpna] peer 10.1.1.1 route-update-interval 10

```