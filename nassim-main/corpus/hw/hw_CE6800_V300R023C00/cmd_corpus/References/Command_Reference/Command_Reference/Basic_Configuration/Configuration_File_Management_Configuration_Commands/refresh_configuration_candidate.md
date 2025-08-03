refresh configuration candidate
===============================

refresh configuration candidate

Function
--------



The **refresh configuration candidate** command re-executes candidate configuration to resolve configuration conflicts.




Format
------

**refresh configuration candidate**


Parameters
----------

None

Views
-----

All views except the user view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the system displays a message indicating that the current running configuration is changed when you run the **display configuration candidate changes** command to view the difference between the candidate configuration and current running configuration, run the refresh configuration candidate command to resolve the configuration conflict so that you can continue to view the configuration difference.If a configuration conflict occurs before you commit the configuration, you can resolve the configuration conflict and then run the **commit** command to commit the configuration. Alternatively, run the **commit** command to commit the configuration directly, without resolving the configuration conflict.

**Precautions**

This command applies only to the two-phase validation mode.


Example
-------

# Update the candidate configuration based on the current running configuration to resolve configuration conflicts.
```
<HUAWEI> system-view
[~HUAWEI] refresh configuration candidate

```