display health (All views)
==========================

display health (All views)

Function
--------



The **display health** command displays the health status of the device.




Format
------

**display health**

**display health verbose**


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

To view information about the device CPU usage and memory usage, run the **display health** command.To view verbose information about the health status of the device run the **display health verbose** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the health status of a device.
```
<HUAWEI> display health
----------------------------------------------------------------------------------------         
Slot                        CPU Usage  Memory Usage(Used/Total)     DataPlane CPU Usage                                             
----------------------------------------------------------------------------------------  
1     MPU(Master)           21%        22%   6084MB/27001MB         0%                      
----------------------------------------------------------------------------------------

```

# Display detailed device health information.
```
<HUAWEI> display health verbose
Voltage:
Base-Board, Unit:volt, Slot 1
---------------------------------------------------------------------------------------------------------------
BoardType          SensorID  SensorName       Status      Require  MajorL  FatalL  MajorH  FatalH   Vlt  ratio
---------------------------------------------------------------------------------------------------------------
CE6866-48S8CQ-P               16  12V              Normal        12.04   10.86      --   13.22      --  0.00   0.17
......
---------------------------------------------------------------------------------------------------------------
Power:
-----------------------------------------------------------------------------
PowerNo  Present Mode State     Current    Voltage   ActualPower   RatedPower
                                (Ampere)   (Volt)    (Watts)       (Watts)
-----------------------------------------------------------------------------
PWR1     YES     AC   Supply        6.6       12.0            79          350
......
-----------------------------------------------------------------------------
internal fan info:
------------------------------------
PowerNo  FanExist  Airflow Direction
------------------------------------
PWR1     --        --
------------------------------------
Fan:
----------------------------------------------------------------------------------------------------
FanID      FanNum      Present      Register      Status      Speed      Mode      Airflow Direction
----------------------------------------------------------------------------------------------------
FAN1       [ 1 ]       YES          YES           Normal      38%(9500)  Auto      Front-to-Back
             1                                                9500
......
----------------------------------------------------------------------------------------------------
Temperature:
  Base-Board, Unit:celsius, Slot 1
------------------------------------------------------------------------------------------------------
BoardType          SensorID  SensorName       Status      Minor  Major  Fatal  FanTMin  FanTMax  Temp
------------------------------------------------------------------------------------------------------
CE6866-48S8CQ-P                  1  AIR_INTAKE       Normal         50     60     70       39       41    30
......
------------------------------------------------------------------------------------------------------
System Memory Usage Information:
Slot: 1   CPU: 0
Total Physical Memory: 27700820 Kbytes
Total Physical Memory Used: 7148360 Kbytes
Physical Memory Using Percentage: 25%
Total Virtual Memory: 49704104 Kbytes
Total Virtual Memory Used: 7338676 Kbytes
Virtual Memory Using Percentage: 14%
State: Unoverload
Overload threshold:  95%, Overload clear threshold:  75%, Duration:   60s
-----------------------------------------------------------------------------------------
System CPU Usage Information:
Slot: 1    CPU:0
CPU utilization statistics at 2020-12-31 16:54:43 786 ms
System CPU Using Percentage :   3%
Dataplane CPU Using Percentage :   0%
CPU utilization for five seconds: 3%, one minute: 2%, five minutes: 2%.
Max CPU Usage :                17%
Max CPU Usage Stat. Time : 2020-12-30 17:23:59 878 ms
State: Unoverload
Overload threshold:  90%, Overload clear threshold:  75%, Duration:   60s
------------------
CPU Usage Details
----------------------------------------------------------------
CPU     Current  FiveSec   OneMin  FiveMin  Max MaxTime
----------------------------------------------------------------
cpu0        26%      26%      25%      25%  99% 2020-12-30 17:24:19
......
----------------------------------------------------------------

```

**Table 1** Description of the **display health (All views)** command output
| Item | Description |
| --- | --- |
| Slot | Indicates the slot ID of the device. |
| CPU utilization for five seconds | Indicates the CPU usage in five seconds. |
| CPU | CPU core. |
| CPU Usage | CPU usage of the system. |
| Memory Usage(Used/Total) | Memory usage (used/total). |
| DataPlane CPU Usage | CPU usage of the data plane. |
| BoardType | Board type. |
| SensorID | Sensor number. |
| SensorName | Sensor name. |
| Status | Current status. |
| Require | Ideal voltage. |
| MajorL | Lower threshold for major alarms of undervoltage. |
| FatalL | Lower threshold for a fatal undervoltage alarm. |
| MajorH | Upper threshold for major overvoltage alarms. |
| FatalH | Upper threshold for fatal overvoltage alarms. |
| Vlt | Current voltage. |
| ratio | Split voltage ratio. |
| PowerNo | Power module number. |
| Present | Whether the power supply is present:   * YES: The power supply is present. * NO: The power supply is not present. |
| Mode | Power supply mode:   * DC: DC power supply. * AC: AC power supply. |
| State | Overload status. |
| Current | Current CPU usage. |
| FanExist | Fan installation status. |
| Airflow Direction | Wnd direction of the fans.   * Back-to-Front: Air flows from back to front. * Front-to-Back: Air flows from front to back. * Left-to-Right: Air flows from left to right. * Right-to-Left: Air flows from right to left. * -: The fan is not present. |
| FanID | Fan ID. |
| FanNum | Number of fans. |
| Register | Whether the fan is registered:   * Registered. * Unregistered. * -: The fan is not present. |
| Speed | Fan speeds, including the average speed of all fans in the fan module and the actual speed of each fan. The actual speed is expressed in rounds per minute. The average fan speed can be expressed as a percentage of the rotation speed against the full speed or the average actual rotation speed. |
| Minor | Upper threshold for minor alarms. |
| Major | Upper threshold for major temperature alarms. |
| Fatal | Upper threshold for fatal temperature alarms. |
| FanTMin | Parameter for target speed adjustment. This parameter is meaningless and does not take effect. |
| FanTMax | Parameter for target speed adjustment. When the temperature is greater than or equal to FanTMax, the fan speed is increased. When the temperature is less than FanTMax - 2, the fan speed is lowered. |
| Temp | Current temperature. |
| System CPU Using Percentage | Indicates the CPU usage of the system. |
| Total Physical Memory | Total physical memory. |
| Total Physical Memory Used | Used physical memory. |
| Total Virtual Memory | Total virtual memory. |
| Total Virtual Memory Used | Used virtual memory. |
| Physical Memory Using Percentage | Physical memory usage. |
| Virtual Memory Using Percentage | Virtual memory usage. |
| Overload threshold | Overload threshold. |
| Overload clear threshold | Overload clearance threshold. |
| five minutes | Indicates the CPU usage within 5 minutes. |
| one minute | Indicates the CPU usage within one minute. |
| Max CPU Usage | Maximum CPU usage. |
| Max CPU Usage Stat. Time | Time when the maximum CPU usage is collected. |
| Max | Maximum CPU usage. |
| Time | Date and time when the power board was powered off the last time. |
| FiveSec | CPU usage per 5 seconds. |
| OneMin | Average CPU core usage within one minute. |
| FiveMin | Average CPU core usage within 5 minutes. |
| MaxTime | Time when the maximum CPU usage occurs. |
| Fan | Indicates fan information. For details, see the display device fan command output. |
| Temperature | Indicates temperature information. For details, see the display device temperature command output. |
| Duration | Measurement interval. |
| Current(Ampere) | Current of the power supply, in amperes. |
| Voltage(Volt) | Voltage of the power supply, in V. |
| ActualPower(Watts) | Real-time power of the power supply, in watts. |
| PCB | Component name. |
| RatedPower(Watts) | Rated power of a power module, in W. |