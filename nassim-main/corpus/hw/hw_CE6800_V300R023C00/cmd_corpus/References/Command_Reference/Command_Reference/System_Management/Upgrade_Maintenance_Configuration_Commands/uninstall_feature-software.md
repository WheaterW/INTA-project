uninstall feature-software
==========================

uninstall feature-software

Function
--------



The **uninstall feature-software** command uninstalls a feature package.




Format
------

**uninstall feature-software** { *feature-file* } &<1-9>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **feature-software** *feature-file* | Specifies the name of a feature package. | The value is a string of 1 to 127 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If the installed feature package is not required, you can run this command to uninstall it to save system resources.

**Precautions**

When a feature package is uninstalled, the patch package corresponding to the feature package is automatically uninstalled.


Example
-------

# Uninstall the feature package.
```
<HUAWEI> uninstall feature-software IGPV100R001C10.ccx
Info: Checking, please wait for a moment...done.
Warning: This will uninstall the package IGPV100R001C10.ccx, Continue? [Y/N]:y
Info: Start to uninstall the package IGPV100R001C10.ccx.
Info: Operating, please wait for a moment...done.
Info: Succeeded in uninstalling the software.

```

# Uninstall feature packages in batches.
```
<HUAWEI> uninstall feature-software V100R001C00B001-PNF_Feature1.ccx V100R001C00B001-PNF_Feature2.ccx
Info: Checking, please wait for a moment...done.
Warning: This will uninstall the package V100R001C00B001-PNF_Feature2.ccx,V100R001C00B001-PNF_Feature1.ccx, Continue? [Y/N]:y
Info: Start to uninstall the package V100R001C00B001-PNF_Feature2.ccx.
Info: Operating, please wait for a moment..done.
Info: Succeeded in uninstalling the software.
Info: Start to uninstall the package V100R001C00B001-PNF_Feature1.ccx.
Info: Operating, please wait for a moment...done.
Info: Succeeded in uninstalling the software.

```