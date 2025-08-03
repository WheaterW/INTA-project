upgrade application-software
============================

upgrade application-software

Function
--------



The **upgrade application-software** command upgrades the image software package in an open application system.




Format
------

**upgrade application-software** *software-path*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *software-path* | Specifies the name of the image software package to be upgraded. | The value is a string of 1 to 127 case-sensitive characters without spaces. |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **upgrade application-software** command to upgrade the image software package and update the application by replacing the software package.

**Precautions**

* Before the upgrade, upload the image software package of the new version to flash:/oas/images/.
* The .tar file name in the image software package of the new version must be the same as that in the image software package to be upgraded.

Example
-------

# Upgrade the image software package.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] upgrade application-software oas-test-healthy.zip
Warning: The software package will be upgraded and the applications using the software package will be reset. Continue? [Y/N]:y
Info: Operating, please wait for a moment.............................................done.
Info: The application software package is upgraded successfully.

```