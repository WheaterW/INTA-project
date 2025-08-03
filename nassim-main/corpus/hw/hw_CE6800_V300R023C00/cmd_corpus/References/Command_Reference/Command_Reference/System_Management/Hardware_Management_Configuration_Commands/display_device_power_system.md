display device power system
===========================

display device power system

Function
--------



The **display device power system** command displays power information of a device.




Format
------

**display device power system**


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

During routine maintenance, you can run this command to check the power of the device.

**Precautions**

1. If no power supply information is displayed on the device, the command output is empty.
2. When the device is not started stably or the power supply is not stable, the power supply status may not be displayed. In this case, real-time data such as the voltage, current, and power of the power supply is displayed as N/A.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the power information of a device.
```
<HUAWEI> display device power system
Average power consumption: 64 W                                                     
Current power consumption: 64 W                                                     
Power manage cycle: 1 hour                                                          
Power manage switch: Off                                                            
                                                                                    
Power Supply Module Information:                                                    
------------------------------------------------------------------------------------
Slot   PowerNo  Present Mode State     Current    Voltage   ActualPower   RatedPower
                                       (Ampere)   (Volt)    (Watts)       (Watts)   
------------------------------------------------------------------------------------
1      PWR1     YES     AC   Supply        3.1       12.0            37          600
       PWR2     YES     AC   Supply        2.3       12.0            27          600
------------------------------------------------------------------------------------
                                                                                    
Board Power Information:
---------------------------------------------------------------
Slot  Card  BoardType            State  ActualPower  RatedPower
                                        (Watts)      (Watts)
---------------------------------------------------------------
1     --   CE6866-48S8CQ-P      On              61         291

```

**Table 1** Description of the **display device power system** command output
| Item | Description |
| --- | --- |
| Average power consumption | Indicates the average power of the device, in watts. |
| Current power consumption | Current power of the device, in watts. |
| Power manage cycle | Interval for updating the power consumption data of the device.   * 15 minutes. * 30 minutes. * 1 hour. * 1 day. * 1 week. * 1 month.   To set the interval for updating power consumption data, run the device power manage cycle command. |
| Power manage switch | Energy saving status of the device:   * On: The function is enabled. * Off: The function is disabled. |
| Power Supply Module Information | Power supply information on the power module. |
| PowerNo | Power module number. |
| Present | Whether the power module is present:   * YES: The power module is present. * NO: The power module is not present. |
| Mode | Power supply mode:   * DC. * AC. |
| State | Power supply status:   * NotSupply: There is no current output. * Supply: There is current output. |
| State | Power-on status of a component.   * On: The board is powered. * Off: The board is not powered on. |
| Board Power Information | Power information of a board. |
| Slot | Slot ID of a component. |
| BoardType | Component type. |
| Card | Subcard number. |
| Current(Ampere) | Current of the power supply, in amperes. If a power component has no real-time current, -- is displayed. |
| Voltage(Volt) | Voltage of the power supply, in volt. |
| ActualPower(Watts) | Real-time power of the power supply, in watts. If the power component has no real-time power, -- is displayed. |
| RatedPower(Watts) | Rated power of a power module, in watt. |
| ActualPower(Watts) | Real-time power of a component, in watts. If a board or fan has no real-time power, -- is displayed. |
| RatedPower(Watts) | Rated power of a component, in watts (W). |