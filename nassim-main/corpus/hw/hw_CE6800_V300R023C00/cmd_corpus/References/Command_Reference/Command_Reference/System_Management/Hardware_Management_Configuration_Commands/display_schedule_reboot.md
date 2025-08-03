display schedule reboot
=======================

display schedule reboot

Function
--------



The **display schedule reboot** command displays the configuration of the scheduled restart of the device.




Format
------

**display schedule reboot**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After using the **schedule reboot** command to configure a scheduled restart, you can use this command to view the configuration of the scheduled restart.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of the scheduled restart of the device.
```
<HUAWEI> display schedule reboot
Info: System will reboot at: 2019-12-20 19:20:00 UTC (in 29 hours and 19 minutes).

```

**Table 1** Description of the **display schedule reboot** command output
| Item | Description |
| --- | --- |
| System will reboot at | Specific restart time. |
| in 29 hours and 19 minutes | Time span between the restart time and the current time. |
| Info | Configuration list. |