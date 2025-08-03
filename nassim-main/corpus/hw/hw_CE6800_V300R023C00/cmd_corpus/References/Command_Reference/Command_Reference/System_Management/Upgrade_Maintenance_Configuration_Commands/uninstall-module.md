uninstall-module
================

uninstall-module

Function
--------



The **uninstall-module** command uninstalls a specified module file online.




Format
------

**uninstall-module** { *moduleName* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *moduleName* | Specifies the name of the module file to be uninstalled. | The value is a string of 5 to 63 case-sensitive characters, spaces not supported. |
| **all** | Specifies that all module files need to be uninstalled. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

This command is used to uninstall a running module from the system. The **display module-information** command displays whether a specified module has been uninstalled in the system.


Example
-------

# Uninstall a specified module online.
```
<HUAWEI> uninstall-module xxxxxx.MOD
This will uninstall the xxxxxx.MOD module. Are you sure? [Y/N]:Y
Info: Operating, please wait for a moment.......done.
Info: Succeeded in uninstalling the module.

```

# Uninstall all modules online.
```
<HUAWEI> uninstall-module all
Warning: This will uninstall all the module. Continue? [Y/N]:y
Info: Operating, please wait for a moment...
Error: No module exists.

```