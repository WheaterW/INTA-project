upgrade feature-software
========================

upgrade feature-software

Function
--------



The **upgrade feature-software** command upgrades a feature package.



By default, no feature package is installed in the system. Therefore, you do not need to perform the upgrade.


Format
------

**upgrade feature-software** { *feature-file* } &<1-9>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **feature-software** *feature-file* | Specifies the name of an independent feature package or the name of the feature in the basic package. | The value is a string of 1 to 127 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If a new feature software package is released, you can perform the upgrade only when the new feature software package has been installed in the current environment.

**Precautions**

Do not install the feature packages with the version being the same as the existing one. Before the upgrade, the feature packages of the same type but of different versions must be installed.


Example
-------

# Upgrade the feature package
```
<HUAWEI> upgrade feature-software IGPV100R002C10.ccx
Info: Operating, please wait for a moment........done.
Info: Succeeded in upgrading the feature.

```

# Upgrade feature packages in batches.
```
<HUAWEI> upgrade feature-software V100R002C00B001-PNF_Feature1.ccx V100R002C00B001-PNF_Feature2.ccx
Info: Operating, please wait for a moment........................................done.
Info: Succeeded in upgrading the software.

```