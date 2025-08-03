display configuration recover-result
====================================

display configuration recover-result

Function
--------



The **display configuration recover-result** command displays information about configuration restoration after the upgrade.




Format
------

**display configuration recover-result**


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

* After you run the **startup saved-configuration** command to specify the configuration file for the next startup and restart the device, run this command to check the configuration recovery result (success, failure, or partial failure) and failure cause.
* A maximum of 1000 records are displayed.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about configuration restoration after the upgrade.
```
<HUAWEI> display configuration recover-result
The current startup saved-configuration file is flash:/test.cfg.
The number of failed commands is 1.
Command : nat 1
View    : system
Line    : 63
Reason  : Unknown command
Time    : 2021-12-05 13:15:56

```

**Table 1** Description of the **display configuration recover-result** command output
| Item | Description |
| --- | --- |
| The current startup saved-configuration file is | Indicates the configuration file saved during the current startup. |
| The number of failed commands is | Indicates the number of times that the command fails to be executed. |
| Command | Command. |
| View | View. |
| Line | Line number. |
| Reason | Indicates the reasons. |
| Time | time. |