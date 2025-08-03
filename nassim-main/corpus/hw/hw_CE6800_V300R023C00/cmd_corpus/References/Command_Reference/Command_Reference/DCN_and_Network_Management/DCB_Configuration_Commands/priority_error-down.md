priority error-down
===================

priority error-down

Function
--------



The **priority error-down** command configures the device to set an interface to the Error-Down state after a deadlock occurs on the interface for a specified number of times within 20 seconds.

The **undo priority error-down** command restores the default configuration.



By default, the device sets an interface to the Error-Down state after a deadlock occurs 30 times on the interface within 20 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**priority** *priority* **error-down** **threshold** *threshold-value*

**undo priority** *priority* **error-down** **threshold** *threshold-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies the priority. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 0 to 7.  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM:The value is an integer ranging from 0 to 5. |
| **threshold** *threshold-value* | Specifies the number of times a deadlock occurs within 20 seconds. The device sets an interface to the Error-Down state after a deadlock occurs on the interface for a specified number of times within 20 seconds. | The value is an integer that ranges from 1 to 300. The default value is 30. |



Views
-----

DCB PFC view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a deadlock occurs frequently on an interface within a period of time, you can run the priority error-down command to adjust the threshold for the interface to enter the Error-Down state.

**Prerequisites**

You need to run the priority command to specify the priority queue for which PFC is enabled.


Example
-------

# Configure the device to set an interface to the Error-Down state after a deadlock occurs on the interface 100 times within 20 seconds.
```
<HUAWEI> system-view
[~HUAWEI] dcb pfc
[~HUAWEI-dcb-pfc-default] priority 4
[*HUAWEI-dcb-pfc-default] priority 4 error-down threshold 100

```