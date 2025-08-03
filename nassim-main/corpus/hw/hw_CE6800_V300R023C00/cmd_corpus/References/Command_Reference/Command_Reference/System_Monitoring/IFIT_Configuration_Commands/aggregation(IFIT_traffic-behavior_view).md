aggregation(IFIT traffic-behavior view)
=======================================

aggregation(IFIT traffic-behavior view)

Function
--------



The **aggregation** command configures a flow table aggregation policy.

The **undo aggregation** command restores the policy of not aggregating flow tables.



By default, no aggregation source port or aggregation destination port is specified for IFIT.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**aggregation** { **source-port** | **destination-port** | **none** }

**undo aggregation** { **source-port** | **destination-port** | **none** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **source-port** | Source port aggregation. | - |
| **destination-port** | Destination port aggregation. | - |
| **none** | No aggregation. | - |



Views
-----

IFIT traffic-behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before configuring IFIT, you can run the command to configure IFIT flow table aggregation. Flow table aggregation includes source port aggregation, destination port aggregation, and no aggregation.

**Prerequisites**

IFIT has been enabled.


Example
-------

# Aggregate flows based on the source port in the IFIT flow table.
```
<HUAWEI> system-view
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] traffic behavior huawei
[*HUAWEI-ifit-dcn-instance-behavior-huawei] aggregation source-port

```