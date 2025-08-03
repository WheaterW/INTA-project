patch delete all
================

patch delete all

Function
--------



The **patch delete all** command deletes patches.




Format
------

**patch delete all**


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

Run this command in either of the following scenarios:

* The system storage space is insufficient.
* If a patch exists in the system and another patch needs to be loaded, delete the existing patch from the system and then install the new patch package.

**Configuration Impact**

After the **patch delete all** command is run, patches in the system are deleted regardless of their status.

**Precautions**

* Running the **patch delete all** command may affect system running. Exercise caution when running the command.
* When the **patch delete all** command is run to delete patches from the current system, the system prompts you whether to delete patches.
* After the **patch delete all** command is run to delete existing patches from the current system, the deleted patches cannot be restored. So, confirm the action before you use this command.
* If the CPU usage exceeds 70%, do not run the **patch delete all** command to uninstall the patch. If you do not want to check the CPU usage, run the **patch force-delete all** command to forcibly uninstall the patch. However, the uninstallation may fail.
* After the **patch delete all** command is executed, if you want to delete the patch package file from the disk, run the **display patch-information verbose** command to query the information about the patch unit. If no patch unit information is obtained, you can delete the patch package file. If patch unit information is obtained, run the **patch health-proc** command. If no patch unit information is obtained after the restoration, delete the patch package file. If the patch unit information can still be obtained after the **patch health-proc** command is executed, contact maintenance engineers.


Example
-------

# Delete all patches.
```
<HUAWEI> patch delete all
This will delete all the patch. Are you sure? [Y/N]:y
Info: Operating, please wait for a moment...............done.
Info: Succeeded in deleting the patch.

```