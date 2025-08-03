device power fan-speed min-value
================================

device power fan-speed min-value

Function
--------



The **device power fan-speed min-value** command sets the percentage of the minimum fan speed to the full fan speed for power modules.

The **undo device power fan-speed min-value** command restores the default minimum fan speed for all power modules.



By default, the minimum fan speed is 20% of the full fan speed for a power module.


Format
------

**device power fan-speed min-value percent** *percent-num*

**undo device power fan-speed min-value percent** [ *percent-num* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **percent** *percent-num* | Specifies the minimum fan speed percentage for power modules. For example, if percent-num is set to 50, the minimum fan speed is 50% of the full fan speed. | The value is an integer ranging from 20 to 100. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



The fan speed of the power module affects the temperature of the power module. By default, the system automatically adjusts the fan speed of the power supply to ensure that the power supply works at a stable temperature. You can run the **device power fan-speed min-value** command in the system view to set the minimum fan speed for a power module. In this way, the system can automatically adjust the fan speed to ensure that the fan speed is not lower than the minimum speed.



**Precautions**



This command takes effect only for power modules with fans. You can run the display device power command to check whether a power module has fans.




Example
-------

# Set the minimum speed of all power module fans to 50% of the full speed of the power module fans.
```
<HUAWEI> system-view
[~HUAWEI] device power fan-speed min-value percent 50

```