startup
=======

startup

Function
--------



The **startup saved-configuration** command specifies the configuration file to be loaded at the next startup of the system.

The **startup shareable-configuration** command imports a configuration file. The password entered by the user matches the key in the configuration file.




Format
------

**startup saved-configuration** *configuration-file*

**startup shareable-configuration** *configuration-file* [ **password** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *configuration-file* | Specifies the name of a configuration file. The file must have been created. | The name is a string of 5 to 64 characters in the format of \*.zip, \*.cfg or \*.dat. |
| **password** | Specifies the password for decrypting a configuration file. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If the configuration file becomes inapplicable due to software upgrade, run the **startup saved-configuration** command to specify a new configuration file to be loaded at the next startup of the system. You can run the startup shareable-configuration command to configure the configuration file that contains the key information saved on another device as the next startup file.The extension of the configuration file name must be .zip, .cfg or .dat. The system configuration file must be saved in the root directory of the storage device.

* A .cfg file is a text file, whose contents can be viewed directly. If a .cfg file is specified as the configuration file, the system restores the commands in the file one by one during device startup.
* A .zip file is compressed from a .cfg file and occupies less space. If a .zip file is specified as the configuration file, the system first decompresses the file into a .cfg file, and then restores the commands in the .cfg file one by one during device startup.
* A .dat file is a compressed file, which can be in binary or text mode. If the startup software version and the .dat file version are the same, the system restores all configurations at a time without the need to restore the commands one by one, accelerating device startup.The specified configuration file for next startup must be checked against the first-login configuration file. If the check fails, the following message is displayed: Error: The configuration file will cause the next startup login failure.Please check it. This message indicates that the configuration file will cause a login failure for the next startup. You need to add the login configuration of the console port or port configured with the management IP address to the configuration file.

**Configuration Impact**



The configuration file to be loaded at the next startup of the system is changed.



**Precautions**

* The specified configuration file has been created.
* The .dat file cannot be modified manually. Otherwise, the configuration file will fail to be loaded when the device stars, and the device will start with no configurations.
* If the autosave function is enabled, after you run this command to configure the configuration file for next startup, automatic saving is disabled for 30 minutes.After the autosave interval expires, a save operation is automatically triggered. As a result, the configured configuration file for next startup is overwritten by the current configuration file.To prevent the incorrect overwriting, run the **undo configuration file auto-save** command to disable the autosave function before you configure the configuration file for next startup.
* After the configuration file for next startup is configured using this command, the file will be overwritten by the current configurations if the **save** command is executed.If the specified configuration file does not have the HMAC code, the setting can still be successful and the integrity check is not performed. Users need to ensure the validity of the file.
* After switching to the FIPS mode, run this command to configure the configuration file for next startup. The specified configuration file cannot be a configuration file created in non-FIPS mode.


Example
-------

# Specify the configuration file to be loaded at the next startup while auto-save is enabled.
```
<HUAWEI> system-view
[~HUAWEI] configuration file auto-save
[*HUAWEI] commit
[~HUAWEI] quit
<HUAWEI> startup saved-configuration huawei.cfg

```

# Specify the configuration file to be loaded at the next startup while auto-save is disabled.
```
<HUAWEI> system-view
[~HUAWEI] undo configuration file auto-save
[*HUAWEI] commit
[~HUAWEI] quit
<HUAWEI> startup saved-configuration huawei.cfg

```

# Set the configuration file that contains key information as that for the next startup.
```
<HUAWEI> startup shareable-configuration 333.cfg
Info: Operating, please wait for a moment..................................done.
Info: Succeeded in setting the configuration for booting system.

```

# Set the configuration file that contains key information as that for the next startup.
```
<HUAWEI> startup shareable-configuration test.cfg password
Enter Password:
Info: Operating, please wait for a moment....................done.
Info: Succeeded in setting the configuration for booting system.

```