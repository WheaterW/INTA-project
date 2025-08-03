command alias
=============

command alias

Function
--------



The **command alias** command creates and enters the command alias view.

The **undo command alias** command deletes all alias configured on the device.




Format
------

**command alias**

**undo command alias**


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

To enter the command alias view, run the command **alias** command.

**Follow-up Procedure**

Run the **alias** command to configure an alias for a command.

**Precautions**

The **undo command alias** command deletes all alias configured on the device as well as the command alias view.


Example
-------

# Enter the command alias view.
```
<HUAWEI> system-view
[~HUAWEI] command alias
[~HUAWEI-cmdalias]

```