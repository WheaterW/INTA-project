reset trace instance
====================

reset trace instance

Function
--------



The **reset trace instance** command clears all the diagnosis instances on a device.




Format
------

**reset trace instance**


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

After service diagnosis is enabled and a diagnosis object is created on a device, the device creates a diagnosis instance when a user matching the attributes of the diagnosis object gets online. If the device diagnoses services of multiple users, it creates a diagnosis instance for each user, which occupies a large amount of system resources. Therefore, the device needs to delete the diagnosis instance of a user when the user goes online successfully or fails to go online. Additionally, the device provides an aging mechanism for service diagnosis. When the 30-second aging time is reached, the device automatically deletes diagnosis instances to reclaim resources.In addition to the preceding two methods for automatically clearing diagnosis instances, you can run the **reset trace instance** command to clear all the diagnosis instances.

**Precautions**

After all the diagnosis instances are cleared using the **reset trace instance** command, properly running diagnosis instances are also deleted. Exercise caution when you run the **reset trace instance** command.


Example
-------

# Clear all diagnosis instances on the device.
```
<HUAWEI> system-view
[~HUAWEI] reset trace instance
Warning: This operation will clear all instance information. Continue? [Y/N]:Y                                                      
Trace Instance Information                                                                                                          
---------------------------------------                                                                                             
Alloc instance times    : 0                                                                                                         
Free instance times     : 0
---------------------------------------

```

**Table 1** Description of the **reset trace instance** command output
| Item | Description |
| --- | --- |
| Alloc instance times | Number of allocated service diagnosis instances. |
| Free instance times | Number of released service diagnosis instances. |