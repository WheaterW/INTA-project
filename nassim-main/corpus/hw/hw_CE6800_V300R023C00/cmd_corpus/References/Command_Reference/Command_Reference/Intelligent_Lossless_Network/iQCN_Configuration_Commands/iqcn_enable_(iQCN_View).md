iqcn enable (iQCN View)
=======================

iqcn enable (iQCN View)

Function
--------



The **iqcn enable** command enables the iQCN function globally.

The **undo iqcn enable** command disables the iQCN function globally and deletes the iQCN configuration.



By default, the iQCN function is disabled globally.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**iqcn enable**

**undo iqcn enable**


Parameters
----------

None

Views
-----

iQCN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In the traditional Congestion Notification Packet (CNP) mode, a forwarding device sends ECN packets to the destination end after detecting queue congestion. After receiving the ECN packets, the destination end sends CNP packets to the source end, to instruct the NIC of the source end to reduce the packet sending rate. When congestion occurs on the network, the NIC of the source end may not reduce the packet sending rate in a timely manner if the congestion feedback path is too long. As a result, the buffer of the forwarding device may be further congested, and even devices on the entire network stop sending traffic due to PFC.After the iQCN function is enabled on the forwarding device, the forwarding device detects whether congestion occurs on the network. When detecting congestion, the forwarding device compares the interval at which CNP packets are received with the interval between rate increase events of the NIC. If the interval at which CNP packets are received is longer, the forwarding device proactively sends CNP packets to the NIC of the source end to ensure that the NIC can reduce the packet sending rate in a timely manner.

**Follow-up Procedure**

* You need to run the iqcn enable command in the interface view to enable the iQCN function.
* You need to run the **rpg-time-reset** command on the forwarding device to set the interval between rate increase events of the NIC.
* You need to run the assign queue command in the iQCN view to specify a lossless queue for which the iQCN function is enabled.

**Precautions**

* When the iQCN function is disabled globally, you can modify settings of the parameters related to the iQCN function, but the function does not take effect. After the iQCN function is enabled globally again, the iQCN function takes effect again based on the current parameter settings.

Example
-------

# Enable the iQCN function globally.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] iqcn
[*HUAWEI-ai-service-iqcn] iqcn enable

```