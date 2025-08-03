reset default-configuration
===========================

reset default-configuration

Function
--------



The **reset default-configuration** command deletes the preset configuration file on a device.




Format
------

**reset default-configuration**


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



To start a device without using the preset configuration file configured through the startup default-configuration command, run the **reset default-configuration** command to delete the preset configuration file.



**Configuration Impact**



If the preset configuration file is deleted and no configuration file is specified for next startup, the device does not use the preset configuration file to restore configurations upon next startup. As a result, the plug-and-play function may be affected.Exercise caution and follow the instructions of the technical support personnel when you run this command.




Example
-------

# Delete the preset configuration file on the device.
```
<HUAWEI> reset default-configuration
Warning: The action will delete the default configuration file on the device.
The default configuration file will be cleared to reconfigure.No default configuration file is set for the device. When the device is started without the next startup configuration, the plug-and-play function may be affected.Continue? [Y/N]: y
Info: Succeeded in clearing the configuration on the device.

```