info-center logfile compression lzma
====================================

info-center logfile compression lzma

Function
--------



The **info-center logfile compression lzma** command sets the user log compression algorithm to lzma.

The **undo info-center logfile compression** command restores the user log compression algorithm to the default value deflate.



By default, Deflate is used to compress user logs.


Format
------

**info-center logfile compression lzma**

**undo info-center logfile compression**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to set the user log compression algorithm to lzma or restore the default value deflate.


Example
-------

# Set the user log compression algorithm to lzma.
```
<HUAWEI> system-view
[~HUAWEI] info-center logfile compression lzma

```