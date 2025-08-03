display device id-led
=====================

display device id-led

Function
--------



The **display device id-led** command displays the ID indicator status.




Format
------

**display device id-led**


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



You can use the **display device id-led** command to view the status information of the current device ID indicator.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the status of the device ID indicator.
```
<HUAWEI> display device id-led
ID-LED Status:
  On  - LED is turned on to help find the device.
  Off - LED is turned off.
  -   - LED is not supported on the device.
--------------------------------------------
Slot   Type               ID-LED Status
--------------------------------------------
1     CE6866-48S8CQ-P       On

```

**Table 1** Description of the **display device id-led** command output
| Item | Description |
| --- | --- |
| ID-LED Status | LED status:   * On: The ID indicator is steady on. * Off: The ID indicator is off. * -: The device does not support the ID indicator. |
| Slot | Slot ID. |
| Type | Hardware type. |