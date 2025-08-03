install-module next-startup (User view)
=======================================

install-module next-startup (User view)

Function
--------



The **install-module next-startup** command configures the module to be automatically loaded during the next startup of the device.




Format
------

**install-module** *moduleName* **next-startup**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *moduleName* | Specifies the name of a module file. | The value is a string of 5 to 63 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To configure a module as the next startup module, run this command to add the module installation package to the list of modules to be started next time. The device automatically loads the module at the next startup.The **display module-information** command displays whether a specified module has been installed in the system.

**Precautions**

The module file must be in the $\_install\_mod directory.


Example
-------

# Specify the module package for the next startup.
```
<HUAWEI> install-module xxxxxx.MOD next-startup

```