display version slot
====================

display version slot

Function
--------



The **display version slot** command displays the version of the device in specified slot.




Format
------

**display version slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 49 case-insensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can use the display version slot command to view the version of the device in specified slot to determine whether the device needs to be upgraded.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the version of the board in a specified slot.
```
<HUAWEI> display version slot 0
Chassis ID: 1 (Master Switch)

MPU(Master) 0 : uptime is  0 day, 0 hour, 40 minutes
        StartupTime 2022/06/30   17:22:00
Memory      Size    : 16384 M bytes
Flash       Size    : 4096 M bytes
MPU version information:
1.PCB       Version : XXXX
2.MAB       Version : 0
3.Board     Type    : XXXX
4.BIOS      Version : 673
5.CPLD1     Version : 272
  CPLD2     Version : 272

```

**Table 1** Description of the **display version slot** command output
| Item | Description |
| --- | --- |
| uptime | System power-on time. |
| StartupTime | System startup time. |
| Memory Size | Total system memory size. |
| Flash Size | Total flash memory size. |
| PCB Version | Version of a printed circuit card. |
| MAB Version | Version of a manufactured card. |
| Board Type | Device type. |
| BIOS Version | BIOS version. |
| CPLD Version | CPLD version. |
| FPGA Version | FPGA version. |