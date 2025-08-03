load-balance inner-connect
==========================

load-balance inner-connect

Function
--------



The **load-balance inner-connect** command displays the load balancing profile view of internal communication interfaces.

The **undo load-balance inner-connect** command restores the default load balancing profile for internal communication interfaces.



By default, the load balancing profile view is created for internal communication interfaces.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H and CE6881H-K.



Format
------

**load-balance inner-connect**

**undo load-balance inner-connect**


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

The device consists of two forwarding chips, which communicate with each other through internal communication interfaces. To change the load balancing mode of the interfaces, run the load-balance inner-connect command to enter the load balancing profile view and set the load balancing mode.

**Follow-up Procedure**

The load balancing mode can be configured in the internal communication interface profile view.


Example
-------

# Enter the internal communication interface profile view.
```
<Switch> system-view
[~Switch] load-balance inner-connect
[~Switch-inner-connect]

```