aging-time (IFIT-dcn-instance view)
===================================

aging-time (IFIT-dcn-instance view)

Function
--------



The **aging-time** command configures the IFIT aging time.

The **undo aging-time** command restores the default IFIT aging time.



By default, the IFIT aging time is 120 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**aging-time** *time-value*

**undo aging-time** [ *time-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **aging-time** *time-value* | Specifies the aging time of the IFIT flow table. | The value is an integer in the range from 10 to 3600. The default value is 120. |



Views
-----

IFIT dcn-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to adjust the IFIT aging time based on network requirements. If no packet statistics are collected in a flow table until the aging time expires, IFIT deletes the flow table.

**Prerequisites**

IFIT has been enabled.

**Precautions**

The IFIT aging time must be greater than the IFIT conversion period. You need to adjust the aging time before adjusting the conversion period. You are advised to set the IFIT aging time to at least twice the conversion period and at least 60s. If the IFIT aging time is too short, IFIT flow table statistics may fluctuate.


Example
-------

# Set the IFIT aging time to 200s.
```
<HUAWEI> system-view
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] aging-time 200

```