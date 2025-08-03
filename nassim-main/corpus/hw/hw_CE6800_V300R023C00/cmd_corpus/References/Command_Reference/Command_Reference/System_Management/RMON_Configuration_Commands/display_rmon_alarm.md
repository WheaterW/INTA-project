display rmon alarm
==================

display rmon alarm

Function
--------



The **display rmon alarm** command displays RMON alarm configurations.




Format
------

**display rmon alarm** [ *entry-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *entry-number* | Specifies RMON alarm configurations with the index number of a specified entry in the alarm table. If no index number is specified, configurations about the alarm table will be displayed. | The value is an integer ranging from 1 to 65535. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After the rmon alarm command is used to configure the RMON alarm threshold function, you can view the monitored object, sampling interval, thresholds, conditions for triggering alarms, and last sampled value using the display rmon alarm command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display RMON alarm configurations.
```
<HUAWEI> display rmon alarm
Alarm table 1 owned by creator is invalid.
 Samples absolute value    : 1.3.6.1.4.1.2011.6.10.2.13
 Sampling interval         : 30(sec)
 Rising threshold          : 500(linked with event 1)
 Falling threshold         : 100(linked with event 2)
 When startup enables      : risingOrFallingAlarm
 Latest value              : 0
Alarm table 2 owned by null is invalid.
 Samples delta value       : 1.3.6.1.4.1.2011.6.10.2.13
 Sampling interval         : 10(sec)
 Rising threshold          : 100(linked with event 2)
 Falling threshold         : 10(linked with event 2)
 When startup enables      : risingOrFallingAlarm
 Latest value              : 0
Alarm table 3 owned by null is valid.
 Samples changeratio value : 1.3.6.1.4.1.2011.6.10.2.13
 Sampling interval         : 10(sec)
 Rising threshold          : 100(linked with event 12494)
 Falling threshold         : 10(linked with event 12494)
 When startup enables      : risingOrFallingAlarm
 Latest value              : 0

```

**Table 1** Description of the **display rmon alarm** command output
| Item | Description |
| --- | --- |
| Alarm table 1 owned by creator is invalid. | Current status of the alarm with the index number being entry-number created by the owner is status.   * entry-number: An index number of the alarm table entry. * owner: An owner. * status: * undercreation: The entry corresponding to the index is invalid. * valid: The entry corresponding to the index is valid. * invalid: The entry is invalid because of the invalid alarm monitor node. |
| Samples absolute value | Identifier of the alarm monitoring object, that is, the absolute value of the monitored MIB object (the value of the variable is directly extracted when the sampling time arrives). |
| Samples delta value | Alarm monitoring object, that is, the increment of the monitored MIB object. |
| Samples changeratio value | Alarm monitoring object, that is, the change rate of the monitored MIB object. |
| Sampling interval | Sampling interval, in seconds. |
| Rising threshold | Upper threshold of an RMON alarm table.  An alarm is generated when the sampled value is greater than or equal to the upper threshold. |
| Falling threshold | Indicates the lower threshold of an RMON alarm table (An alarm is generated when the sampled value is less than or equal to the lower threshold). |
| When startup enables | Conditions for triggering an alarm.  An alarm is generated when the sampled value is greater than or equal to the upper threshold, or less than or equal to the lower threshold. The value can be:   * risingOrFallingAlarm: An alarm is generated no matter the sampled value is greater than or equal to the upper threshold, or less than or equal to the lower threshold. * risingAlarm: An alarm is generated when the sampled value is greater than or equal to the upper threshold. * fallingAlarm: An alarm is generated when the sampled value is lower than or equal to the lower threshold. |
| Latest value | Latest sampled value. |