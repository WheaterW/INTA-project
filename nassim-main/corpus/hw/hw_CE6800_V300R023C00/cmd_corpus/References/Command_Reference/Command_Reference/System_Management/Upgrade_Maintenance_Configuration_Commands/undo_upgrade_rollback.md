undo upgrade rollback
=====================

undo upgrade rollback

Function
--------



The **undo upgrade rollback** command cancels the timeout period of the rollback timer for a system software upgrade.



By default, the rollback timer is not enabled.


Format
------

**undo upgrade rollback**


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

If the version rollback function is disabled, the system will not perform version rollback whether any users successfully log in to the device in a specified period of time.By default, the version rollback function is disabled. After each version rollback completes, the version rollback function is disabled again.

**Precautions**

If users successfully log in to the device, the system automatically cancels the timeout period for version rollback.After you run this command, the current system resets the rollback timer.


Example
-------

# Cancel the timeout period of the rollback timer.
```
<HUAWEI> undo upgrade rollback
Info: The state of upgrade rollback is disable.

```