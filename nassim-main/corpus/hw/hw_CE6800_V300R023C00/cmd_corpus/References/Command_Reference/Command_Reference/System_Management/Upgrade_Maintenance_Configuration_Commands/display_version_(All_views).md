display version (All views)
===========================

display version (All views)

Function
--------



The **display version** command displays the device version.




Format
------

**display version**


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

You can run this command to check the current version of the device and determine whether the device needs to be upgraded.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the current system version.
```
<HUAWEI> display version
Huawei Versatile Routing Platform Software
YunShan OS, Version 1.23.0.X (CE6800 V300R023C00)
Copyright (C) 2021-2023 Huawei Technologies Co., Ltd.
HUAWEI CE6866-48S8CQ-P uptime is 0 day, 5 hours, 32 minutes
Patch Version: XXX

XXX (Master) 1 : uptime is  1 day, 22 hours, 35 minutes
        StartupTime XXXX/XX/XX   11:21:03
Memory      Size    : 16384 M bytes
Flash       Size    : 4096 M bytes
XXX version information:
1.PCB       Version : XXX
2.MAB       Version : 0
3.Board     Type    : XXX
4.BIOS      Version : 1906
5.CPLD1     Version : 256
  CPLD2     Version : 256

```
```
<HUAWEI> display version         //V300R023C00 and later versions.
Huawei Versatile Routing Platform Software
YunShan OS, Version 1.23.0.X (CloudEngine 58&68&78&88&98 V300R023C00)
Copyright (C) 2021-2023 Huawei Technologies Co., Ltd.
HUAWEI CE6866-48S8CQ-P uptime is 0 day, 5 hours, 32 minutes
Patch Version: XXX

XXX (Master) 1 : uptime is  1 day, 22 hours, 35 minutes
        StartupTime XXXX/XX/XX   11:21:03
Memory      Size    : 16384 M bytes
Flash       Size    : 4096 M bytes
XXX version information:
1.PCB       Version : XXX
2.MAB       Version : 0
3.Board     Type    : XXX
4.BIOS      Version : 1906
5.CPLD1     Version : 256
  CPLD2     Version : 256

```

**Table 1** Description of the **display version (All views)** command output
| Item | Description |
| --- | --- |
| Copyright (C) 2021-2023 Huawei Technologies Co., Ltd. | Copyright statement of Huawei. |
| uptime | HUAWEI XXX uptime indicates the running time of the device.  Other uptime indicates the registration time of the board. |
| Patch Version | Patch version. |
| StartupTime | System power-on time. |