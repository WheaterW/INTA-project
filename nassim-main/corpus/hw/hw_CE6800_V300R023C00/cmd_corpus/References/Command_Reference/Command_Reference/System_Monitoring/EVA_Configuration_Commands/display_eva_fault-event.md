display eva fault-event
=======================

display eva fault-event

Function
--------



The **display eva fault-event** command displays EVA events and strategy matching information.




Format
------

**display eva fault-event** [ *fileName* ] { **matched** | **unmatched** | **all** } [ *beginTime* *endTime* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *fileName* | Specify the name of an EVA script. | The value is a string of 2 to 31 case-sensitive characters, starting with a letter and containing only digits, letters, and underscores (\_). It cannot contain spaces.   * The file name extension of an EVA script in Python format is .py. * The .json file name extension is not required for an EVA script in JSON format. |
| **matched** | Specifies the matched policy. | - |
| **unmatched** | Specifies the policy that is not matched. | - |
| **all** | Specifies all policies. | - |
| *beginTime* | Specifies the start time. The value is a local time in the 24-hour format of YYYY/MM/DD,HH:MM:SS or YYYY-MM-DD,HH:MM:SS and within last seven days. | The format is YYYY/MM/DD,HH:MM:SS,YYYY-MM-DD,HH:MM:SS. YYYY/MM/DD and YYYY-MM-DD indicate year/month/day and year-month-day, respectively. The value of YYYY ranges from 1970 to 9999; the value of MM ranges from 1 to 12; the value of DD ranges from 1 to 31. HH:MM:SS indicates hour:minute:second. The value of HH ranges from 0 to 23; the values of MM and SS range from 0 to 59. |
| *endTime* | Specifies the end time. The value is a local time in the 24-hour format of YYYY/MM/DD,HH:MM:SS or YYYY-MM-DD,HH:MM:SS and within last seven days. | The format is YYYY/MM/DD,HH:MM:SS,YYYY-MM-DD,HH:MM:SS. YYYY/MM/DD and YYYY-MM-DD indicate year/month/day and year-month-day, respectively. The value of YYYY ranges from 1970 to 9999; the value of MM ranges from 1 to 12; the value of DD ranges from 1 to 31. HH:MM:SS indicates hour:minute:second. The value of HH ranges from 0 to 23; the values of MM and SS range from 0 to 59. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can run this command to view events defined in an EVA script and strategy matching information.If the filename parameter is not specified, event information about all registered scripts is queried.If the begintime and endtime parameters are not specified, event information at all time is queried.If the filename, begintime, and endtime parameters are specified, event information in the specified time segment of the script is queried.If the matched parameter is specified, the event that matches a strategy is queried.If the unmatched parameter is specified, the event that does not match a strategy is queried.If the all parameter is specified, all events (including matched and unmatched events) are queried.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display events defined in the EVA script and policy strategy information.
```
<HUAWEI> display eva fault-event matched  2020-01-02,19:20:30 2020-01-02,20:30:30
Total:1
--------------------------------------------------------------------------------                                                    
Time                 FileName     EventName       Value Strategy   Entity                                                           
--------------------------------------------------------------------------------                                                    
2020-01-02 19:34:46  cpu_high.py e1              3.000 s1         e1.cpu-id=0,e1.slot-id=1                                      
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display eva fault-event** command output
| Item | Description |
| --- | --- |
| Time | Time when an event occurs. |
| FileName | * Script file name for an EVA script in Python format. * Script name for an EVA script in JSON format. |
| EventName | Event name. |
| Value | KPI value when the event occurs, "-" means not involved. |
| Strategy | Strategy matching status.   * Indicates the currently matched strategy. * ops: event subscribed by the OPS. * unmatched: The strategy is not matched. * unmatched(self-recovery): The fault is rectified, and the strategy is not matched. * matching: The strategy is being matched. * Python file delete: The Python file is deleted. |
| Entity | Currently matched entity, "-" means not involved. |
| Total | Total number of records. |