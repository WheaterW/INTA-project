check startup checkpoint
========================

check startup checkpoint

Function
--------



The **check startup checkpoint** command verifies a specified checkpoint.



By default, the system restoration point is in the normal state.


Format
------

**check startup checkpoint** *checkpoint\_name*


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

This command is used to verify a specified checkpoint. If the checkpoint is verified, you can use the checkpoint to restore configuration. If the checkpoint fails the verification, the checkpoint cannot be used to restore configuration.


Example
-------

# Verify the specified rollback point.
```
<HUAWEI> check startup checkpoint chkpnt_1

```