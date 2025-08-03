display configuration exclusive user
====================================

display configuration exclusive user

Function
--------



The **display configuration exclusive user** command displays information about the user that locks the configuration set.




Format
------

**display configuration exclusive user**


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

You can run the display configuration exclusive user command to query the user that obtains configuration access. If the configuration set is not locked, there is no display.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the user that locks the configuration set.
```
<HUAWEI> display configuration exclusive user
User Index: 34
User Session Name: VTY 0
User Name: root
IP Address: 10.135.38.234
Locked Time: 2013-03-06 21:09:36
Last Configuration Time: 2013-03-06 21:09:36
The time out value of configuration right locked is: 30 second(s)

```

**Table 1** Description of the **display configuration exclusive user** command output
| Item | Description |
| --- | --- |
| User Index | Index of a user. |
| User Session Name | Session name of a user, ranging from VTY0 to VTY14. |
| User Name | User name of logging. |
| IP Address | IP address of a user, valid for VTY users only. |
| Locked Time | Time when the configuration set is locked. |
| Last Configuration Time | Time when the user runs the last command. |
| The time out value of configuration right locked is | Time when the configuration right is locked. |