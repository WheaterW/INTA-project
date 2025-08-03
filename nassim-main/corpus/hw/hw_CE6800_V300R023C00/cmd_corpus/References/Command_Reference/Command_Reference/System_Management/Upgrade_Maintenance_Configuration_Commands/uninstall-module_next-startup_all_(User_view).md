uninstall-module next-startup all (User view)
=============================================

uninstall-module next-startup all (User view)

Function
--------



The **uninstall-module next-startup all** command clears the specified module that is automatically loaded during the next startup of the device.




Format
------

**uninstall-module next-startup all**


Parameters
----------

None

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

# Delete all module packages for next startup.
```
<HUAWEI> uninstall-module next-startup all

```