reboot
======

reboot

Function
--------



The **reboot** command restarts the device. Before the restart, the system displays a message asking you whether to save the configuration.




Format
------

**reboot**


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

The function of this command is the same as that of powering off and then powering on the device. During remote maintenance of the device, you can run this command to restart the device without going to the place where the device is located.

**Configuration Impact**



If the configuration file for next startup (new configuration file) is the same as the configuration file saved on the device after the **reboot** command is run, the system does not ask you whether to save the configuration before the restart. If the configuration file for next startup (new configuration file) differs from the configuration file saved on the device, the system asks you whether to save the configuration before the restart, and unsaved configuration information will be lost after the restart.



**Precautions**

* The **reboot** command needs to be delivered completely and does not support predictive delivery.
* In normal cases, do not run this command because it may lead to a temporary network outage. In addition, check that the configuration script of the device has been saved before you restart the device.
* After this command is run, if you do not respond to the system prompt, the system returns to the user view after timeout and does not restart.
* After secondary authentication for risky commands is enabled using the **configuration re-authentication enable** command, you need to enter the login password for secondary authentication when running the **reboot** command to make the command take effect.


Example
-------

# Restart the device.
```
<HUAWEI> reboot
MPU 6:
Next startup system software: flash:/xxx.cc
Next startup saved-configuration file: flash:/xxx.cfg
Next startup paf file: default
Next startup patch package: NULL
Warning: The system will reboot. Continue? [Y/N]:y

```

# Enable second authentication for risky commands and restart the device.
```
<HUAWEI> reboot
MPU 2:
Next startup system software: cfcard:/xxx.cc
Next startup saved-configuration file: cfcard:/xxx.cfg
Next startup paf file: default
Next startup patch package: NULL
Warning: Current configuration will be saved to the next startup saved-configuration file! Continue? [Y/N]:Y
Now saving the current configuration.....
Save the configuration successfully.
System will reboot! Continue? [Y/N]:Y
Info: This command is a high-risk command. Enter the login password of the current user again.
Enter Password:

```