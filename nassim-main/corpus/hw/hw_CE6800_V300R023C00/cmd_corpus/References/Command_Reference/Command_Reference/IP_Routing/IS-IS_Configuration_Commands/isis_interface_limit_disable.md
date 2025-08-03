isis interface limit disable
============================

isis interface limit disable

Function
--------



The **isis interface limit disable** command disables the limit on the number of IS-IS interfaces that can be configured on a device.

The **undo isis interface limit disable** command restores the default configuration.



By default, the number of IS-IS interfaces that can be configured on a device is limited.


Format
------

**isis interface limit disable**

**undo isis interface limit disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, each network product model can customize a threshold to limit the number of IS-IS interfaces that can be configured on a device. Run the **isis interface limit disable** command to remove the limit on the number of IS-IS interfaces that can be configured on the device. After this command is run, the number of IS-IS interfaces is no longer limited to the device threshold. Run the **undo isis interface limit disable** command to restore the maximum number of IS-IS interfaces that can be configured on a device. If the number of IS-IS interfaces on the device is greater than or equal to the threshold, no IS-IS interface can be added.

**Precautions**

Each device model may have a specified threshold to limit the number of IS-IS interfaces that can be configured on the device. This threshold cannot exceed the default of 6000.By default, the threshold is not checked during device configuration restoration. This ensures that the isis enable and isis ipv6 enable configurations are not lost after the device is upgraded from the source version to the target version. In the target version, if the number of configured IS-IS interfaces exceeds the threshold, new interfaces cannot be configured until the **isis interface limit disable** command is run.If the **isis interface limit disable** command is not configured, the number of IS-IS interfaces that can be configured on each device cannot exceed the threshold. After the **isis interface limit disable** command is run, a maximum of 16384 IS-IS interfaces can be configured on each device.


Example
-------

# Disable the limit on the number of IS-IS interfaces that can be configured on a device.
```
<HUAWEI> system-view
[~HUAWEI] isis interface limit disable

```