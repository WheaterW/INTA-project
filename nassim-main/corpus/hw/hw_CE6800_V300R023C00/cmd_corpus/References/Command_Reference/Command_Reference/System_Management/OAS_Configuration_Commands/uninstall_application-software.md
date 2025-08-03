uninstall application-software
==============================

uninstall application-software

Function
--------



The **uninstall application-software** command uninstalls an image software package.




Format
------

**uninstall application-software** *software-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *software-name* | Specifies the image software package to be uninstalled. | The value is a string of 1 to 127 case-sensitive characters without spaces. |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After OAS is enabled, you can run this command to uninstall the image software package.

**Precautions**

Before uninstalling the image software package, you need to delete related applications.


Example
-------

# Uninstall the image software package.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] uninstall application-software oas1234567890.zip
Warning: The application software package oas1234567890.zip will be uninstalled. Continue? [Y/N]:Y
Info: The application software package is uninstalled successfully.

```