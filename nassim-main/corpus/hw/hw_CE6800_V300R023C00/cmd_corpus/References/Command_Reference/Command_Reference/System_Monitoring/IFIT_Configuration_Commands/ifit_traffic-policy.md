ifit traffic-policy
===================

ifit traffic-policy

Function
--------



The **ifit traffic-policy** command applies a traffic policy to an interface.

The **undo ifit traffic-policy** command deletes a traffic policy from an interface.



By default, no IFIT traffic policy is applied to an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ifit traffic-policy** *policy-name*

**undo ifit traffic-policy** *policy-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **traffic-policy** *policy-name* | Specifies the name of a traffic policy. | The value is a string of 1 to 32 case-sensitive characters without spaces. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,50GE interface view,Eth-Trunk interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After an IFIT traffic policy is created, apply the traffic policy to an interface. Device traffic is filtered based on the traffic policy and specified flows that meet conditions enter the IFIT measurement domain.

**Prerequisites**

The IFIT view is displayed using the **ifit** command.A traffic policy has been created using the **policy** command.


Example
-------

# Apply the IFIT policy p1 to an interface.
```
<HUAWEI> system-view
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] traffic policy p1
[*HUAWEI-ifit-dcn-instance-policy-p1] quit
[*HUAWEI-ifit-dcn-instance] quit
[*HUAWEI-ifit] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] ifit traffic-policy p1

```