startup patch all
=================

startup patch all

Function
--------



The **startup patch all** command specifies the patch file to be used at the next startup.



By default, no patch file to be used at the next startup is specified.


Format
------

**startup patch** *pkgname* **all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pkgname* | Specifies the file name of the patch package for the next startup. | The value is a string of 5 to 127 case-sensitive characters without spaces. The length of the patch file storage path ranges from 0 to 64 characters, and the length of the patch file name ranges from 5 to 63 characters. |
| **all** | All the slots. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If you want a patch file to be loaded and run after the system restarts, you can run the **startup patch** command to specify the patch file to be used at the next startup.

**Prerequisites**

The patch package file has been loaded to the device.

**Configuration Impact**

After the **startup patch** command is run and the system is restarted, the patch file will be loaded and run on all boards.

**Precautions**

If the **startup patch** command is run multiple times, the latest configuration will override the previous ones.After the **startup patch** command is run, use either of the following methods if you do not want the specified patch file to take effect after the system restart:

* Run the **patch delete** command to delete the current patch file.
* Run the **reset patch-configure** command to clear the name of the patch file to be used at the next startup.

Example
-------

# Specify the patch package loaded to the device at the next startup.
```
<HUAWEI> startup patch xxxxxx.PAT all
Info: Operating, please wait for a moment......done.
Info: Succeeded in setting startup the patch.

```