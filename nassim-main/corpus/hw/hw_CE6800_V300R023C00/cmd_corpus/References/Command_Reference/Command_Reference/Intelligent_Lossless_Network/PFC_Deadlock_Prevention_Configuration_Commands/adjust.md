adjust
======

adjust

Function
--------



The **adjust** command adjusts the queue priority and DSCP value of packets in a hook-shaped flow matching a PFC uplink interface group.

The **undo adjust** command deletes the configuration for a hook-shaped flow matching a PFC uplink interface group.



By default, there is no configuration for a hook-shaped flow matching a PFC uplink interface group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**adjust original-dscp** *original-dscpvalue* **to** **priority** *prioritynumber* **dscp** *dscpvalue*

**undo adjust original-dscp** *original-dscpvalue* **to** **priority** *prioritynumber* **dscp** *dscpvalue*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **to** | Adjusts information of packets in a hook-shaped flow matching a PFC uplink interface group. | - |
| **priority** *prioritynumber* | Adjusts the queue priority of packets in a hook-shaped flow matching a PFC uplink interface group so that the packets are forwarded through the specified queue. | The value is an integer ranging from 0 to 7. |
| **dscp** *dscpvalue* | Adjusts the DSCP value of packets in a hook-shaped flow matching a PFC uplink interface group so that the packets are still mapped to the specified queue on the downstream device. | The value is an integer ranging from 0 to 63. |
| **original-dscp** *original-dscpvalue* | Specifies the DSCP value of packets in a hook-shaped flow to be adjusted. | The value is an integer ranging from 0 to 63. |



Views
-----

PFC uplink group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the system detects that a service flow enters and exits through interfaces in a PFC uplink interface group, the service flow is considered as a high-risk hook-shaped flow that may cause a PFC deadlock. You can run this command to configure a PFC uplink interface group. For a hook-shaped flow that matches the interface group, the device proactively adjusts the queue priority and DSCP value in the packets to change the PFC backpressure path and prevent loops caused by PFC frames.

**Precautions**



The **adjust** command can be configured at most twice in a PFC uplink interface group, and the settings of the original-dscpValue, priority, and dscpValue parameters must be different in the two command configurations. If the configuration needs to be modified, run the **undo adjust original-dscp original-dscpValue to priority priority dscp dscpValue** command to delete the original configuration first.




Example
-------

# Set the queue priority to 4 and DSCP value to 32 for a hook-shaped flow which original DSCP value is 10 that matches the PFC uplink interface group myuplink.
```
<HUAWEI> system-view
[~HUAWEI] dcb pfc uplink group myuplink
[*HUAWEI-dcb-pfc-uplink-group-myuplink] adjust original-dscp 10 to priority 4 dscp 32

```