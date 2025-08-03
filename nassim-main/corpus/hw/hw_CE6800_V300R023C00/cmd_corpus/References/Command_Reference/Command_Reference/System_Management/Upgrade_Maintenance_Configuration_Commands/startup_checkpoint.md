startup checkpoint
==================

startup checkpoint

Function
--------



The **startup checkpoint** command creates a specified checkpoint.



By default, a rollback point is created based on the current system software information.


Format
------

**startup checkpoint** *checkpoint\_name*


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

Before upgrading or rolling back feature software or setting a software package for the next startup, run this command to create a checkpoint. A checkpoint records the running system software package, feature package, and patch package.


Example
-------

# Create a specified checkpoint.
```
<HUAWEI> startup checkpoint chkpnt1

```