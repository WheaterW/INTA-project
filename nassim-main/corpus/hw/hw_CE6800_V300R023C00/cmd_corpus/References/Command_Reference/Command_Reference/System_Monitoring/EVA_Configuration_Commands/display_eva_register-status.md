display eva register-status
===========================

display eva register-status

Function
--------



The **display eva register-status** command displays the script registration status.




Format
------

**display eva register-status** [ *fileName* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *fileName* | Specifies the name of an EVA script. | The value is a string of 2 to 31 case-sensitive characters, starting with a letter and containing only digits, letters, and underscores (\_). It cannot contain spaces.   * The file name extension of an EVA script in Python format is .py. * The .json file name extension is not required for an EVA script in JSON format. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

To check whether a script has been registered, run the display eva register-status command.If the filename parameter is not specified, the registration status of all scripts on the device is displayed.If the filename parameter is specified, the registration status of the specified script is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Query the script registration status.
```
<HUAWEI> display eva register-status
Inspection install status: complete
Inspection data path: flash:/eva/eva_inspection_20211109154918.zip
Total: 3
--------------------------------------------------------------------------
FileName                         Status     FaultInfo                     
--------------------------------------------------------------------------
cpuHigh.py                       Success    -                             
memHigh.py                       Success    -                             
SystemExceptionCheck             Success    -                                                       
--------------------------------------------------------------------------

```

**Table 1** Description of the **display eva register-status** command output
| Item | Description |
| --- | --- |
| Inspection install status | PMI script installation status.   * running: The script is being parsed and installed. * complete: The script has been installed. |
| Inspection data path | Path for storing PMI data. |
| FileName | * For an EVA script in Python format, this parameter indicates the script name. * For an EVA script in JSON format, this parameter indicates the name of a check item. |
| Status | Script registration status.   * Success: The registration is successful. * Failed: The registration fails. |
| FaultInfo | Script registration failure cause. |
| Total | Total number of records. |