startup extended-system-software
================================

startup extended-system-software

Function
--------



The **startup extended-system-software** command sets the system extended package for the next startup.



By default, the system extension package for the next startup is specified for the corresponding model.


Format
------

**startup extended-system-software** { *file-name* } &<1-4>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *file-name* | Specifies the name of a system extension package. | The value is a string of 5 to 127 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can run this command to set the system extended package for the next startup. For example, you can run this command to set a hardware package, which is a system extension package.


Example
-------

# Set the extended system package for the next startup.
```
<HUAWEI> startup extended-system-software Hardpkg2_V800R012C00SPC101.cch Hardpkg2_V800R012C10SPC102.cch
Info: Start to set the package Hardpkg2_V800R012C00SPC101.cch.
Info: Operating, please wait for a moment........done.
Info: Succeeded in setting the software package for next startup.
Info: Start to set the package Hardpkg2_V800R012C10SPC102.cch.
Info: Operating, please wait for a moment........done.
Info: Succeeded in setting the software package for next startup.

```