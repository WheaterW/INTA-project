dcb pfc uplink group
====================

dcb pfc uplink group

Function
--------



The **dcb pfc uplink group** command creates a PFC uplink interface group and displays the PFC uplink interface group view, or directly displays the view of an existing PFC uplink interface group.

The **undo dcb pfc uplink group** command deletes a PFC uplink interface group.



By default, no PFC uplink interface group exists in the system.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dcb pfc uplink group** *groupname*

**undo dcb pfc uplink group** *groupname*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *groupname* | Specifies the name of a PFC uplink interface group. | The value is a string of 1 to 31 case-sensitive characters. Spaces and special characters | > $ \* ^ are not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

PFC deadlock prevention is a preventive solution. This function enables devices to identify service flows that may cause a PFC deadlock, modify the queue priority, and change the PFC backpressure path to prevent loops caused by PFC frames.A PFC uplink interface group is defined in the PFC deadlock prevention function. You can add a leaf node's interfaces connecting to a spine node to a PFC uplink interface group. If the system detects that a service flow enters and exits through interfaces in the interface group, the service flow is a high-risk hook-shaped flow that may cause a PFC deadlock.

**Follow-up Procedure**

Run the group-member interface command in the PFC uplink interface group view to add specified interfaces to the PFC uplink interface group.Run the adjust command in the PFC uplink interface group view to adjust the queue priority and DSCP value of packets in a hook-shaped flow matching the PFC uplink interface group.

**Precautions**

Only one PFC uplink port group can be created in the system.


Example
-------

# Create a PFC uplink interface group named myuplink.
```
<HUAWEI> system-view
[~HUAWEI] dcb pfc uplink group myuplink
[*HUAWEI-dcb-pfc-uplink-group-myuplink]

```