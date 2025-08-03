route-policy nonexistent-config-check
=====================================

route-policy nonexistent-config-check

Function
--------



The **route-policy nonexistent-config-check** command controls whether the system strictly checks whether a nonexistent route-policy filter is referenced using a command.

The **undo route-policy nonexistent-config-check disable** command enables strict check on a nonexistent route-policy filter referenced using a command.



By default, a nonexistent route-policy filter cannot be referenced using a command.


Format
------

**route-policy nonexistent-config-check disable**

**route-policy nonexistent-config-check enable**

**undo route-policy nonexistent-config-check disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enable** | Indicates that the system does not allow a nonexistent route-policy to be specified in a command. | - |
| **disable** | Indicates that the system allows a nonexistent route-policy to be specified in a command. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, if a nonexistent route-policy filter is referenced using a command, the configuration does not take effect. To disable strict check on reference of a nonexistent route-policy filter, run the **route-policy nonexistent-config-check disable** command.




Example
-------

# Disable strict check on reference of a nonexistent route-policy filter using a command.
```
<HUAWEI> system-view
[~HUAWEI] route-policy nonexistent-config-check disable

```