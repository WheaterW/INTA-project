record-file disable
===================

record-file disable

Function
--------



The **record-file disable** command disables the function of generating performance statistics files.

The **undo record-file disable** command restores the function of generating performance statistics files.



By default, a performance statistics file is automatically generated and saved on the device.


Format
------

**record-file disable**

**undo record-file disable**


Parameters
----------

None

Views
-----

Statistics task view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To save system resources, reduce system cost and operations on storage devices, and prolong the lifespan of a storage device during performance statistics collection, run the record-file disable command to prevent performance statistics files from being generated.To set the format for generated performance statistics files, run the file-format <format> command. If the system generates a new performance statistics file when four performance statistics files already exist, the latest performance statistics file will replace the earliest one.


Example
-------

# Disable the function of generating performance statistics files.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] statistics-task huawei
[*HUAWEI-pm-statistics-huawei] record-file disable

```