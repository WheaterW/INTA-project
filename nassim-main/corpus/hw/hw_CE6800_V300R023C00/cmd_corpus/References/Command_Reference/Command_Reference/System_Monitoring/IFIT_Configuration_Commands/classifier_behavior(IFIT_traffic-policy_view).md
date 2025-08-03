classifier behavior(IFIT traffic-policy view)
=============================================

classifier behavior(IFIT traffic-policy view)

Function
--------



The **classifier behavior** command configures a traffic behavior for a specified traffic classifier in an IFIT traffic policy, that is, binds the traffic classifier to the traffic behavior.

The **undo classifier behavior** command unbinds a traffic classifier from a traffic behavior in an IFIT traffic policy.



By default, no traffic classifier or traffic behavior is bound to an IFIT traffic policy.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**classifier** *classifier-name* **behavior** *behavior-name* [ **precedence** *precedence-value* | **cache-number** *cache-number* ] \*

**undo classifier** *classifier-name* **behavior** *behavior-name* [ **precedence** *precedence-value* | **cache-number** *cache-number* ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **behavior** *behavior-name* | Specifies the name of a traffic classifier. | The value is a string of 1 to 32 case-sensitive characters, starting with a letter or digit. Spaces and question marks (?) are not supported. |
| **precedence** *precedence-value* | Specifies the priority of a traffic classifier. | The value is an integer ranging from 0 to 63. |
| **cache-number** *cache-number* | Specifies the number of flow tables generated based on a policy. | The value is an integer in the range from 1 to 6144. The default value is 512. |
| **classifier** *classifier-name* | Specifies the name of a traffic classifier. | The value is a string of 1 to 32 case-sensitive characters, starting with a letter or digit. Spaces and question marks (?) are not supported. |



Views
-----

IFIT traffic-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After creating an IFIT traffic policy, you must associate the traffic classifier with the traffic behavior in the IFIT traffic policy view. That is, bind the traffic classifier to the traffic behavior so that the traffic policy has actual contents and can be applied.

**Prerequisites**

The IFIT view is displayed using the **ifit** command.A traffic classifier has been created using the **classifier** command.A traffic behavior has been created using the **behavior** command.A traffic policy has been created using the **policy** command.


Example
-------

# Apply the traffic behavior b1 to packets matching the traffic classifier c1 in the traffic policy p1.
```
<HUAWEI> system-view
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] traffic classifier c1
[*HUAWEI-ifit-dcn-instance-classifier-c1] quit
[*HUAWEI-ifit-dcn-instance] traffic behavior b1
[*HUAWEI-ifit-dcn-instance-behavior-b1] quit
[*HUAWEI-ifit-dcn-instance] traffic policy p1
[*HUAWEI-ifit-dcn-instance-policy-p1] classifier c1 behavior b1

```