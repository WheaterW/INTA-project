peer route-update-interval(bgp-muli-instance-af-evpn view)
==========================================================

peer route-update-interval(bgp-muli-instance-af-evpn view)

Function
--------



The **peer route-update-interval** command sets the interval for sending Update messages with the same route prefix to a peer.

The **undo peer route-update-interval** command restores the default configuration.



By default, the interval at which route update messages are sent to IBGP peers is 15s, and the interval at which route update messages are sent to EBGP peers is 30s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** { *peerIpv4Addr* | *peerIpv6Addr* } **route-update-interval** *interval*

**undo peer** { *peerIpv4Addr* | *peerIpv6Addr* } **route-update-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *interval* | Specifies the minimum interval at which routing updates are sent. | The value is an integer ranging from 0 to 600, in seconds. The value 0 indicates that the device immediately sends BGP Update messages to notify its peers of route changes. |



Views
-----

bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When routes change, the device sends routing updates to notify its peers. If a route changes frequently, the **peer route-update-interval** command can be used to adjust the interval at which Update packets are sent for changes of this route. This frees the device from sending Update packets for every route change.

**Precautions**

After the **peer route-update-interval** command is run, all routes in the current BGP routing table are sent to peers.

* If the interval between two new route additions is longer than the interval configured using the **peer route-update-interval** command, the device immediately sends an Update message to notify its peers, regardless of the interval configured using the **peer route-update-interval** command.
* If the interval between two new route additions is shorter than the interval configured using the **peer route-update-interval** command, the device sends an Update message to notify its peers after the configured interval expires.If a route is withdrawn because the export policy denies the route, the device sends a Withdraw message to notify its peers after the configured interval expires.
* In other cases, if a route is withdrawn, the device immediately sends a Withdraw message to notify its peers, regardless of the interval set using the **peer route-update-interval** command.

Example
-------

# Set the interval at which BGP sends route update packets to a peer to 10 seconds in the BGP-EVPN multi-instance address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance aa
[*HUAWEI-bgp-instance-aa] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-aa] l2vpn-family evpn
[*HUAWEI-bgp-instance-aa-af-evpn] peer 10.1.1.1 enable
[*HUAWEI-bgp-instance-aa-af-evpn] peer 10.1.1.1 route-update-interval 10

```