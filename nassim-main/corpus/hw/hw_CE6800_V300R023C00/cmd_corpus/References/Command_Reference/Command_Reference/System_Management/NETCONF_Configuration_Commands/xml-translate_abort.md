xml-translate abort
===================

xml-translate abort

Function
--------



The **xml-translate abort** command stops the CLI-to-XML translation.




Format
------

**xml-translate abort**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

In the translation mode, after the configuration commands to be translated are executed, to stop the CLI-to-XML translation, run the xml-translate abort command.

**Prerequisites**

The CLI-to-XML translation mode has been accessed using the **xml-translate begin** command, and all the configuration commands to be translated have been executed.

**Configuration Impact**

After the xml-translate abort command is run, the current running configuration database is unlocked, and the system view is returned.

**Precautions**



Only administrator users (at level 3 or 15) can run the xml-translate abort command.




Example
-------

# Stop the CLI-to-XML translation.
```
<HUAWEI> system-view
[~HUAWEI] xml-translate begin
Warning: The running database will be locked when you enter the CLI-to-XML translate mode. Continue? [Y/N]:y
[&HUAWEI] acl 2001
[&HUAWEI-acl4-basic-2001] quit
[&HUAWEI] xml-translate abort

```