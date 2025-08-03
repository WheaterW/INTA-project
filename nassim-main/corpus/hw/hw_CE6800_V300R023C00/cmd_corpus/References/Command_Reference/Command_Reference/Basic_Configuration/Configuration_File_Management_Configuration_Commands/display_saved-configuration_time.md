display saved-configuration time
================================

display saved-configuration time

Function
--------



The **display saved-configuration time** command displays time information about the configuration of the autosave function.




Format
------

**display saved-configuration time**


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

To view the time when the system saves the configuration last time, run the **display saved-configuration time** command.

1. In the command output, "Saved configuration manually:" indicates the time when the configuration is manually saved.
2. In the command output, "Saved configuration automatically:" indicates the time when the configuration is automatically saved.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the time when the device saved the configuration last time.
```
<HUAWEI> display saved-configuration time
Saved configuration automatically:
15:49:07 DefaultZoneName 2015/06/08
Time Zone: UTC+00:00

```

**Table 1** Description of the **display saved-configuration time** command output
| Item | Description |
| --- | --- |
| Saved configuration automatically | The time information about the configuration of the autosave function. |
| Time Zone | Time zone. |