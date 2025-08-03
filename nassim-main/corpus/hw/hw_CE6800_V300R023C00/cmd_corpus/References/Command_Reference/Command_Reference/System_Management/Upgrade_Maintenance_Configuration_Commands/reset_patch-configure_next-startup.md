reset patch-configure next-startup
==================================

reset patch-configure next-startup

Function
--------



The **reset patch-configure next-startup** command deletes the configuration of the patch file for next startup.




Format
------

**reset patch-configure next-startup**


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

After the **startup patch** command is run to specify the patch file for next startup, you can run the **reset patch-configure next-startup** command to clear the configuration.

**Precautions**

If you run the **reset patch-configure next-startup** command, the patch file for next startup is empty. After the device restarts, the system will not automatically load or run the patch file after being restarted.


Example
-------

# Clear all the patch configurations for the next startup.
```
<HUAWEI> reset patch-configure next-startup
Info: Operating, please wait for a moment.....done.
Info: Succeeded in clearing startup the patch.

```