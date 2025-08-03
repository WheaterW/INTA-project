upgrade extended-system-software
================================

upgrade extended-system-software

Function
--------



The **upgrade extended-system-software** command upgrades the system extension package.



By default, the specified system extension package is upgraded.


Format
------

**upgrade extended-system-software** *file-name*


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

After a new system extension package is released, you can perform the upgrade if you have identified that the system extension package needs to be upgraded and the system extension package of this type has been installed in the current environment. For example, you can run this command to upgrade a hardware package, which is a system extension package.

**Precautions**

The system extension package of the same version cannot be upgraded. Before the upgrade, the system extension package of the same type but a different version must have been installed.


Example
-------

# Upgrade the system extension package.
```
<HUAWEI> upgrade extended-system-software Hardpkg2_V800R012C00SPC101.cch
Info: Operating, please wait for a moment..................................done.
Info: Succeeded in upgrading the software.

```