lacp preempt delay
==================

lacp preempt delay

Function
--------



The **lacp preempt delay** command configures a preemption delay.

The **undo lacp preempt delay** command restores the default preemption delay.



The default preemption delay is 30 seconds.


Format
------

**lacp preempt delay** *delay-time*

**undo lacp preempt delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **delay** *delay-time* | Specified a preemption delay. | The value is an integer ranging from 0 to 180, in seconds. |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a member interface of an Eth-Trunk interface in static Link Aggregation Control Protocol (LACP) mode fails, it goes to the backup state. When the member interface recovers, it switches to the forwarding state. To avoid unstable data transmission on the Eth-Trunk link due to the member interface's alternating between Up and Down, you can run the lacp preempt delay command to configure a preemption delay. In this manner, the member interface switches to the forwarding state only after the preemption delay expires.

* If it is required that the member interface switch to the forwarding state soon after it recovers, you can use the lacp preempt delay command to set the preemption delay to the minimum value.
* If it is required that the member interface switch to the forwarding state some time after it recovers, you can use the lacp preempt delay command to set a proper preemption delay. The value can range from 0 to 180 seconds.

**Prerequisites**



The **mode lacp-static** command has been run in the Eth-Trunk interface view to configure the Eth-Trunk interface to work in static LACP mode, and the **lacp preempt enable** command has been run in the Eth-Trunk interface view to enable preemption.



**Configuration Impact**



If LACP priority preemption occurs, the backup link waits for a period of time before switching to the forwarding state.



**Precautions**



In the case that LACP priority preemption in static LACP mode is enabled but the preemption delay is not configured, the system uses the default preemption delay. If the preemption delay of a local device is different from that of the peer, the system uses the longer preemption delay.




Example
-------

# Set the preemption delay of Eth-Trunk 1 to 20s.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] mode lacp-static
[*HUAWEI-Eth-Trunk1] lacp preempt enable
[*HUAWEI-Eth-Trunk1] lacp preempt delay 20

```