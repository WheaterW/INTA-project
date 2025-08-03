display oas application
=======================

display oas application

Function
--------



The **display oas application** command displays information about all created applications.




Format
------

**display oas application** [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Displays the application details. | - |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

* You can run the **display oas application** command to view information about all created applications.
* You can run the **display oas application verbose** command to view details about all created applications.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about all created applications.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] display oas application verbose
Application information:
--------------------------------------------------------------------------------
Application Name        : mpu1
Slot ID                 : 5
Software Name           : oasImages
Running State           : running
CPU ID                  : 0
Container ID            : 6f00afe58d7d
Container PIDS          : 21
Runtime Options         : --cpus 3 --blkio-weight 26
Memory Usage / Limits   : 106MiB / 7.55GiB
Memory Using Percentage : 1.37%
CPU Using Percentage    : 2.14%
Net I/O                 : 260MB / 1.79GB
Block I/O               : 38.9MB / 4.1kB
--------------------------------------------------------------------------------
[~HUAWEI-oas]

```

# Display information about all created applications.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] display oas application
----------------------------------------------------------------------------------------------------------
Application Name                 Slot ID              Software Name                    Running State
----------------------------------------------------------------------------------------------------------
mpu1                             5                    oasImages                        running
----------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display oas application** command output
| Item | Description |
| --- | --- |
| Application Name | Application name. |
| Slot ID | Slot ID. |
| Software Name | Image software package. |
| Running State | Application running status. |
| CPU ID | CPU ID. |
| CPU Using Percentage | CPU usage. |
| Container ID | Container ID. |
| Container PIDS | Process ID of a container. |
| Runtime Options | Run-time options. |
| Memory Usage / Limits | Memory usage/limit. |
| Memory Using Percentage | Memory usage. |
| Net I/O | Network I/O. |
| Block I/O | Block I/O. |