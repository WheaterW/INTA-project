display aaa statistics offline-reason
=====================================

display aaa statistics offline-reason

Function
--------



The **display aaa statistics offline-reason** command displays the reasons why users go offline.




Format
------

**display aaa statistics offline-reason**


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

The display aaa statistics offline-reason command helps you know reasons why users go offline. You can locate network faults according to the command output.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display reasons why users go offline.(The displayed data is for reference only.)
```
<HUAWEI> display aaa statistics offline-reason
19  User request to offline       :2  
87  AAA cut command               :1

```

**Table 1** Description of the **display aaa statistics offline-reason** command output
| Item | Description |
| --- | --- |
| AAA cut command | A user is disconnected by the cut access-user command. |
| 19/87 | Reason code. |
| user request to offline | A user requested to go offline. |
| 2/1 | Number of times users go offline. |