startup default-configuration
=============================

startup default-configuration

Function
--------



The **startup default-configuration** command configures a preset configuration file for the system. If no configuration file is specified for next startup, the device uses this preset configuration file for startup.




Format
------

**startup default-configuration** *configuration-file*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *configuration-file* | Specifies the name of a configuration file to be used as the default configuration file. This file must exist. | The value is a string of 8 to 127 characters in the format of \*.defcfg. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



When a device starts without any configuration file, engineers need to configure the device onsite, which is inconvenient for device O&M. To implement plug-and-play after a device starts without any configuration file, run the **startup default-configuration** command to preset a configuration file for the device. The preset configuration file must contain configurations required by the plug-and-play function. The preset configuration file will be used for configuration restoration when the device starts without any configuration file.The configuration file name extension must be \*.defcfg, and the default configuration file must be stored in the root directory of the device before being specified. After the **startup default-configuration** command is configured, the default configuration file in the root directory will be imported to the device.The preset configuration file is in text format, and its content can be directly viewed. After the preset configuration file is specified for startup, the device restores the commands in the preset configuration file one by one upon startup.



**Configuration Impact**



If no configuration file is specified for next startup, the device uses the preset configuration file for next startup.



**Precautions**



The size of the preset configuration file cannot exceed 50 KB.Exercise caution and follow the instructions of the technical support personnel when you run this command.




Example
-------

# Configure the preset configuration file for the system.
```
<HUAWEI> startup default-configuration huawei.defcfg
Warning: The action will override and update the default configuration file on the device. Continue? [Y/N]:y
...
Info: Succeeded in setting the configuration for booting system.

```