uninstall extended-system-software
==================================

uninstall extended-system-software

Function
--------



The **uninstall extended-system-software** command uninstalls a system extension package.



By default, only system extension packages that are not in use can be uninstalled.


Format
------

**uninstall extended-system-software** { *file-name* } &<1-4>


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

If an installed system extension package is no longer required, run this command to uninstall it to save system resources. For example, you can run this command to uninstall a hardware package, which is a system extension package.


Example
-------

# Uninstall the system extension package.
```
<HUAWEI> uninstall extended-system-software Hardpkg_V800R011C10B560.cch Hardpkg_V800R012C00B560.cch
Warning: This will uninstall the package Hardpkg_V800R011C10B560.cch,Hardpkg_V800R012C00B560.cch, Continue? [Y/N]:Y
Info: Start to uninstall the package Hardpkg_V800R011C10B560.cch.
Info: Operating, please wait for a moment.....done.
Info: Succeeded in uninstalling the software.
Info: Start to uninstall the package Hardpkg_V800R012C00B560.cch.
Info: Operating, please wait for a moment....done.
Info: Succeeded in uninstalling the software.

```