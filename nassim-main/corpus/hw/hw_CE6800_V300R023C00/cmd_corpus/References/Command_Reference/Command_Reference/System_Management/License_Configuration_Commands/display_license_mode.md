display license mode
====================

display license mode

Function
--------



The **display license mode** command displays the license mode of a device.




Format
------

**display license mode**


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

In terms of the license management mode, licenses are classified as cloud licenses or non-cloud licenses. This command displays the license mode of the device.

* In cloud license mode, you can activate and manage a license resource pool on the license management platform to dynamically allocate and reclaim license control items among multiple devices registered in the resource pool, implementing license resource sharing and dynamic adjustment among multiple devices.
* The non-cloud license mode is the traditional standalone license mode, in which the license resources of each device are static and fixed. To adjust license resource allocation among devices, you need to split the license and perform activation again.

**Precautions**

The device is the common mode by default. The device can switch to common mode or cloud mode.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the license mode of the device.
```
<HUAWEI> display license mode
 License mode      : cloud

```

**Table 1** Description of the **display license mode** command output
| Item | Description |
| --- | --- |
| License mode | License mode:   * cloud: cloud license. * common: non-cloud license. |