set flow-control-message reliability disable
============================================

set flow-control-message reliability disable

Function
--------



The **set flow-control-message reliability disable** command disables the board from being reset when message congestion lasts for 30 minutes.

The **undo set flow-control-message reliability disable** command enables the board to reset when message congestion lasts for 30 minutes.



By default, if the message congestion detected by the board is more than 30 minutes, the board will reset.


Format
------

**set flow-control-message reliability disable**

**undo set flow-control-message reliability disable**


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

If the message congestion detected by the board is more than 30 minutes, the board will reset. The **set flow-control-message reliability disable** command can be used to stop the board from resetting when message congestion lasts for 30 minutes.


Example
-------

# Disable the board from being reset when message congestion lasts for 30 minutes.
```
<HUAWEI> system-view
[~HUAWEI] set flow-control-message reliability disable

```