slow-peer detection (BGP-IPv4 unicast address family view)
==========================================================

slow-peer detection (BGP-IPv4 unicast address family view)

Function
--------



The **slow-peer detection threshold** command enables slow peer detection.

The **undo slow-peer detection threshold** command disables slow peer detection.

The **slow-peer detection disable** command disables slow peer detection.

The **undo slow-peer detection disable** command enables slow peer detection.



By default, slow peer detection is enabled, and the slow peer detection threshold is 300s.


Format
------

**slow-peer detection threshold** *threshold-value*

**slow-peer detection disable**

**undo slow-peer detection** [ **threshold** *threshold-value* ]

**undo slow-peer detection disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **threshold** *threshold-value* | Specifies a slow peer detection threshold. If the difference between the time taken to send packets to BGP peer 1 and the shortest time taken to send packets to BGP peer 2 is greater than the threshold, BGP peer 1 is considered as a slow peer. | The value is an integer ranging from 120 to 3600, in seconds. The default value is 300. |



Views
-----

BGP-IPv4 unicast address family view,BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An update peer-group may contain multiple peers. If the local device advertises routes to one peer slowly due to network congestion, the speed at which the local device advertises routes to other peers in the update peer-group is affected. To prevent this problem, slow peer detection is enabled by default.After slow peer detection is enabled, the local device calculates the difference between the time taken to send messages to each peer in the update peer-group and the shortest time taken to send messages to each peer in the group. If the difference between the time taken to send messages to a peer and the shortest time is greater than the threshold specified for slow peer detection, the local device considers this peer as a slow peer and removes it from the update peer-group, which prevents this slow peer from affecting route advertisement to other peers in the group.

**Configuration Impact**

If the command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Enable slow peer detection in the BGP-IPv4 unicast address family view and set the slow peer detection threshold to 200s.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] slow-peer detection threshold 200

```