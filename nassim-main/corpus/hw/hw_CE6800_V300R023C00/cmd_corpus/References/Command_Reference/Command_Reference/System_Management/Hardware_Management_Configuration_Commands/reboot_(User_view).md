reboot (User view)
==================

reboot (User view)

Function
--------



The **reboot fast** command quickly restarts the device. Before the restart, the system does not prompt you whether to save the configuration.

The **reboot save diagnostic-information** command restarts the device and saves diagnostic information to a specified location.




Format
------

**reboot** { **fast** | **save** **diagnostic-information** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **fast** | Restarts the device quickly without asking you whether to save the configuration. | - |
| **save** | Indicates the diagnostic information saved before the device restarts. | - |
| **diagnostic-information** | Displays system fault diagnosis information. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The function of the **reboot** command is the same as powering off and then powering on a device, but this command facilitates remote device maintenance.

**Configuration Impact**

* After the **reboot fast** command is executed, the system quickly restarts the device without prompting you to save the configuration. The unsaved configuration will be lost.
* After the **reboot save diagnostic-information** command is run, if the diagnostic information file already exists, the system asks you whether to overwrite the existing file. If you choose to overwrite the existing file, the system saves the diagnostic information to the root directory and overwrites the existing file. If you choose not to overwrite the file, the system does not collect diagnostic information. Diagnostic information does not affect device configuration.

**Precautions**

* In normal cases, do not run this command because it may lead to a temporary network outage. In addition, check that the configuration script of the device has been saved before you restart the device.
* After this command is run, if you do not respond to the system prompt, the system returns to the user view after timeout and does not restart.
* After the **reboot save diagnostic-information** command is run, press Ctrl+C to interrupt diagnostic information collection.
* If a user runs the **display diagnostic-information** command when another user is running the **reboot save diagnostic-information** command, a message indicating that the command is locked by another user is displayed.
* After secondary authentication for risky commands is enabled using the **configuration re-authentication enable** command, you need to enter the login password for secondary authentication when running the **reboot** command to make the command take effect.


Example
-------

# Restart the device and save diagnostic logs.
```
<HUAWEI> reboot save diagnostic-information
MPU 5:
Next startup system software: flash:/xxx.cc
Next startup saved-configuration file: flash:/xxx.cfg
Next startup paf file: default
Next startup patch package: flash:/xxx.PAT
Warning: The current configuration will be saved to the next startup saved-configuration file. Continue? [Y/N]:y
Now saving the current configuration.....
Save the configuration successfully.
Info: The diagnostic information will be saved to rbsaveddata.txt, it will take several minutes. Please wait.
Now saving the diagnostic information to the device.................................................................................................................................................................................................................................................................
Warning: Can not get the status on the slave board.
..................................................................
Info: The diagnostic information was saved to the device successfully.
Warning: The system will reboot. Continue? [Y/N]:y
System preprocessing has started, 100% completed.
System preprocessing succeeded.

```

# Restart the device quickly.
```
<HUAWEI> reboot fast
MPU 6:
Next startup system software: flash:/xxx.cc
Next startup saved-configuration file: flash:/xxx.cfg
Next startup paf file: default
Next startup patch package: NULL
Warning: The system will reboot. Continue? [Y/N]:y

```