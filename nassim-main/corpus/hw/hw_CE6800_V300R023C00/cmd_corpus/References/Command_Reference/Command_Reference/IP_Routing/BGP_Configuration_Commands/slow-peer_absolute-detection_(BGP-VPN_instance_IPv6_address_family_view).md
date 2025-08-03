slow-peer absolute-detection (BGP-VPN instance IPv6 address family view)
========================================================================

slow-peer absolute-detection (BGP-VPN instance IPv6 address family view)

Function
--------



The **slow-peer absolute-detection threshold** command configures an absolute threshold for slow peer detection.

The **undo slow-peer absolute-detection threshold** command restores the absolute threshold of slow peer detection.

The **slow-peer absolute-detection disable** command disables slow peer detection in absolute mode.

The **undo slow-peer absolute-detection disable** command enables slow peer detection in absolute mode.



By default, slow peer detection in absolute mode is enabled, and the threshold for slow peer detection in absolute mode is 9s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**slow-peer absolute-detection threshold** *threshold*

**slow-peer absolute-detection disable**

**undo slow-peer absolute-detection threshold** *threshold*

**undo slow-peer absolute-detection disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **threshold** *threshold* | Specifies an absolute threshold for slow peer detection. | The value is an integer that ranges from 3 to 3600, in seconds. The default value is 60. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After slow peer detection is enabled, the local device calculates the difference between the time taken to send Update messages to each BGP peer and the shortest time taken to send Update messages to a BGP peer in the group. If the difference between the time taken to send Update messages to BGP peer 1 and the shortest time is greater than the specified threshold, the local device considers BGP peer 1 as a slow peer and removes it from the update peer-group. The removal of the slow peer prevents this slow peer from affecting update message advertisement to other peers in the group. If Update messages fail to be advertised, the traditional slow peer detection function cannot be used to detect slow peers. To address this problem, configure an absolute threshold for slow peer detection. If the delay in sending Update messages to a peer is greater than the absolute threshold, the peer is considered a slow peer.


Example
-------

# Set the absolute threshold for slow peer detection to 100s.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] slow-peer absolute-detection threshold 100

```