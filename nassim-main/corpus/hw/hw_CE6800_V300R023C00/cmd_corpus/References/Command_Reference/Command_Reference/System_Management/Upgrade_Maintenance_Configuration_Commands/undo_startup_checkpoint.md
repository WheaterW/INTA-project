undo startup checkpoint
=======================

undo startup checkpoint

Function
--------



The **undo startup checkpoint** command deletes a specified checkpoint.



By default, the specified rollback point is deleted.


Format
------

**undo startup checkpoint** *checkpoint\_name*


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

If a checkpoint is not required, run this command to delete the checkpoint.


Example
-------

# Delete a specified rollback point.
```
<HUAWEI> undo startup checkpoint chkpnt_1

```