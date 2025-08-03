license switch mode
===================

license switch mode

Function
--------



The **license switch mode** command switches the license mode to a specified mode.



By default, the device works in non-cloud-based license mode.


Format
------

**license switch** { **common** | **cloud** } **mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **common** | Specifies the traditional license mode. | - |
| **cloud** | Specifies the cloud license mode. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If the device needs to use cloud license resources, run the **license switch cloud mode** command to switch to the cloud mode and then apply for resources from the cloud license server. You can also run the **license switch common mode** command to switch the device to the non-cloud mode and use the resources in the non-cloud license file.

**Precautions**

Before switching the license mode of a device to the cloud mode, ensure that no license file is activated on the device or the activated license file has been revoked.To switch the license mode of a device to the non-cloud mode, ensure that no cloud license is allocated to the device or the allocated license resources have been invalidated.


Example
-------

# Switch to cloud mode.
```
<HUAWEI> license switch cloud mode
Warning: This operation will switch to the cloud mode. Continue? [Y/N]:Y
Info: Succeeded in switching to the cloud mode.

```

# Switch to common mode.
```
<HUAWEI> license switch common mode
Warning: This operation will switch to the common mode. Continue? [Y/N]:Y
Info: Succeeded in switching to the common mode.

```