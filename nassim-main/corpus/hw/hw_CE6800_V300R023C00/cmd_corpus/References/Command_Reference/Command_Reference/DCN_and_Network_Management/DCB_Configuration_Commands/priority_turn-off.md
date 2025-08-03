priority turn-off
=================

priority turn-off

Function
--------



The **priority turn-off** command enables a switch to automatically disable PFC on an interface after the specified number of deadlocks occur within 20 seconds.

The **undo priority turn-off** command restores the default configuration.



By default, the device automatically disables PFC on an interface after a deadlock occurs 30 times on the interface within 20 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**priority** *priority* **turn-off** **threshold** *threshold-value*

**undo priority** *priority* **turn-off** **threshold** *threshold-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies the priority. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 0 to 7.  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM:The value is an integer ranging from 0 to 5. |
| **threshold** *threshold-value* | Specifies the number of deadlocks within 20 seconds. The switch disables PFC on an interface after the specified number of deadlocks is reached. | The value is an integer that ranges from 1 to 300. The default value is 30. |



Views
-----

DCB PFC view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a deadlock occurs frequently on an interface within a period of time, you can run the priority turn-off command to adjust the threshold for automatically disabling PFC on the interface.

**Prerequisites**

You need to run the priority command to specify the priority queue for which PFC is enabled.

**Precautions**

To use PFC after PFC is automatically disabled, run the **undo dcb pfc enable** command in the interface view to disable PFC, run the **dcb pfc enable** command to enable PFC, and reconfigure PFC.


Example
-------

# Configure a device to automatically disable PFC after 100 deadlocks occur within 20 seconds.
```
<HUAWEI> system-view
[~HUAWEI] dcb pfc
[~HUAWEI-dcb-pfc-default] priority 4
[*HUAWEI-dcb-pfc-default] priority 4 turn-off threshold 100

```