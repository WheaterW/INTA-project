system-view immediately
=======================

system-view immediately

Function
--------



The **system-view immediately** command enters the system view and uses the immediate validation mode for configuration editing.




Format
------

**system-view immediately**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The system supports two configuration validation modes: immediate validation and two-phase validation.Run the **system-view immediately** command to enter the system view and edit configurations in immediate validation mode. In immediate validation mode, the configuration takes effect immediately after you enter a command and press Enter.

**Precautions**

Command line prompt. HUAWEI is the default device name. The prompt indicates the current view. <HUAWEI> indicates the user view, [HUAWEI] indicates the system view in immediate validation mode, and [\*HUAWEI] indicates the system view in two-phase validation mode. In two-phase validation mode, configurations that are not submitted in the system are marked with an asterisk (\*). If all configurations have been submitted in the system, the configurations are marked with ~.


Example
-------

# Enter the system view and adopt the immediate validation mode.
```
<HUAWEI> system-view immediately
[HUAWEI] sysname PE
[PE]

```