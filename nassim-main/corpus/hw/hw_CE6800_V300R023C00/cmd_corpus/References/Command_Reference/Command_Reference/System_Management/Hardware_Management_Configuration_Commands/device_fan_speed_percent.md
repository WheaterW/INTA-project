device fan speed percent
========================

device fan speed percent

Function
--------



The **device fan speed percent** command sets the fan speed.

The **undo device fan speed percent** command restores the fan speed adjustment mode to automatic.



By default, the fan speed adjustment mode is automatic.


Format
------

**device fan speed percent** *percent-num*

**undo device fan speed percent** [ *percent-num* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **percent** *percent-num* | Specifies the percentage of the current fan speed to the full fan speed. | The value is an integer, and the value range depends on the device configuration. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When the board temperature is too high or the fan generates loud noise, you can run this command to manually adjust the fan speed.The fan speed modes are as follows:

* Automatic mode: The fan speed is automatically adjusted based on the board temperature. This mode is used by default or when the set fan speed is canceled.
* Manual mode: The fan speed is set using the command.

**Precautions**



This command does not take effect for the power module. Only the minimum speed can be configured for power module.




Example
-------

# Set the fan speed to 80% of the full speed of all fans.
```
<HUAWEI> system-view
[~HUAWEI] device fan speed percent 80

```