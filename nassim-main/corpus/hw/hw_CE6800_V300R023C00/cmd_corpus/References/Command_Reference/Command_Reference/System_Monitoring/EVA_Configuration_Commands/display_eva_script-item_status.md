display eva script-item status
==============================

display eva script-item status

Function
--------



The **display eva script-item status** command displays the running status of EVA scripts.




Format
------

**display eva script-item status**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can run this command to query the running status of EVA scripts. If a script has been executed and uninstalled, the script running status cannot be queried.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the script running status.
```
<HUAWEI> display eva script-item status
Inspection running status: running
----------------------------------------------------------------------------------------------------------------
Script                Type            RegisterTime           Status         LastExecTime            Result
---------------------------------------------------------------------------------------------------------------
SystemExceptionCheck  Build-in        2021-01-11 11:11:10    Idle           2021-01-20 11:11:10     Pass
Duplex_Mode           Inspection      2021-02-22 12:22:20    Running        2021-02-22 12:22:20     Failed
OSPF_PEER             Inspection      2021-02-22 12:22:20    Running        2021-02-22 12:22:20     Norelated
Test1                 User-define     2021-03-05 15:15:15    Idle           --                      --
-----------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display eva script-item status** command output
| Item | Description |
| --- | --- |
| Inspection running status | Running status of a PMI script. Only the running status of the latest PMI script is displayed.   * running: The script is running. * complete: The script is in the complete state. |
| Script | Script name. |
| Type | Script type:   * build-in: built-in script of the system. * user-define: user-defined script. * inspection: inspection script. |
| RegisterTime | Time when a script is registered. |
| Status | Script running status.:   * Idle: The script is suspended. * Waiting: The script is in the waiting state. * Running: The script is being executed. |
| LastExecTime | Last time when the script is executed. |
| Result | Latest script execution result. |