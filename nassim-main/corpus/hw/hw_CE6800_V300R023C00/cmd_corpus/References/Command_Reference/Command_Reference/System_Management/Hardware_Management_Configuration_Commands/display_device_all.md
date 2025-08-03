display device all
==================

display device all

Function
--------



The **display device all** command displays the type and status of components on a device.




Format
------

**display device all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays the type and status of all components on a device, including information about devices that are not available but have offline configurations. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can use this command to check the working status of components on a device and check whether the device is working normally.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display component information about the device.
```
<HUAWEI> display device all
CE6866-48S8CQ-P's Device status:
--------------------------------------------------------------------------------
Slot  Card   Type                     Online   Power Register     Alarm     Primary        
--------------------------------------------------------------------------------
1     -      CE6866-48S8CQ-P          Present  On    Registered   Normal    Master         
      FAN1   FAN                      Present  On    Registered   Normal    NA             
      FAN2   FAN                      Present  On    Registered   Normal    NA             
      FAN3   FAN                      Present  On    Registered   Normal    NA             
      PWR1   PAC600S12-CB             Present  On    Registered   Normal    NA             
      PWR2   PAC600S12-CB             Present  Off   Registered   Abnormal  NA             
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display device all** command output
| Item | Description |
| --- | --- |
| Slot | Slot ID. |
| Card | Card ID. |
| Type | Component type. |
| Online | Whether a component is running properly:   * Present: The component is running properly. * Offline: The component is not running properly or is isolated. |
| Power | Whether a component is powered on:   * On: The component is powered on. * Off: The component is not powered on.   "-" indicates the component power-on status cannot be obtained. The status may be caused by the following situations:   * The component is not registered or the registration fails. If the component is not registered, check again after the component is registered. If the registration fails, rectify the fault according to the troubleshooting manual. * The component is just registered, and the power-on status is not reported. Wait a moment and check again. |
| Register | Whether a component is registered:   * Registered: The component has been registered successfully. * Unregistered: The component fails to be registered. |
| Alarm | Component running status:   * -Abnormal: indicates that a major or critical hardware alarm exists in the slot corresponding to the component. You can run the display device alarm hardware command to view hardware alarms. * Normal: The component is running properly. * WrongType: The currently installed component model conflicts with the preconfigured model. * "- ": indicates that the component running status cannot be obtained. |
| Primary | Master/Slave status of the device. The master device, slave device, and other devices are in Master, Slave, and NA states respectively. |