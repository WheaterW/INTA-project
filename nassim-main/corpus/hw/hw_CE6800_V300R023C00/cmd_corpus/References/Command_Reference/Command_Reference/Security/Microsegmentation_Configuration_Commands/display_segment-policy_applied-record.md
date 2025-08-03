display segment-policy applied-record
=====================================

display segment-policy applied-record

Function
--------



The **display segment-policy applied-record** command displays the application status of a microsegmentation grouping policy.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display segment-policy applied-record slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of characters. The value is a slot ID. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check the application status of a microsegmentation grouping policy, run the **display segment-policy applied-record** command. The command output helps you learn about the delivery status of microsegmentation grouping policy rules on the current device, facilitating fault diagnosis and locating.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the delivery status of microsegmentation policy rules.
```
<HUAWEI> display segment-policy applied-record slot 1
----------------------------------------------------------------------------------------
Policy                           Classfier Name                   Rule     State
----------------------------------------------------------------------------------------
p1                               c1                                  5     Success
                                                                    10     Success
                                 c2                                  5     Success
                                                                    10     Processing
----------------------------------------------------------------------------------------

```

**Table 1** Description of the **display segment-policy applied-record** command output
| Item | Description |
| --- | --- |
| Policy | Name of a microsegmentation grouping policy. |
| Classfier Name | Name of a segment classifier. |
| Rule | Microsegmentation rule index. |
| State | Delivery status.   * Success: The grouping policy is successfully delivered. * Fail: The grouping policy fails to be delivered. * Rollback: The grouping policy fails to be updated and the system rolls back to the status before the update. * Processing: The grouping policy information is being updated or delivered. |