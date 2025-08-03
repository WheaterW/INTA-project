device power over-current-protect
=================================

device power over-current-protect

Function
--------



The **device power over-current-protect** command disables overcurrent protection for the power supply.

The **undo device power over-current-protect** command restores overcurrent protection of the power supply.



By default, overcurrent protection is enabled.


Format
------

**device power over-current-protect disable**

**undo device power over-current-protect disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **disable** | Disables overcurrent protection for the power supply. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



After overcurrent protection for the power supply is enabled on a device, if the current of a power module exceeds the rated current, the power module stops supplying power to the device.




Example
-------

# Disable overcurrent protection for the power supply.
```
<HUAWEI> system-view
[~HUAWEI] device power over-current-protect disable

```