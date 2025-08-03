display configuration exclusive by-user-name
============================================

display configuration exclusive by-user-name

Function
--------



The **display configuration exclusive by-user-name** command displays lock information of the system configuration locked based on user name.




Format
------

**display configuration exclusive by-user-name**


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

To view system configuration lock information, run the display configuration exclusive by-user-name command. The command output includes the name of a user who locks or unlocks the system configuration, time when the system configuration is locked or unlocked, and lock ID.If no system configuration is locked, no command output is displayed after the display configuration exclusive by-user-name command is run.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display lock information after the system configuration is locked.
```
<HUAWEI> display configuration exclusive by-user-name
Lock User Name: root123
Lock Time: 2018-03-07 20:13:31+04:00 DST
Identifier: 13

```

# Display lock information after the system configuration is unlocked.
```
<HUAWEI> display configuration exclusive by-user-name
Unlock User Name: root1234
Unlock Time: 2018-03-07 20:14:09+04:00 DST

```

**Table 1** Description of the **display configuration exclusive by-user-name** command output
| Item | Description |
| --- | --- |
| Lock User Name | Name of a user who locks the system configuration. |
| Lock Time | Time when the system configuration is locked. |
| Unlock User Name | Name of a user who unlocks the system configuration. |
| Unlock Time | Time when the system configuration is unlocked. |
| Identifier | Lock ID, which is unique. |