slow-peer absolute-detection (BGP-MVPN address family view)
===========================================================

slow-peer absolute-detection (BGP-MVPN address family view)

Function
--------



The **slow-peer absolute-detection threshold** command configures an absolute threshold for slow peer detection.

The **undo slow-peer absolute-detection threshold** command restores the absolute threshold of slow peer detection.

The **slow-peer absolute-detection disable** command disables slow peer detection in absolute mode.

The **undo slow-peer absolute-detection disable** command enables slow peer detection in absolute mode.



By default, slow peer detection in absolute mode is enabled, and the threshold for slow peer detection in absolute mode is 60 seconds.


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

BGP-MVPN address family view


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
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn] slow-peer absolute-detection threshold 100

```