display stp bridge (All views)
==============================

display stp bridge (All views)

Function
--------



The **display stp bridge** command displays detailed information about the spanning tree of a bridge.




Format
------

**display stp bridge** { **local** | **root** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **local** | Displays detailed information about the spanning tree of the local bridge. | - |
| **root** | Displays details about the spanning tree of the root bridge. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



If a device has many interfaces, running the **display stp** command displays a large amount of information, and it is difficult to find wanted information about the spanning trees of the root and local bridges.To view detailed information about the spanning trees of the root and local bridges, run the display stp bridge command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the spanning tree of the root bridge.
```
<HUAWEI> display stp bridge root
MSTID RootID               RootCost HelloTime MaxAge ForwardDelay RootPort
--------------------------------------------------------------------------
    0 61440.00e0-fc12-3456        0         2     20           15                         
    1 61440.00e0-fc12-3456        0         2     20           15

```

**Table 1** Description of the **display stp bridge (All views)** command output
| Item | Description |
| --- | --- |
| MSTID | MSTP instance ID. |
| RootID | MSTP root bridge ID. |
| RootCost | MSTP root path cost. |
| HelloTime | Interval at which Bridge Protocol Data Units (BPDUs) are sent from the root bridge. |
| MaxAge | Maximum TTL of a BPDU. |
| ForwardDelay | Time interface status transition takes. |
| RootPort | Root port. |