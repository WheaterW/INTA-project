display eva register-strategy
=============================

display eva register-strategy

Function
--------



The **display eva register-strategy** command displays policy registration information about a script.




Format
------

**display eva register-strategy** [ *fileName* ]


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

To view policy registration information about a script, run this command.If fileName is not specified, policy registration information about all registered scripts is displayed.If fileName is specified, policy registration information about the script named fileName is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display policy registration information about the device.
```
<HUAWEI> display eva register-strategy cpuHigh
Total: 1
------------------------------------------------------------------------------------
FileName Name     ValidTime  SurvivalTime SecDetect  RegisterTime        Action  Formula                                                          
------------------------------------------------------------------------------------
cpuHigh   s1              60            60 False      2020-05-14 08:29:28 log     e1
------------------------------------------------------------------------------------

```

**Table 1** Description of the **display eva register-strategy** command output
| Item | Description |
| --- | --- |
| FileName | * Script file name for an EVA script in Python format. * Script name for an EVA script in JSON format. |
| Name | Policy name. |
| ValidTime | Validity period, in seconds. All events are considered to have occurred only when the time difference between the first event and last event is not greater than this validity period. |
| SurvivalTime | Lifetime of the script, in seconds. It is used together with SecDetect. |
| SecDetect | Secondary detection flag of a script, indicating whether the script is invoked by other scripts. The value can be True or False. If this parameter is set to True, SurvivalTime takes effect. The value is fixed to False for JSON scripts. |
| RegisterTime | Registration information of the script. |
| Action | Action associated with the policy.   * log: displays diagnostic logs. Only Python scripts support this parameter. * scriptNest: enables the nested script. Only Python scripts support this parameter. * uninstall: disables the nested script. Only Python scripts support this parameter. * netconf.Exec: NETCONF RPC operation. Only Python scripts support this parameter. * netconf.Get: NETCONF get operation. Only Python scripts support this parameter. * task: task group of the JSON script. |
| Formula | Policy formula. |
| Total | Total number of records. |