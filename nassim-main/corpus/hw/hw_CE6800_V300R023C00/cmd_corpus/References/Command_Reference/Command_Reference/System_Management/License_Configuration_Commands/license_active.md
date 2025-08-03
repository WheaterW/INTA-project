license active
==============

license active

Function
--------



The **license active** command activates a license file on the current device.



By default, the license file is not activated.


Format
------

**license active** *file-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *file-name* | Specifies the name of the license file to be activated. | The value is a string of 5 to 127 case-sensitive characters. It cannot contain spaces. The file name extension is .dat, .xml, or .zip. The file name extension depends on the actual license file. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



If the current license file on the device expires or feature specifications need to be expanded, you can run the **license active** command to replace or upgrade the license file.



**Prerequisites**



The new license file has been uploaded to the current device.The file name extension of the license file is .dat, .xml, or .zip, and the license file must be stored in the root directory of the storage device.



**Configuration Impact**

* In the case of a license file that was never activated before, you can run the **license active** command to activate the license file.
* In the case of the license file that is running in the system and needs to be upgraded, note the following situation: if the configuration of the new license file is lower than the current configuration, after the **license active** command is run, the system asks you to confirm whether to upgrade the license file. If you choose "No", the system does not perform the upgrade operation; if you choose "Yes", the system activates the license file and performs the upgrade operation.In the case where the configuration in the new license file is lower than that in the current license file, you need to check whether the configuration items on which services depend exist in the new license file. If not, apply for a correct license file and activate it. Otherwise, after the board or device is restarted, services may be interrupted due to the lack of the configuration items on which services depend.

**Precautions**

* The system supports only standalone licenses and does not support network licenses. A standalone license file enables some features to be implemented on a device; a network license requires that a device obtain the permission of some features from a server.
* When the system restarts, the system activates the license file that was activated last time to ensure the license files are the same before and after restart.


Example
-------

# Activate the license file named license.xml.
```
<HUAWEI> license active license.xml
Now activing the license....done.
Info: Succeeded in activating the license file on the board.

```