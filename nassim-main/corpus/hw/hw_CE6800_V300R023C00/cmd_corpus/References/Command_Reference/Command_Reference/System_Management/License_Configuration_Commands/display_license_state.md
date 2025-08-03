display license state
=====================

display license state

Function
--------



The **display license state** command displays the status of a license file in the current system.




Format
------

**display license state**


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

To check the status of a license file running in the system, run this command. The command output contains the current license status and the remaining validity period of the license in this status.

**Prerequisites**

An active license file exists on the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the status of a license file in the current system.
```
<HUAWEI> display license state
Info: Current license state is Demo. The license for the current configuration will expire in 4 day(s).

```

**Table 1** Description of the **display license state** command output
| Item | Description |
| --- | --- |
| state | * Demo: trial state. * Normal: indicates the normal state. * Default: The device is in the default state when no license is authorized. If no license file is activated after delivery or the license is not reactivated after the grace period expires, the license is in this state. * Trial: indicates the keep-alive state. * Emergency: emergency state. |
| Info | License status. |