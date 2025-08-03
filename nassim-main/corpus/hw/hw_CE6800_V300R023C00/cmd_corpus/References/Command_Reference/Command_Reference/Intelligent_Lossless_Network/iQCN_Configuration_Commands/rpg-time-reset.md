rpg-time-reset
==============

rpg-time-reset

Function
--------



The **rpg-time-reset** command sets the interval between rate increase events of the NIC on a forwarding device.

The **undo rpg-time-reset** command restores the default interval between rate increase events of the NIC.



By default, the interval between rate increase events of the NIC configured on a forwarding device is 300 us.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**rpg-time-reset** *timer*

**undo rpg-time-reset** *timer*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *timer* | Specifies the interval between rate increase events of the NIC configured on a forwarding device. The interval must be the same as the actual interval between rate increase events of the NIC on the source host. | The value is an integer ranging from 200 to 600, in us. |



Views
-----

iQCN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to configure the interval between rate increase events of the NIC on a forwarding device. If the forwarding device detects congestion after the iQCN function is enabled, the forwarding device compares the interval at which CNP packets are received with the interval between rate increase events of the NIC. If the interval at which CNP packets are received is longer, the forwarding device proactively sends CNP packets to the NIC of the source host to ensure that the NIC can reduce the packet sending rate in a timely manner.


Example
-------

# Set the interval between rate increase events of the NIC to 300 us on a forwarding device.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] iqcn
[*HUAWEI-ai-service-iqcn] rpg-time-reset 300

```