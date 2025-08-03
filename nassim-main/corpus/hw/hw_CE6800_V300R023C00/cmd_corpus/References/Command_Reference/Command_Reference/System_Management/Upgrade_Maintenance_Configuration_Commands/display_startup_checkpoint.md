display startup checkpoint
==========================

display startup checkpoint

Function
--------



The **display startup checkpoint** command displays the checkpoint information in the system.




Format
------

**display startup checkpoint**


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

If you want to roll back the system to a checkpoint, run the **display startup checkpoint** command to view the checkpoint information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# display startup checkpoint.
```
<HUAWEI> display startup checkpoint
---------------------------------------------------------------------------------
Name                             Create Time                      Create Mode
---------------------------------------------------------------------------------
@chkpnt_auto                     2020-05-29 16:04:35              Auto
chkpng_1                         2020-05-30 11:10:50              Manual
---------------------------------------------------------------------------------

```

**Table 1** Description of the **display startup checkpoint** command output
| Item | Description |
| --- | --- |
| Name | Checkpoint name. |
| Create Time | Checkpoint create time. |
| Create Mode | Checkpoint create mode. |