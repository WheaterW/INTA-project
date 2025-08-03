display license state trial
===========================

display license state trial

Function
--------



The **display license state trial** command displays the remaining valid keepalive period of the license file.




Format
------

**display license state trial**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

If a license file has been activated and in the keepalive period, the **display license state trial** command can be run to display the remaining valid keepalive period of the license file.

**Prerequisites**

Before running this command, ensure that an activated license file exists on the device. Otherwise, no output is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the remaining valid keepalive period of the license file.
```
<HUAWEI> display license state trial
Info: Current license state is Trial. The trial days remains 59 days.The license for the current configuration will expire at 02:00 on the next day of the last trial day.

```

**Table 1** Description of the **display license state trial** command output
| Item | Description |
| --- | --- |
| Info | Remaining valid keepalive period of a license file. |