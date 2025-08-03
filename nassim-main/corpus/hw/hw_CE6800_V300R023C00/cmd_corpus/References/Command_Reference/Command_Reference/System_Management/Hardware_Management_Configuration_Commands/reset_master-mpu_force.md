reset master-mpu force
======================

reset master-mpu force

Function
--------



The **reset master-mpu force** command forcibly restarts the device.




Format
------

**reset master-mpu force**


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

To forcibly restart a device when an exception occurs on the device and the **reset slot** command cannot be executed, run the **reset master-mpu force** command.


Example
-------

# Forcibly restart the device.
```
<HUAWEI> reset master-mpu force
Warning: This operation will perform a forcible device restart. Are you sure you want to continue? Enter the complete [Yes/No]:Yes

```