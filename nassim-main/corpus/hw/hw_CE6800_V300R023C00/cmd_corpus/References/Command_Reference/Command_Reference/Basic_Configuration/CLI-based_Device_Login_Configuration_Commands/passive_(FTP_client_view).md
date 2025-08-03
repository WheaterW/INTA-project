passive (FTP client view)
=========================

passive (FTP client view)

Function
--------



The **passive** command sets the data transmission mode to passive.

The undo passive command sets the data transmission mode to active.



By default, the data transmission mode is active.


Format
------

**passive**

**undo passive**


Parameters
----------

None

Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The device supports active and passive data transmission.


Example
-------

# Set the data transmission mode to active.
```
<HUAWEI> ftp 10.1.1.2
[ftp] undo passive

```