display saved-configuration configuration
=========================================

display saved-configuration configuration

Function
--------



The **display saved-configuration configuration** command displays the parameters of the function to automatically save configurations.




Format
------

**display saved-configuration configuration**


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

Run the **display saved-configuration configuration** command to check the parameters of the function to automatically save configurations, including the automatic save interval and CPU usage.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the parameters of the function to automatically save configurations.
```
<HUAWEI> display saved-configuration configuration
Auto save configuration status                    : Enable
 Auto save configuration interval                  : 60 minutes 
 Save delay after configuration changed            : 10 minutes 
 The threshold of the CPU usage permitted when save : 50%(default)

```

**Table 1** Description of the **display saved-configuration configuration** command output
| Item | Description |
| --- | --- |
| Auto save configuration status | The status of auto save configuration function.   * Enable. * Disable. |
| Auto save configuration interval | Interval for auto-save. |
| Save delay after configuration changed | Auto-save delay time after a configuration change. |
| The threshold of the CPU usage permitted when save | Threshold of CPU usage permitted during auto-save. |