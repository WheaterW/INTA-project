display configuration replace failed
====================================

display configuration replace failed

Function
--------



The **display configuration replace failed** command displays information about configuration replacement failures.




Format
------

**display configuration replace failed**


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

If configuration replacement fails, run the display configuration replace failed command to view the detailed failure information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about configuration replacement failures.
```
<HUAWEI> display configuration replace failed
Failed command(s):

Command : - interface a
View : system
Reason : Command not match

Command : + interface b
View : system 
Reason : Command not match

```

**Table 1** Description of the **display configuration replace failed** command output
| Item | Description |
| --- | --- |
| Failed command(s) | Information about the configuration replacement failure. |
| Command | Command that fails to be replaced. |
| View | View to which the command that fails to be replaced belongs. |
| Reason | Reason for the configuration replacement failure. |