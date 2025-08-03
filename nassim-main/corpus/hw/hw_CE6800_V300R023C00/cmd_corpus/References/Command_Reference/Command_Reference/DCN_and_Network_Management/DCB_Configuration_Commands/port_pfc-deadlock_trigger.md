port pfc-deadlock trigger
=========================

port pfc-deadlock trigger

Function
--------



The **port pfc-deadlock trigger** command configures the device to set an interface to the Error-Down state or disable PFC on the interface after a deadlock occurs on the interface for a specified number of times within 20 seconds.

The **undo port pfc-deadlock trigger** command restores the default configuration.



By default, the device automatically disables PFC on an interface after a deadlock occurs on the interface for a specified number of times within 20 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**port pfc-deadlock trigger** { **error-down** | **turn-off** }

**undo port pfc-deadlock trigger** { **error-down** | **turn-off** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **error-down** | Configure an interface to enter the Error-Down state when the number of deadlocks detected within 20 seconds exceeds the deadlock threshold. | - |
| **turn-off** | Disable the PFC function when the number of deadlocks detected within 20 seconds exceeds the deadlock threshold. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a deadlock occurs frequently on an interface within a period of time, you can run the port pfc-deadlock trigger command to configure the device to set the interface to the Error-Down state or disable PFC on the interface.


Example
-------

# Configure the device to set interface 100GE1/0/1 to the Error-Down state after a PFC deadlock occurs on the interface for a specified number of times within a specified period.
```
<HUAWEI> system
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] port pfc-deadlock trigger error-down

```