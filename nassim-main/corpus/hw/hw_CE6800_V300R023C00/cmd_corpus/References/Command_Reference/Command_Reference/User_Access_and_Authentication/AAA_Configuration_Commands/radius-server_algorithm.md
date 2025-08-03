radius-server algorithm
=======================

radius-server algorithm

Function
--------

The **radius-server algorithm** command configures the algorithm for selecting RADIUS servers.

The **undo radius-server algorithm** command restores the default algorithm for selecting RADIUS servers.

By default, the algorithm for selecting RADIUS servers is primary/secondary.



Format
------

**radius-server algorithm** { **loading-share** | **master-backup** }

**undo radius-server algorithm**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **loading-share** | Sets the algorithm for selecting RADIUS servers to load balancing. | - |
| **master-backup** | Sets the algorithm for selecting RADIUS servers to primary/secondary. | - |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

When two or more than two RADIUS servers are available, you can use the **radius-server algorithm** command to set the algorithm for selecting RADIUS servers.

* When master-backup is specified, the weight is used to determine the primary and secondary RADIUS authentication or accounting servers. The server with a larger weight value is the primary server. If devices have the same weight, the server that was first configured is the primary server.
* When loading-share is specified, the device sends a packet to a server according to the weights configured on servers. For example, if the weights of RADIUS server A, RADIUS server B, and RADIUS server C are 80, 80, and 40 respectively, the probabilities of sending packets to RADIUS server A, RADIUS server B, and RADIUS server C are as follows:
* RADIUS server A: 80/(80 + 80 + 40) = 40%
* RADIUS server B: 80/(80 + 80 + 40) = 40%
* RADIUS server C: 40/(80 + 80 + 40) = 20%

**Precautions**

If you run the **radius-server algorithm** command multiple times in the same RADIUS server template view, only the latest configuration takes effect.



Example
-------

# Set the algorithm for selecting RADIUS servers to load balancing.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template template1
[*HUAWEI-radius-template1] radius-server algorithm loading-share

```