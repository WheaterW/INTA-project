display system work-mode
========================

display system work-mode

Function
--------



The **display system work-mode** command displays the working mode of the system, including the current working mode and the working mode after the next startup.




Format
------

**display system work-mode**


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

**Usage Scenario**



You can run the **display system work-mode** command to query the current working mode and the working mode after the next startup of the system.



**Precautions**



Only the CE6885-LL-56F supports this command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the working mode of the device.
```
<HUAWEI> display system work-mode
Current System Work mode: standard-forward
Next System Work mode : standard-forward

```

**Table 1** Description of the **display system work-mode** command output
| Item | Description |
| --- | --- |
| Current System Work mode | The current system work mode. |
| Next System Work mode | The next system work mode. |