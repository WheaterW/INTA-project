display eva fault
=================

display eva fault

Function
--------



The **display eva fault** command displays fault data managed by the EVA.




Format
------

**display eva fault** [ **unrecovered** | **recovered** ] [ *object* ] [ *beginTime* *endTime* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **unrecovered** | Indicates the information about unresolved faults. | - |
| **recovered** | Indicates the information about resolved faults. | - |
| *object* | Indicates the name of a fault object. | The value is a string of 1 to 31 case-insensitive characters. |
| *beginTime* | Indicates the start time for querying fault data. The time is the local time in the 24-hour format. | The format is in YYYY/MM/DD plus HH:MM:SS or YYYY-MM-DD plus HH:MM:SS.  YYYY/MM/DD indicates year/month/day, and YYYY-MM-DD indicates year-month-day. YYYY ranges from 1970 to 9999, MM ranges from 1 to 12, and DD ranges from 1 to 31.  HH:MM:SS indicates hour:minute:second. HH ranges from 0 to 23, and MM and SS range from 0 to 59. |
| *endTime* | Indicates the end time for querying fault data. The time is the local time in the 24-hour format. | The format is in YYYY/MM/DD plus HH:MM:SS or YYYY-MM-DD plus HH:MM:SS.  YYYY/MM/DD indicates year/month/day, and YYYY-MM-DD indicates year-month-day. YYYY ranges from 1970 to 9999, MM ranges from 1 to 12, and DD ranges from 1 to 31.  HH:MM:SS indicates hour:minute:second. HH ranges from 0 to 23, and MM and SS range from 0 to 59. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

To view fault data managed by the EVA, run this command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display fault data.
```
<HUAWEI> display eva fault
2021-09-24 14:46:07.895                                                                                                             
Total: 4                                                                                                                            
------------------------------------------------------------------------------------------------------------------------------------
OccurTime           RecoverTime         FaultPattern    ObjectLevel      Object     Description                                     
------------------------------------------------------------------------------------------------------------------------------------
2021-09-24 14:37:13 -                   VCMU.POWER.002  DEVICE_POWER     POWER8     The B plane power supply on the power module is 
faulty.                                                                                                                             
2021-09-24 14:37:13 -                   VCMU.POWER.002  DEVICE_POWER     POWER9     The power module supply failed.                 
2021-09-24 14:37:17 -                   VCMU.POWER.002  DEVICE_POWER     POWER1     The power type does not match the type of the ba
ckplane.                                                                                                                            
2021-09-24 14:37:13 -                   VCMU.POWER.002  DEVICE_POWER     POWER10    The B plane power supply on the power module is 
faulty.                                                                                                                             
------------------------------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display eva fault** command output
| Item | Description |
| --- | --- |
| OccurTime | Time when the fault occurred. |
| RecoverTime | Time when the fault was rectified. |
| FaultPattern | Fault mode. |
| ObjectLevel | Level of a fault object. |
| Object | Name of a fault object. |
| Description | Fault description. |
| Total | Total number of records. |