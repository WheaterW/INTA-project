traffic behavior(IFIT-dcn-instance view)
========================================

traffic behavior(IFIT-dcn-instance view)

Function
--------



The **traffic behavior** command configures a traffic behavior.

The **undo traffic behavior** command deletes a traffic behavior.



By default, no IFIT traffic behavior is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**traffic behavior** *behavior-name*

**undo traffic behavior** *behavior-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **behavior** *behavior-name* | Specifies the name of a traffic behavior. | The value is a string of 1 to 32 case-sensitive characters, starting with a letter or digit. Spaces and question marks (?) are not supported. |



Views
-----

IFIT dcn-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before configuring IFIT, you can run this command to configure an IFIT traffic behavior. In the traffic behavior view, you can specify the IFIT behavior for traffic.

**Prerequisites**

IFIT has been enabled.


Example
-------

# Specify the IFIT traffic behavior.
```
<HUAWEI> system-view
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] traffic behavior behavior1

```