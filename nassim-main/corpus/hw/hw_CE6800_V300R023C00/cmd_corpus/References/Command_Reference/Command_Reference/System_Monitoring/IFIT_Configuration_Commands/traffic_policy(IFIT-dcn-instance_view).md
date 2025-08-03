traffic policy(IFIT-dcn-instance view)
======================================

traffic policy(IFIT-dcn-instance view)

Function
--------



The **traffic policy** command configures a traffic policy.

The **undo traffic policy** command deletes a traffic policy.



By default, no IFIT traffic policy is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**traffic policy** *policy-name*

**undo traffic policy** *policy-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **policy** *policy-name* | Specifies the name of a traffic policy. | The value is a string of 1 to 32 case-sensitive characters without spaces. |



Views
-----

IFIT dcn-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before configuring IFIT, you can run this command to configure an IFIT traffic policy. A traffic policy can be bound to a traffic classifier or a traffic behavior. The traffic policy can be applied to an interface or globally, and the number and priority of flows created based on the traffic policy can be specified.

**Prerequisites**

IFIT has been enabled.


Example
-------

# Specify an IFIT traffic policy.
```
<HUAWEI> system-view
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] traffic policy policy1

```