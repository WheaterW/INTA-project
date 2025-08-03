shutdown (Console-type user interface view)
===========================================

shutdown (Console-type user interface view)

Function
--------



The **shutdown** command closes a specified user interface.

The **undo shutdown** command starts a specified user interface.



By default, the specified user interface is enabled.


Format
------

**shutdown**

**undo shutdown**


Parameters
----------

None

Views
-----

CONSOLE-type user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When a specified user interface is abnormal or needs to be suspended due to other reasons, you can run this command.


Example
-------

# Disable the console user interface.
```
<HUAWEI> system-view
[~HUAWEI] user-interface console 0
[~HUAWEI-ui-console0] shutdown
Warning: Disabling the console port will make the console port unavailable. If you cannot log in through the management port, the device will be in unmanaged state. Continue? [Y/N]:y

```