display task
============

display task

Function
--------



The **display task** command displays the information about tasks.




Format
------

**display task**


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

If you want to view the task information so as to make a configuration for the task group, run the **display task** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# View information about all tasks in the system.
```
<HUAWEI> display task
--------------------------------------------
Task-name                            Task-id
--------------------------------------------
ospf                                       1
rip                                        2
ripng                                      3
ntp                                        4
key-chain                                  5
patch                                      6
rpm                                        7
bgp                                        8
tunnel-policy                              9
tunnel                                    10
igmp                                      11

...                   

--------------------------------------------
Total 75, 75 printed

```

**Table 1** Description of the **display task**  command output
| Item | Description |
| --- | --- |
| Task-name | Task name. |
| Task-id | Task ID. |
| Total 75, 75 printed | Total number of tasks and total number of the printed tasks. |