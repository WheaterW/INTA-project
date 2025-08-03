display ops environment
=======================

display ops environment

Function
--------



The **display ops environment** command displays user-defined environment variables.




Format
------

**display ops environment**


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

**Usage Scenario**

The OPS supports the following environment variables:

* System environment variables: automatically generated during system running. The name of a system environment variable begins with an underscore (\_).
* User environment variables: environment variables that are configured using the **environment** command.

To view user-defined environment variables, run the display ops **environment** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display user-defined environment variables.
```
<HUAWEI> display ops environment
--------------------------------------------------------------------------------
No.  Name                            Value                                       
--------------------------------------------------------------------------------
1    a                               1                                           
2    b                               2                                           
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display ops environment** command output
| Item | Description |
| --- | --- |
| No. | Number of the environment variable. |
| Name | Name of the environment variable. |
| Value | Value of the environment variable. |