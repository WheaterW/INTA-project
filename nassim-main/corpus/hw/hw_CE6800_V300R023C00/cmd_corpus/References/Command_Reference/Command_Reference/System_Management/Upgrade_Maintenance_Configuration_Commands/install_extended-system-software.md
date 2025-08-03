install extended-system-software
================================

install extended-system-software

Function
--------



The **install extended-system-software** command installs the system extension package.



By default, the system extension package of the corresponding model is installed.


Format
------

**install extended-system-software** { *file-name* } &<1-4>


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

**Usage Scenario**

This command is used to install the system extension package. For example, you can run this command to install a hardware package, which is a system extension package.


Example
-------

# Install the system extension package.
```
<HUAWEI> install extended-system-software Hardpkg_V800R011C10B560.cch Hardpkg_V800R012C00B560.cch
Info: Start to install the package Hardpkg_V800R011C10B560.cch.
Info: Operating, please wait for a moment........done.
Info: Succeeded in installing the software.
Info: Start to install the package Hardpkg_V800R012C00B560.cch.
Info: Operating, please wait for a moment.......done.
Info: Succeeded in installing the software.

```