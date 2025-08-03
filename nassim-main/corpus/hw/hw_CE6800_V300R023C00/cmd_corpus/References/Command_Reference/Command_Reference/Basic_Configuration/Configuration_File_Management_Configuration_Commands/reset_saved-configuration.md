reset saved-configuration
=========================

reset saved-configuration

Function
--------



The **reset saved-configuration** command clears information about the configuration files on the storage device.




Format
------

**reset saved-configuration**


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



After the device software is upgraded, the configuration file in the storage medium may not match the new software version. In this case, you can run the **reset saved-configuration** command to clear the old configuration file.If the device in use applies to another scenario and the original configuration file of the device does not meet requirements in the scenario, you can run the **reset saved-configuration** command to clear the existing configuration file and set a new configuration file.



**Precautions**

* Exercise caution and follow the instructions of the technical support personnel when you run this command.
* If secondary authentication for risky commands has been enabled using the configuration re-authentication enable command, you need to enter the login password for secondary authentication before running the **reset saved-configuration** command.
* When upgrading the system software package of a device, specify the system software package for next startup first. In this case, the device automatically specifies the configuration file for next startup. You can run this command to clear the configuration.


Example
-------

# Clear the configuration files used at the startup from the storage device.
```
<HUAWEI> reset saved-configuration
Warning: The action will delete the saved configuration on the device.
The configuration will be erased to reconfigure.Continue? [Y/N]:n


<HUAWEI> reset saved-configuration
Warning: The action will delete the saved configuration on the device.
The configuration will be erased to reconfigure.Continue? [Y/N]:y
Warning: Now clearing the configuration on the device.
Info: Succeeded in clearing the configuration on the device.

```