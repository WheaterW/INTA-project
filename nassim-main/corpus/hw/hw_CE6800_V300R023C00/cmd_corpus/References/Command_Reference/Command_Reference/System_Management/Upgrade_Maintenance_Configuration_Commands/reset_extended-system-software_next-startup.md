reset extended-system-software next-startup
===========================================

reset extended-system-software next-startup

Function
--------



The **reset extended-system-software next-startup** command clears the extended system package setting for the next startup.



By default, the specified extension package for the next startup is cleared.


Format
------

**reset extended-system-software next-startup** { *file-name* } &<1-4>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *file-name* | Specifies the name of an extended system package. | The value is a string of 5 to 127 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

If the specified extended system software package for next startup is no longer required, run the reset system extended-package command to clear it. For example, you can run this command to clear a hardware package, which is a system extension package.


Example
-------

# Clear the extended system package setting for the next startup.
```
<HUAWEI> reset extended-system-software next-startup Hardpkg2_V800R012C00SPC101.cch Hardpkg2_V800R012C10SPC102.cch
Info: Start to reset the package Hardpkg2_V800R012C00SPC101.cch.
Info: Operating, please wait for a moment......done.
Info: Succeeded in clearing the software package for next startup.
Info: Start to reset the package Hardpkg2_V800R012C10SPC102.cch.
Info: Operating, please wait for a moment......done.
Info: Succeeded in clearing the software package for next startup.

```