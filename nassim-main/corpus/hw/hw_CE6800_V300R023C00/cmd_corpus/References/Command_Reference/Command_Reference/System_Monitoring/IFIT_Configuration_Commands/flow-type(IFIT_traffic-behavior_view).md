flow-type(IFIT traffic-behavior view)
=====================================

flow-type(IFIT traffic-behavior view)

Function
--------



The **flow-type** command configures the flow type for IFIT.

The **undo flow-type** command restores the dynamic IFIT flow function.



By default, dynamic flows are analyzed for IFIT.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**flow-type** { **dynamic** | **static** **flow-id** *flow-id* }

**undo flow-type** { **dynamic** | **static** [ **flow-id** *flow-id* ] }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *flow-id* | - | The value is an integer ranging from 1 to 128. |



Views
-----

IFIT traffic-behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before configuring IFIT, you can run the command to configure an IFIT flow type. Dynamic flows are created and analyzed based on the specified 4-tuple or 5-tuple. Static flows are created and analyzed based on the specified flow characteristics, which are not affected by the flow aggregation policy.

**Prerequisites**

IFIT has been enabled.


Example
-------

# Set the IFIT flow type to static and the flow ID to 100.
```
<HUAWEI> system-view
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] traffic behavior huawei
[*HUAWEI-ifit-dcn-instance-behavior-huawei] flow-type static flow-id 100

```