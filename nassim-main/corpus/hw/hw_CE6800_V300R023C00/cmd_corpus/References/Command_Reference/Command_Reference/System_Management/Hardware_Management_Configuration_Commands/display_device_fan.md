display device fan
==================

display device fan

Function
--------



The **display device fan** command displays fan information, such as whether a fan is installed, the fan status (normal or faulty), the fan speed, and the fan mode (automatic or manual).




Format
------

**display device fan**


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

You can run this command to check fan information, such as whether each fan is in position, fan status (normal or faulty), fan speed, and fan mode (automatic or manual).

**Precautions**

If no fan information is available on the device, the command output is empty.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display fan information.
```
<HUAWEI> display device fan
Fan module:
-----------------------------------------------------------------------------------------------------------------
Slot       FanID      FanNum      Present      Register      Status      Speed        Mode      Airflow Direction
-----------------------------------------------------------------------------------------------------------------
   1       FAN1       [ 1 ]       YES          YES           Normal      43%(10700)   Auto      Front-to-Back
                        1                                                10700
           FAN2       [ 1 ]       YES          YES           Normal      42%(10500)   Auto      Front-to-Back
                        1                                                10500
           FAN3       [ 1 ]       YES          YES           Normal      43%(10600)   Auto      Front-to-Back
                        1                                                10600
           FAN4       [ 1 ]       YES          YES           Normal      42%(10500)   Auto      Front-to-Back
                        1                                                10500
-----------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display device fan** command output
| Item | Description |
| --- | --- |
| Fan module | Detailed information about a fan module. |
| Slot | Slot ID. |
| FanID | Fan ID. |
| FanNum | Number of fans. |
| Present | Whether a fan is present:   * YES. * NO. |
| Register | Whether a fan is registered:   * YES: registered. * NO: not registered. * --: The fan is not present. |
| Status | Fan status:   * Normal. * Abnormal. * --: The fan is not present. |
| Speed | Displays the fan speed, including the average speed of all fans in the fan module and the actual speed of each fan. The unit of the actual speed is revolution/minute. In automatic mode, the average rotational speed is the average value of the percentage of the rotational speed to the full speed or the average value of the actual rotational speed. In manual mode, the average fan speed is the manually set fan speed percentage. |
| Mode | Fan mode:   * Auto: The fan speed is automatically adjusted. * Manual: The fan rotates at a fixed speed. * --: The fan is not present. |
| Airflow Direction | Air flow direction of the fan:   * Left-to-Right: Air flows from left to right. * Right-to-Left: Air flows from right to left. * Back-to-Front: Air flows from back to front. * Front-to-Back: Air flows from the front to the rear. * --: The fan module cannot be detected. |