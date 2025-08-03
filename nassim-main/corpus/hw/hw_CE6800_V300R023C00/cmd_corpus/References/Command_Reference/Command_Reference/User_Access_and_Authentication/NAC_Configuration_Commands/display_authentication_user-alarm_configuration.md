display authentication user-alarm configuration
===============================================

display authentication user-alarm configuration

Function
--------



The **display authentication user-alarm configuration** command displays alarm thresholds for the percentage of successfully authenticated NAC users.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display authentication user-alarm configuration**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view the alarm thresholds for the percentage of successfully authenticated NAC users.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the alarm thresholds for the percentage of successfully authenticated NAC users.
```
<HUAWEI> display authentication user-alarm configuration
  Current Alarm Percent:100                                                     
  Current Alarm Resume Percent:60

```

**Table 1** Description of the **display authentication user-alarm configuration** command output
| Item | Description |
| --- | --- |
| Current Alarm Percent | Upper alarm threshold for the percentage of successfully authenticated NAC users. |
| Current Alarm Resume Percent | Lower alarm threshold for the percentage of successfully authenticated NAC users. |