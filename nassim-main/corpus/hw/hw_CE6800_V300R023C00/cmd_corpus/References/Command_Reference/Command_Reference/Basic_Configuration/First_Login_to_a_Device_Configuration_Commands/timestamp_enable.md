timestamp enable
================

timestamp enable

Function
--------



The **timestamp enable** command enables the timestamp function for a system.

The **undo timestamp enable** command disables the timestamp function.



By default, the timestamp function is disabled for the system.


Format
------

**timestamp enable**

**undo timestamp enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable the timestamp function for a system, run the timestamp enable command. After this function is enabled, the time for querying the system configurations is displayed each time you run the display command.


Example
-------

# Enable the timestamp function for the system.
```
<HUAWEI> system-view
[~HUAWEI] timestamp enable

```