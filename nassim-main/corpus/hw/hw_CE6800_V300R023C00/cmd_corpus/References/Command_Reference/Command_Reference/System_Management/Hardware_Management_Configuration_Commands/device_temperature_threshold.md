device temperature threshold
============================

device temperature threshold

Function
--------



The **device temperature threshold** command sets the temperature alarm threshold of a board.

The **undo device temperature threshold** command restores the default temperature alarm threshold of a board.



By default, the temperature alarm threshold of a board varies according to the hardware used by the device.


Format
------

**device temperature threshold slot** *slot-id* **sensor** *sensor-id* **minor** *minor-value* **major** *major-value* **fatal** *fatal-value* [ **tmin** *tmin-value* **tmax** *tmax-value* ]

**undo device temperature threshold slot** *slot-id* **sensor** *sensor-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **sensor** *sensor-id* | Specifies the ID of a sensor. | The value is an integer. You can enter a question mark (?) and select a value from the displayed value range. |
| **minor** *minor-value* | Specifies the minor overtemperature alarm threshold of a board. | The value is an integer ranging from 80 to 120, in percentage. |
| **major** *major-value* | Specifies the major alarm threshold of a board. | The value is an integer ranging from 80 to 120, in percentage. |
| **fatal** *fatal-value* | Specifies the fatal alarm threshold of a board. | The value is an integer ranging from 80 to 120, in percentage. |
| **tmin** *tmin-value* | Specifies the lowest temperature for fan speed adjustment. | The value is an integer that ranges from -50 to 127, in degrees Celsius. |
| **tmax** *tmax-value* | Specifies the highest temperature for fan speed adjustment. | The value is an integer ranging from â50 to 127, in degrees Celsius. |
| **slot** *slot-id* | Specifies a slot ID. | The value is a character string. You can enter a question mark (?) and select a value as prompted. The value is a string of 1 to 29 case-insensitive characters. It cannot contain spaces. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* To adapt to changes in the external environment, you can run this command to manually adjust the temperature alarm threshold so that the system can detect board temperature changes more accurately and quickly.
* When the fan works in automatic speed adjustment mode, the fan speed can be automatically adjusted according to the board temperature. The adjustment policy varies according to the hardware. The main policies are as follows:Speed adjustment policy 1:
  
  + When the temperature is greater than or equal to tmax-value, the fan speed increases.
  + When the temperature is lower than tmax-value-2, the fan speed decreases.
  
  Speed adjustment policy 2:
  
  + When the temperature is lower than or equal to tmin-value, the fan speed decreases to the lower limit.
  + When the temperature is higher than tmin-value, the fan speed increases with the temperature.
  + When the temperature reaches tmax-value, the fan speed is adjusted to 100%.

**Precautions**

* For models that do not support this function, sensor information is not displayed.
* Only fan models support tmin and tmax.


Example
-------

# Set the minor alarm threshold of boards to 80% of the default minor alarm threshold, the major alarm threshold to 90% of the default major alarm threshold temperature, the fatal alarm threshold to 100% of the fatal alarm threshold, the lowest temperature for adjusting the fan speed to 60°C, and the highest temperature for adjusting the fan speed to 70°C.
```
<HUAWEI> system-view
[~HUAWEI] device temperature threshold slot 1 sensor 1 minor 80 major 90 fatal 100 tmin 60 tmax 70

```