display device temperature
==========================

display device temperature

Function
--------



The **display device temperature** command displays the slot temperature.




Format
------

**display device temperature** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Slot ID. | The value is a string of 1 to 49 case-insensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

This command displays temperature information. During routine maintenance, you can run this command to check whether the temperature of the device is normal.

**Precautions**

If the temperature of the power module on some devices can be obtained, the power module temperature information is additionally displayed.If some devices support the low temperature threshold, the low temperature threshold is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the temperature of a specified slot.
```
<HUAWEI> display device temperature slot 1
  Base-Board, Unit: celsius, Slot 1, Fru 0
------------------------------------------------------------------------------------------------------
BoardType          SensorID  SensorName       Status      Minor  Major  Fatal  FanTMin  FanTMax  Temp
------------------------------------------------------------------------------------------------------
CE6866-48S8CQ-P             1  TEMP_A           Normal         70     75     85       57       60    38
CE6866-48S8CQ-P             2  TEMP_B           Normal         70     75     85       62       65    47
CE6866-48S8CQ-P             3  CPU              Normal        103    108    115       67       70    39
CE6866-48S8CQ-P             4  NP0              Normal        103    108    115       92       95    55
CE6866-48S8CQ-P             5  NP1              Normal        103    108    115       92       95    55
......
------------------------------------------------------------------------------------------------------

```

# Display the device's temperature information.
```
<HUAWEI> display device temperature
  Base-Board, Unit: celsius, Slot 1, Fru 0
------------------------------------------------------------------------------------------------------
BoardType          SensorID  SensorName       Status      Minor  Major  Fatal  FanTMin  FanTMax  Temp
------------------------------------------------------------------------------------------------------
CE6866-48S8CQ-P              1  TEMP_0           Normal        110    115    120       99      101    46
CE6866-48S8CQ-P              2  CDR0             Normal        108    117    125       94       96    40  
...... 
------------------------------------------------------------------------------------------------------
......

```

**Table 1** Description of the **display device temperature** command output
| Item | Description |
| --- | --- |
| Slot | Slot information. |
| Fru | Card number information. |
| BoardType | Type of an electronic label. |
| SensorID | Sensor number. |
| SensorName | Sensor name. |
| Status | Current status. |
| Minor | Upper threshold for minor alarms. |
| Major | Upper threshold for a major temperature alarm. |
| Fatal | Upper threshold for fatal temperature alarms. |
| FanTMin | Target speed adjustment parameter, which is meaningless and does not take effect.  This field is not displayed for models that do not support fans. |
| FanTMax | Indicates the target speed adjustment parameter. When the temperature is greater than or equal to FanTMax, the fan speed is increased. When the temperature is lower than FanTMax-2, the fan speed is decreased.  This field is not displayed for models that do not support fans. |
| Temp | Current temperature. |