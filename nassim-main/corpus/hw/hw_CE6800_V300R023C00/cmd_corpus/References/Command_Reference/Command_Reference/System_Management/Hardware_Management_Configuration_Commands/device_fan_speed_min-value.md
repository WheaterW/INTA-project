device fan speed min-value
==========================

device fan speed min-value

Function
--------



The **device fan speed min-value** command sets the minimum fan speed.

The **undo device fan speed min-value** command restores the default fan configuration.



By default, the minimum fan speed is not set.


Format
------

**device fan speed min-value percent** *percent-num*

**undo device fan speed min-value percent** [ *percent-num* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **percent** *percent-num* | Specifies the minimum fan speed, in percentage. For example, if percent-number is set to 50, the minimum fan speed is 50% of the full speed. | The value is an integer, and the value range depends on the device configuration. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The fan speed affects the device temperature. When the device temperature is high, increase the fan speed to lower the device temperature. When the device temperature is low, reduce the fan speed to save energy. By default, the system automatically adjusts the fan speed to keep the device temperature proper. You can run the **device fan speed min-value** command in the system view to set a minimum fan speed. In this way, the system can automatically adjust the fan speed to a value that is not lower than the minimum fan speed.You can also run the **device fan speed percent** command to set the fan speed.

**Precautions**



This command does not take effect for the power module. To set the minimum speed for the power module, run the **device power fan-speed min-value** command in the system view.




Example
-------

# Set the minimum fan speed to 50% of the full speed for all fans.
```
<HUAWEI> system-view
[~HUAWEI] device fan speed min-value percent 50

```