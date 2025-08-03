display device configuration
============================

display device configuration

Function
--------



The **display device configuration** command displays the type and status of configured devices, including information about pre-configured and online devices.




Format
------

**display device configuration**


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

You can use this command to check device pre-configuration.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the components on a device.
```
<HUAWEI> display device configuration
CE6866-48S8CQ-P's Device status:
--------------------------------------------------------------------------------
Slot  Card   Type                           Online   Power Register     Alarm     Primary
--------------------------------------------------------------------------------
1     -      CE6866-48S8CQ-P        Present  On    Registered   Normal    Master
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display device configuration** command output
| Item | Description |
| --- | --- |
| Slot | Slot ID. |
| Card | Card ID. |
| Type | Hardware type. |
| Online | Online status. |
| Power | Power status. |
| Register | Register status. |
| Alarm | Alarm status. |
| Primary | Active/standby status. |