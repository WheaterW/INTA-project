uninstall-module next-startup (User view)
=========================================

uninstall-module next-startup (User view)

Function
--------



The **uninstall-module next-startup** command clears the specified module that is automatically loaded during the next startup of the device.




Format
------

**uninstall-module** *moduleName* **next-startup**


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

If a specified module does not need to be started next time, you can run the **uninstall-module next-startup** command to clear the specified module from the next startup module list.If all modules do not need to be started next time, run the **uninstall-module next-startup all** command to clear all modules from the module list for next startup.

**Precautions**

Running this command may affect the normal running of the system. Therefore, exercise caution when running this command.


Example
-------

# Uninstall a specified module online.
```
<HUAWEI> uninstall-module xxxxxx.MOD next-startup
This will uninstall the xxxxxx.MOD module. Are you sure? [Y/N]:Y
Info: Operating, please wait for a moment.......done.
Info: Succeeded in uninstalling the module.

```