upgrade rollback rollback-timer
===============================

upgrade rollback rollback-timer

Function
--------



The **upgrade rollback rollback-timer** command sets the timeout period of the rollback timer for a system software upgrade.



By default, the rollback timer is not enabled.


Format
------

**upgrade rollback rollback-timer** *time-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **rollback-timer** *time-value* | Specifies a timeout period for a rollback timer. | The value is an integer that ranges from 10 to 360. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If you need to cancel the version upgrade being performed for some reason (for example, a new startup file was damaged), you can run the upgrade rollback command to perform version rollback to restore the version being upgraded to the original version.After the version rollback function is enabled, the system rolls back if no user is authenticated and logs in to the system within the specified period (rollback timer).If the version rollback function is disabled, the system will not perform version rollback whether any users successfully log in to the device in a specified period of time.By default, the version rollback function is disabled. After each version rollback completes, the version rollback function is disabled again.



If users successfully log in to the device, the system automatically cancels the timeout period for version rollback.After you run this command, the current system resets the rollback timer.




Example
-------

# Set the upgrade rollback timer to 10 minutes.
```
<HUAWEI> upgrade rollback rollback-timer 10

```