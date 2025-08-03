display eva register-events
===========================

display eva register-events

Function
--------



The **display eva register-events** command displays event registration information of a script.




Format
------

**display eva register-events** [ *fileName* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *fileName* | Specifies the name of an EVA script. | The value is a string of 2 to 31 case-sensitive characters, spaces not supported. It must start with a letter and contain only digits, letters, and underscores (\_).   * A Python script ends with .py. * Scripts in JSON format do not need to be suffixed with .json. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

To view the event registration information of the script, you can run the command.If the filename parameters are not specified, the event registration information of all registered scripts is displayed.If the filename parameters are specified, the event registration information of the script named filenameis displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display registration information about the event configured in the script.
```
<HUAWEI> display eva register-events cpuHigh
Total: 1 
------------------------------------------------------------------------------------
Filename  EventName Compare Threshold Frequency  Xpath
------------------------------------------------------------------------------------
cpuHigh     e1          >          80         3  huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info/system-cpu-usage
------------------------------------------------------------------------------------

```

**Table 1** Description of the **display eva register-events** command output
| Item | Description |
| --- | --- |
| Filename | * For a Python script, this parameter indicates the script file name. * For a script in JSON format, this parameter indicates the script name. |
| EventName | Event name. |
| Compare | Relationship function. |
| Threshold | Threshold. |
| Frequency | Frequency. An event is determined to have occurred only when the number of times that the judgment formula in the script is met is greater than or equal to this frequency. |
| Xpath | XPath information, which includes the xPath information in the YANG file referenced by the script, as well as the KPI and log event information in the database. |
| Total | Total number of records. |