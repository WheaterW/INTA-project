display ops running context
===========================

display ops running context

Function
--------



The **display ops running context** command displays information about system environment variables.




Format
------

**display ops running context**

**display ops running context history**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **history** | Displays information about historical system environment variables. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The OPS supports the following environment variables:

* System environment variables: environment variables that are automatically generated during system running. The name of a system environment variable begins with an underscore (\_).
* User environment variables: environment variables that are configured using the **environment** command.To view information about current or historical system environment variables, run the display ops running context command.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about current system environment variables.
```
<HUAWEI> display ops running context
--------------------------------------------------------------------------------
Creator                        Variable                       Value                         
--------------------------------------------------------------------------------
_ops_frame_execute.py          absolute                       aaadfdf                       
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display ops running context** command output
| Item | Description |
| --- | --- |
| Creator | Script of the environment variable. |
| Variable | Name of the environment variable. |
| Value | Value of the environment variable. |