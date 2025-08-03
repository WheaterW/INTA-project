peer tracking (BGP-VPN instance IPv6 address family view) (group)
=================================================================

peer tracking (BGP-VPN instance IPv6 address family view) (group)

Function
--------



The **peer tracking** command enables BGP Peer Tracking. That is, you can configure BGP to fast detect the unreachable state of a peer and re-establish the connection between the local device and the peer.

The **undo peer tracking** command disables BGP Peer Tracking.



By default, BGP Peer Tracking is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **tracking** [ **delay** *delay-time* ]

**undo peer** *group-name* **tracking**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **delay** *delay-time* | Indicates the interval between when BGP detects the peer unreachable and when BGP tears down the corresponding connection. | An integer ranging from 0 to 65535, in seconds. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a network where BFD is unsuitable to be deployed, you can configure BGP Peer Tracking on the local device to implement fast network convergence by rapidly detecting the unreachable state of the peer.A BGP peer is considered unreachable in either of the following situations:

* The BGP peer's IP address does not match any route in the IP routing table.
* The BGP peer's IP address matches a route with the outbound interface being a Null0 interface in the IP routing table.A proper value of delay-time can ensure network stability when a peer is detected unreachable.
* If delay-time is set to 0, BGP immediately tears down the connection between the local device and its peer after the peer is detected unreachable.
* If IGP route flapping occurs and delay-time for an IBGP peer is set to 0, the peer relationship between the local device and the peer alternates between Up and Down. Therefore, delay-time for an IBGP peer should be set to a value greater than the actual IGP route convergence time.
* When BGP neighbors successfully perform the GR negotiation, the master/slave switchover occurs on the BGP neighbors, to prevent the failure of GR, delay-time should be set to a value greater than GR convergence time. If delay-time is set to be smaller than the GR convergence time, the connection between the local device and the BGP peer will be torn down, which leads to the failure of GR.

**Prerequisites**

The **peer as-number** command has been run to create BGP peers or BGP peer groups.

**Precautions**

IGP is configured with GR, and the BGP neighbor relationship is established based on IGP routes. In such a situation, when a node fails on the network and the master/slave switchover occurs on the node, IGP does not delete the routes from the node, and BGP neighbors cannot sense the fault on the node. Therefore, the BGP Peer Tracking function does not take effect.


Example
-------

# Configure BGP Peer Tracking.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpn1
[*HUAWEI-bgp-6-vpn1] group test external
[*HUAWEI-bgp-6-vpn1] peer test as-number 200
[*HUAWEI-bgp-6-vpn1] peer test tracking

```