display upgrade rollback-timer
==============================

display upgrade rollback-timer

Function
--------



The **display upgrade rollback-timer** command displays information about the upgrade rollback timer.




Format
------

**display upgrade rollback-timer**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Before upgrading or downgrading the system, you can run this command to check whether the system software, configuration file name, PAF file name, and patch file name for the next startup are correct. Only when these parameters are correct, the system can be upgraded or downgraded successfully. You can also run this command to view the names of the system software, configuration file, PAF file, and patch file loaded for the current startup.


Example
-------

# Display information about whether the rollback function is enabled on the device when the rollback function is enabled.
```
<HUAWEI> display upgrade rollback-timer
Upgrade rollback timer (minutes): 10.
If the function is enabled, the master board will restart using the bootfile flash:/XXXXXXXX.cc.

```

# Display information about whether the rollback function is enabled on the device when the rollback function is disabled.
```
<HUAWEI> display upgrade rollback-timer
Upgrade rollback timer (minutes): --.
If the function is enabled, the master board will restart using the bootfile flash:/XXXXXXXX.cc.

```

**Table 1** Description of the **display upgrade rollback-timer** command output
| Item | Description |
| --- | --- |
| Upgrade rollback timer (minutes) | Value of the rollback timer. The value -- indicates that the rollback timer is not configured. |