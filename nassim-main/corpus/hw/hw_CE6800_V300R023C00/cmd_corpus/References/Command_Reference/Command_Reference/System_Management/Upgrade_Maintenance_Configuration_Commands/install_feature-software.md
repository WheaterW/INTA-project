install feature-software
========================

install feature-software

Function
--------



The **install feature-software** command installs a feature package.



By default, a specified feature package is installed.


Format
------

**install feature-software** { *feature-file* } &<1-9>


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

If the released package contains a feature package, you can run this command to install the feature package.


Example
-------

# Install feature packages in batches.
```
<HUAWEI> install feature-software V100R001C00B001-PNF_Feature1.ccx V100R001C00B001-PNF_Feature2.ccx
Info: Checking, please wait for a moment....done.
Info: Start to install the package V100R001C00B001-PNF_Feature1.ccx.
Info: Operating, please wait for a moment...done.
Info: Succeeded in installing the software.
Info: Start to install the package V100R001C00B001-PNF_Feature2.ccx.
Info: Operating, please wait for a moment....done.
Info: Succeeded in installing the software.

```

# Install the feature package.
```
<HUAWEI> install feature-software IGPV100R001C10.ccx
Info: Checking, please wait for a moment...done.
Info: Start to install the package IGPV100R001C10.ccx.
Info: Operating, please wait for a moment....done.
Info: Succeeded in installing the software.

```