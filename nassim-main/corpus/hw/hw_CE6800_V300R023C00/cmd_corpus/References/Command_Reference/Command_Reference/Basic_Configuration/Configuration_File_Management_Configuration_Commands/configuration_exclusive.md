configuration exclusive
=======================

configuration exclusive

Function
--------



The **configuration exclusive** command enables the configuration locking function that allows only one user to configure the system. During this period, all other users can only query configurations.

The **undo configuration exclusive** command disables the configuration locking function.



By default, the configuration locking function is disabled.


Format
------

**configuration exclusive**

**undo configuration exclusive**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The current device allows multiple users to log in and perform configurations. However, if multiple users who have logged in to the device concurrently perform configurations, configuration conflicts may occur, causing service exceptions. If a user needs to exclusively perform configurations, you can run the **configuration exclusive** command to lock the system configuration. You can run the **display configuration exclusive user** command to query information about the user who locks the configuration set.



**Prerequisites**



The configuration locking function is disabled for all users.



**Configuration Impact**

* After the **configuration exclusive** command is run, the current configurations are locked. In this case, the current user can deliver configurations, and other users can view, save, and maintain configurations, but cannot deliver configurations. You can run the **display configuration exclusive user** command to check information about the user for whom the configuration permission is locked.
* After the **undo configuration exclusive** command is run, the current configurations are unlocked so all users can perform and deliver configurations. Only the user who locks configurations can unlock the configurations in the session where the lock command is executed. Configurations cannot be unlocked by other users or in other sessions.
* If there are no configuration updates during the maximum period during which no configuration is delivered, the system unlocks the configurations automatically. To configure the maximum period during which no configuration is delivered, run the configuration exclusive timeout command.

**Precautions**



Only one user can lock the configuration at a time. After the user logs out, the configuration is unlocked automatically.




Example
-------

# Enable the configuration locking function for user1.
```
<HUAWEI> configuration exclusive

```