oam-mgr
=======

oam-mgr

Function
--------



The **oam-mgr** command displays the OAM management view.

The **undo oam-mgr** command deletes the OAM management view.



By default, the OAM management view is not created.


Format
------

**oam-mgr**

**undo oam-mgr**


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



Ethernet OAM fault advertisement is implemented by an OAM manager (OAMMGR), application modules, and detection modules. An OAMMGR module associates one module with another. A detection module monitors link status and network performance. If a detection module detects a fault, it instructs the OAMMGR module to notify an application module or another detection module of the fault. After receiving the notification, the application or detection module takes measures to prevent a communication interruption or service quality deterioration.



**Follow-up Procedure**



Associate the detection modules with other application modules in this view.




Example
-------

# Display the OAM management view.
```
<HUAWEI> system-view
[~HUAWEI] oam-mgr

```