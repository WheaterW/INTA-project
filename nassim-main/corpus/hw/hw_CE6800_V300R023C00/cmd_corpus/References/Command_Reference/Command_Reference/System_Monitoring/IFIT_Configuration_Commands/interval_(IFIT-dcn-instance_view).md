interval (IFIT-dcn-instance view)
=================================

interval (IFIT-dcn-instance view)

Function
--------



The **interval** command configures the IFIT measurement interval.

The **undo interval** command restores the IFIT measurement interval to the default value.



By default, the IFIT measurement interval is 60s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**interval** *interval-value*

**undo interval** [ *interval-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interval** *interval-value* | IFIT measurement interval. | The value is an integer in the range from 10 to 3600. The default value is 60. |



Views
-----

IFIT dcn-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to configure the IFIT measurement interval, which determines the time for switching the Loss-Flag and the interval for exporting the flow table.

**Prerequisites**

IFIT has been enabled.

**Precautions**

The IFIT flow table aging time must be longer than the IFIT measurement interval. Before adjusting the IFIT measurement interval, adjust the flow table aging time.


Example
-------

# Set the IFIT measurement interval to 30s.
```
<HUAWEI> system-view
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] interval 30

```