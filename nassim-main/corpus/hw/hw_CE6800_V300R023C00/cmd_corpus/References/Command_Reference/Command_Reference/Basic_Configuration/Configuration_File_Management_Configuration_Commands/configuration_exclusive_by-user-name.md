configuration exclusive by-user-name
====================================

configuration exclusive by-user-name

Function
--------



The **configuration exclusive by-user-name** command enables a user to lock the system configuration.

The **undo configuration exclusive by-user-name** command enables a user to unlock the system configuration.



By default, the system configuration is not locked.


Format
------

**configuration exclusive by-user-name** *user-name*

**undo configuration exclusive by-user-name** *user-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-name* | Specifies the name of a user. | The name is a string of 1 to 253 characters. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Multiple users can access a device and manage it. A user can be a controller or another type of user. If the configuration of a forwarder is modified by a non-controller user, the configurations of the controller and forwarder may be inconsistent. The configuration exclusive by-user-name command can be used to specify the controller to lock the system configuration of a forwarder to avoid the inconsistency.When multiple users manage a device at the same time, you can specify a user to lock the device. Only this user can modify the device configuration, while others cannot.

**Configuration Impact**

After the system configuration is locked by a user, only this user can perform configuration operations. Other users can view, edit, maintain, and save the configuration but cannot commit the configuration. If another user needs to commit the configuration, run the undo configuration exclusive by-user-name user-name command to unlock the configuration first.

When this command is run, ensure that the user-name value is that specified when the configuration exclusive by-user-name command is run.

**Precautions**

* Only one user can lock the system configuration at a time.
* The user that runs this command to lock the system configuration must be the same as the user-name in the configuration exclusive by-user-name user-name command.
* Only users of the management user level can lock and unlock the system configuration.
* The configuration exclusive by-user-name command locks the device configuration based on the user name. Only the same user name can be used to unlock the device configuration. After the user is logged out, the device configuration will not be unlocked automatically. The **configuration exclusive** command locks the device configuration based on the session. The device configuration can be unlocked only by the current session. After the session is logged out, the device configuration is unlocked automatically.

Example
-------

# Enable user huawei456 to lock the system configuration.
```
<HUAWEI> system-view
[~HUAWEI] configuration exclusive by-user-name huawei456

```