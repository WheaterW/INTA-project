display device power
====================

display device power

Function
--------



The **display device power** command displays the power supply status of a device.

The **display device power verbose** command displays the detailed power supply status of a device.




Format
------

**display device power** [ **verbose** ]


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

During routine maintenance, you can run this command to view the status of power modules.

**Precautions**

1. When the device has only built-in power modules without power module information:

* The **display device power** command output displays "Power state: Normal."
* The **display device power verbose** command output is empty.

1. When the device is not started stably or the power supply is not stable, the power supply status may not be displayed. In this case, real-time data such as the voltage, current, and power of the power supply is displayed as N/A.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the detailed power supply status.
```
<HUAWEI> display device power verbose
------------------------------------------------------------------------------------
Slot   PowerNo  Present Mode State     Current    Voltage   ActualPower   RatedPower
                                       (Ampere)   (Volt)    (Watts)       (Watts)   
------------------------------------------------------------------------------------
1      PWR1     YES     AC   Supply        9.6       12.1           116          600
       PWR2     YES     AC   Supply       13.1       12.0           158          600
------------------------------------------------------------------------------------
Power last power-off info:                      
--------------------------------------------------------------------------------
Slot   PowerNo  Time                            Reason                          
--------------------------------------------------------------------------------
1      PWR1     2022-05-31 01:34:29             Non Input Failure               
       PWR2     2022-05-31 01:34:29             Non Input Failure               
--------------------------------------------------------------------------------
Power supply details:                           
------------------------------------------------
Slot   PowerNo  Type InputVoltage     InputPower
                     (Volt)           (Watts)   
------------------------------------------------
1      PWR1     AC          220.0            133
       PWR2     AC          219.0            176
------------------------------------------------

```

# Display power supply information.
```
<HUAWEI> display device power
------------------------------------------------------------------------------------
Slot   PowerNo  Present Mode State     Current    Voltage   ActualPower   RatedPower
                                       (Ampere)   (Volt)    (Watts)       (Watts)
------------------------------------------------------------------------------------
1      PWR1     YES     AC   Supply        9.8       12.0           118          600
       PWR2     YES     AC   Supply       13.4       12.0           159          600
------------------------------------------------------------------------------------
internal fan info:
-------------------------------------------
Slot   PowerNo  FanExist  Airflow Direction
-------------------------------------------
1      PWR1     YES       Back-to-Front
       PWR2     YES       Back-to-Front
-------------------------------------------

```

**Table 1** Description of the **display device power** command output
| Item | Description |
| --- | --- |
| PowerNo | Power module number. |
| Present | Whether the power module is in position:   * YES: The power module is present. * NO: The power module is not present. |
| Mode | Power supply mode:   * DC. * AC. |
| State | Power supply status:   * NotSupply: No current is output. * Supply: There is current output. |
| Power last power-off info | Last power-off information. |
| Time | Date and time of the last power failure of the power module. |
| Reason | Cause of the last power failure of the power module:   * Input Failure: Input undervoltage or input power failure. * Non Input Failure: Non input failure. |
| Type | Power module type. |
| Slot | Power slot. |
| internal fan info | Information about the built-in fan of the power module. |
| FanExist | Whether the fan module exists:   * YES: The fan module exists. * NO: The fan module does not exist. |
| Airflow Direction | Wind direction of the fan:   * Back-to-Front. * Front-to-Back. |
| Current(Ampere) | Current of the power supply, in ampere (A). |
| Voltage(Volt) | Voltage of the power supply, in volt (V). |
| ActualPower(Watts) | Real-time power of the power supply, in watts. If the power component has no real-time power, -- is displayed. |
| RatedPower(Watts) | Rated power of the power supply, in watts (W). |
| InputPower(Watts) | Input power of the power supply, in watts (W). |
| InputVoltage(Volt) | Input voltage of the power supply, in volt (V). |