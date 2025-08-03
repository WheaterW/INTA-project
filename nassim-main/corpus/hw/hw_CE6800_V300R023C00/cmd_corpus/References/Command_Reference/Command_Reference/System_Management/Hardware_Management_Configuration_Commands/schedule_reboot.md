schedule reboot
===============

schedule reboot

Function
--------



The **schedule reboot** command configures the scheduled restart of a device and sets the specific time when the device restarts or the delay time before the device restarts.

The **undo schedule reboot** command disables the scheduled restart function.



By default, the scheduled restart is disabled.


Format
------

**schedule reboot** { **at** *exact-time* [ *date* ] | **delay** *interval* [ **force** ] }

**undo schedule reboot**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **at** *exact-time* | Specifies the device restart time. | exact-time is in the format of hh:mm. It must be later than the current time of the device and the difference between them must be less than 720 hours. In this parameter:   * hh indicates the hour, and the value ranges from 0 to 23. * mm indicates the minute, and the value ranges from 0 to 59. |
| *date* | Specifies the device restart date. | The format of date is YYYY/MM/DD, in which YYYY/MM/DD indicates the year, month, and day. In this parameter:   * YYYY is an integer that ranges from 2000 to 2099. * MM is an integer that ranges from 1 to 12. * DD is an integer that ranges from 1 to 31. |
| **delay** *interval* | Specifies the delay time before the device restarts. | The format of interval is hh:mm or mm. The value must be no more than 720 hours. In this parameter:   * Hh:mm: hh indicates the hour, ranging from 0 to 720, and mm indicates minutes, ranging from 0 to 59. * mm indicates the minutes, ranging from 0 to 43200.   Currently, the system supports a string of 1 to 6 characters. |
| **force** | Specifies forcible scheduled restart. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When upgrading or restarting the device, you can configure the device to restart at time when few services are running to minimize the impact on services.

**Configuration Impact**

If the **schedule reboot at** command is used to set a specific date parameter (yyyy/mm/dd) and the date is a future date, the device restarts at the scheduled time and the error is within 1 minute.Note that the specified date cannot be 30 days later than the current date. In addition, after this command is used, the system prompts you to confirm the input information. The setting takes effect only after you enter "Y" or "y". If the related configuration exists, the latest configuration overrides the previous one.If no specific date is set, the following situations occur:

* If the scheduled time is later than the current time, the device restarts at this time that day.
* If the scheduled time is earlier than the current time, the device restarts at this time next day.After the **schedule reboot** command is used, if the system time is changed using the **clock datetime** command and the new system time is later than the time set using the **schedule reboot** command, the parameters set using the **schedule reboot** command become invalid.

**Precautions**

Exercise caution when running this command. When the device restarts at the scheduled time, services are interrupted on the entire device.When the device restarts, ensure that the configuration file on the device is saved.


Example
-------

# Cancel the scheduled restart operation.
```
<HUAWEI> undo schedule reboot

```

# Configure the device to restart at 22:00.
```
<HUAWEI> schedule reboot at 22:00
Warning: The current configuration will be saved to the next startup saved-configuration file. Continue? [Y/N]:N
Info: Reboot system at: 2020-06-02 22:00:00 UTC (in 5 hours and 43 minutes).
Confirm? [Y/N]:Y

```

**Table 1** Description of the **schedule reboot** command output
| Item | Description |
| --- | --- |
| Warning | Whether to save the configuration. |
| Info | Restart confirmation details. |