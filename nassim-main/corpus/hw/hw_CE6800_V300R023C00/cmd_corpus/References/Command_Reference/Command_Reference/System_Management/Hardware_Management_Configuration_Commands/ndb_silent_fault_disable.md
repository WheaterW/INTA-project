ndb silent fault disable
========================

ndb silent fault disable

Function
--------



The **ndb silent fault disable** command disables the function of resetting a board when a silent DB fault occurs on a device.

The **undo ndb silent fault disable** command enables the function of resetting a board when a silent DB fault occurs on a device.



By default, a board resets when a silent DB fault occurs on a device.


Format
------

**ndb silent fault disable**

**undo ndb silent fault disable**


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

When a silent DB fault occurs in the database, you can disable the board reset function if you determine that the fault does not affect service running and the board does not need to be restarted.


Example
-------

# Disable the function of resetting the board when the silent fault occurs.
```
<HUAWEI> system-view
[~HUAWEI] ndb silent fault disable

```