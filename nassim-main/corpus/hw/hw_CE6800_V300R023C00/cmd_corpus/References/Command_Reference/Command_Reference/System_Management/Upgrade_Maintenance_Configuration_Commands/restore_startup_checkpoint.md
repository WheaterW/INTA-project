restore startup checkpoint
==========================

restore startup checkpoint

Function
--------



The **restore startup checkpoint** command configures a checkpoint for the next startup.



By default, if the system does not need to perform software rollback, you do not need to set the rollback point for the next use.


Format
------

**restore startup checkpoint** *checkpoint\_name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *checkpoint\_name* | Checkpoint name. | The value is a string of 5 to 32 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To specify a checkpoint for the next startup in a software rollback scenario, run the restore startup checkpoint command.

**Follow-up Procedure**

Run the **reboot** command to restart the device.

**Precautions**

After the checkpoint is specified, restart the device.


Example
-------

# Restore data to the specified rollback point.
```
<HUAWEI> restore startup checkpoint chkpnt_1

```