display device board
====================

display device board

Function
--------



The **display device board** command displays the type and status of devices, excluding information about power modules and fan modules.




Format
------

**display device board**


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

You can use this command to check the working status of boards on a device and check whether the device is working normally.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the components on a device.
```
<HUAWEI> display device board
CE6866's Device status:
--------------------------------------------------------------------------------
Slot  Card   Type                     Online   Power Register     Alarm     Primary        
--------------------------------------------------------------------------------
1     -      CE6866-48S8CQ-P          Present  On    Registered   Normal    Master         
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display device board** command output
| Item | Description |
| --- | --- |
| Slot | Slot num. |
| Card | Card ID. |
| Type | Hardware type. |
| Online | Online status. |
| Power | Power status. |
| Register | The register status. |
| Alarm | Alarm status. |
| Primary | Active/standby status. |