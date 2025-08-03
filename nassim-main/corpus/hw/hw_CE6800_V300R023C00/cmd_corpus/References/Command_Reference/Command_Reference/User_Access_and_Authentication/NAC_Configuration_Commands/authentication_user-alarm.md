authentication user-alarm
=========================

authentication user-alarm

Function
--------



The **authentication user-alarm** command sets alarm thresholds for the percentage of successfully authenticated NAC users.

The **undo authentication user-alarm** command restores the default alarm thresholds for the percentage of successfully authenticated NAC users.



By default, the lower alarm threshold for the percentage of successfully authenticated NAC users is 50, and the upper alarm threshold is 100.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication user-alarm percentage** *percent-lower-value* *percent-upper-value*

**undo authentication user-alarm**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *percent-lower-value* | Specifies the lower alarm threshold for the percentage of successfully authenticated NAC users. | The value is an integer that ranges from 1 to 100. The default value is 50. |
| *percent-upper-value* | Specifies the upper alarm threshold for the percentage of successfully authenticated NAC users. | The value is an integer in the range from 1 to 100, in percentage. The default value is 100. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When the number of successfully authenticated NAC users reaches a specified percentage, the device generates an alarm. You can run the **authentication user-alarm percentage** command to set the upper and lower alarm thresholds for this percentage.When the percentage of successfully authenticated NAC users against the maximum number of users allowed by the device is greater than or equal to the upper alarm threshold, the device generates an alarm. When this percentage reaches or falls below the lower alarm threshold, the device generates a clear alarm.


Example
-------

# Set the lower and upper alarm thresholds for the percentage of successfully authenticated NAC users to 30 and 80, respectively.
```
<HUAWEI> system-view
[~HUAWEI] authentication user-alarm percentage 30 80

```