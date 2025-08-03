peer route-update-interval (BGP-VPN-Target address family view)
===============================================================

peer route-update-interval (BGP-VPN-Target address family view)

Function
--------



The **peer route-update-interval** command sets the interval for sending Update messages with the same route prefix to a peer.

The **undo peer route-update-interval** command restores the default configuration.



By default, the interval at which routing updates are sent to IBGP peers is 15s, and the interval at which routing updates are sent to EBGP peers is 30s.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **route-update-interval** *interval*

**undo peer** { *ipv4-address* | *ipv6-address* } **route-update-interval**

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **route-update-interval** *interval*

**undo peer** *ipv4-address* **route-update-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *interval* | Specifies the minimum interval at which routing updates are sent. | The value is an integer ranging from 0 to 600, in seconds. The value 0 indicates that the device immediately sends BGP Update messages to notify its peers of route changes. |



Views
-----

BGP-VPN-target address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When routes change, the device sends routing updates to notify its peers. If a route changes frequently, the **peer route-update-interval** command can be used to adjust the interval at which Update packets are sent for changes of this route. This frees the device from sending Update packets for every route change.

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
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 200
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer 10.1.1.1 enable
[*HUAWEI-bgp-af-vpn-target] peer 10.1.1.1 route-update-interval 10

```