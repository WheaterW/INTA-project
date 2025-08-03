install-module (User view)
==========================

install-module (User view)

Function
--------



The **install-module** command dynamically loads a specified module file.




Format
------

**install-module** *moduleName*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *moduleName* | Specify the module file name. The file must exist in the flash:/$\_install\_mod/ directory. | The value is a string of 5 to 63 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To install a module in the current system by loading the module file, run the install-module command. The extension of a module file name must be \*.MOD.To check information about successfully loaded module files, run the **display module-information** command.

**Precautions**

Loaded module files must be stored in the $\_install\_mod directory.


Example
-------

# Load the xxxxxx.MOD file to the $\_install\_mod directory.
```
<HUAWEI> install-module xxxxxx.MOD
Info: Operating, please wait for a moment..........done.
Info: Succeeded in installing the module.

```