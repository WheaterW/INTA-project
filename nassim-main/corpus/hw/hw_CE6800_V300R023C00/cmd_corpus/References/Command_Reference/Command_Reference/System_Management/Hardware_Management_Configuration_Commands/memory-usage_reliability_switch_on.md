memory-usage reliability switch on
==================================

memory-usage reliability switch on

Function
--------



The **memory-usage reliability switch on** command enables the memory overload reliability function.

The **undo memory-usage reliability switch on** command disables the memory overload reliability function.



By default, the memory overload reliability function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**memory-usage reliability switch on**

**undo memory-usage reliability switch on**


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



To enable the system to notify users of the top 3 components with the highest memory usage when memory usage is overloaded and to reset the PROTO1 process to improve memory reliability if this process has the highest memory usage, run the **memory-usage reliability switch on** command to enable the memory overload reliability function.With this function enabled, when the memory usage of a board exceeds the level-1 overload threshold, the system notifies users of the top 3 components to which processes with the highest memory usage belong. When the memory usage of the board exceeds the level-2 overload threshold, the system notifies users of the process with the highest memory usage. If this process is the PROTO1 process, the system resets the process.



**Precautions**



After the **undo memory-usage reliability switch on** command is run, if the memory usage of a board exceeds the threshold, the device restarts.




Example
-------

# Enable the memory overload reliability function.
```
<HUAWEI> system-view
[~HUAWEI] memory-usage reliability switch on

```