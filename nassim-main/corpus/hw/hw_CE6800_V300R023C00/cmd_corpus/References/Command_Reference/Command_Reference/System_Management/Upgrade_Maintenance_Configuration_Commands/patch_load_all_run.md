patch load all run
==================

patch load all run

Function
--------



The **patch load all run** command loads and activates a matching patch in the patch package to the current system.




Format
------

**patch load** *PkgName* **all** **run**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *PkgName* | Specify a patch name. | The value is a string of 5 to 127 case-sensitive characters without spaces. The length of the patch file storage path ranges from 0 to 64 characters, and the length of the patch file name ranges from 5 to 63 characters. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Before loading a patch, the system resolves the patch package to check the validity of patch files and obtain the attributes of patch files.When you load a patch to the current system, the system searches the patch package for a matching patch file according to the attributes of the patch file.

* If a matching patch file is found in the patch package, the system loads and activates the patch.
* If no matching patch file is found in the patch package, the system does not load or activate the patch.

**Prerequisites**

The patch package file has been loaded to the device.

**Configuration Impact**

After the patch load all run command is run, the system runs the patch after loading it.

**Precautions**

* If the CPU usage exceeds 70% or the memory usage exceeds 90%, do not run the patch load all run command to load the patch. If you do not want to check the CPU or memory usage, run the patch force-load all run command to forcibly load the patch. However, the patch may fail to be loaded.
* When loading a cold patch, restart the device to make the patch take effect.


Example
-------

# Perform one-click patch loading and activation.
```
<HUAWEI> patch load xxxxxx.PAT all run
Info: Operating, please wait for a moment.........................done.
Info: Succeeded in running the patch.

```