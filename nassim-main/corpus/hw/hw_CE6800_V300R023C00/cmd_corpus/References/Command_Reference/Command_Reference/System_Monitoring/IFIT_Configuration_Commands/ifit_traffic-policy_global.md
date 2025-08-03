ifit traffic-policy global
==========================

ifit traffic-policy global

Function
--------



The **ifit traffic-policy global** command applies an IFIT traffic policy globally.

The **undo ifit traffic-policy global** command cancels the global application of an IFIT traffic policy.



By default, no traffic policy is applied to the system.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ifit traffic-policy** *policy-name* **global**

**undo ifit traffic-policy** *policy-name* **global**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **traffic-policy** *policy-name* | Specifies the name of a traffic policy. | The value is a string of 1 to 32 case-sensitive characters without spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After an IFIT traffic policy is created, apply the traffic policy globally. Device traffic is filtered based on the traffic policy and specified flows that meet conditions enter the IFIT measurement domain.

**Prerequisites**

The IFIT view is displayed using the **ifit** command.A traffic policy has been created using the **policy** command.


Example
-------

# Apply the IFIT policy p1 globally.
```
<HUAWEI> system-view
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] traffic policy p1
[*HUAWEI-ifit-dcn-instance-policy-p1] quit
[*HUAWEI-ifit-dcn-instance] quit
[*HUAWEI-ifit] quit
[*HUAWEI] ifit traffic-policy p1 global

```